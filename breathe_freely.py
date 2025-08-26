import streamlit as st

st.title("Breathe Freely: Помощник отказа от курения")

if "days_no_smoke" not in st.session_state:
    st.session_state["days_no_smoke"] = 0

if st.button("Сегодня не курил"):
    st.session_state["days_no_smoke"] += 1

st.markdown(f"**Дней без сигарет:** {st.session_state['days_no_smoke']}")

emotion = st.text_input("Что чувствуешь сегодня? Какие были триггеры?")
if emotion:
    st.write(f"Эмоции за сегодня: {emotion}")

motivation = [
    "Каждый день без сигарет — победа над собой!",
    "Сегодня ты стал здоровее.",
    "Ты вдохновляешь других своим примером.",
    "Дыши свободно и легко!"
]
if st.button("Получить мотивацию"):
    msg_id = st.session_state['days_no_smoke'] % len(motivation)
    st.info(motivation[msg_id])

st.markdown("---")
st.markdown("Внимание: если чувствуешь сильную тягу — попробуй сделать вдох, задержку на 4 секунды и медленный выдох.")
