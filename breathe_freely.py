import streamlit as st
import random
import pandas as pd
from datetime import date

# Названия и цвета
app_title = "🔥 Смелое решение!"
counter_title = "💪 Отвага в Днях"
main_color = "#2E8B57"
accent_color = "#4682B4"

# Расширенный список мотивационных цитат
motivations = [
    "«Смелость — начало всякого дела.» — Уильям Шекспир",
    "«Ты храбрее, чем ты думаешь, сильнее, чем кажешься, и умнее, чем ты думаешь.» — Кристофер Робин",
    "«Жизнь — это либо смелое приключение, либо ничего.» — Хелен Келлер",
    "«Смелость — не отсутствие страха, а победа над ним.» — Нельсон Мандела",
    "«Будь тем изменением, которое хочешь видеть в мире.» — Махатма Ганди",
    "«Вдохновение — это желание творить, и оно приходит к смелым.» — Фридрих Ницше",
    "«Только изменяя себя, меняется мир вокруг.» — Лев Толстой",
    "«Только те, кто рискует зайти слишком далеко, могут узнать, как далеко можно зайти.» — Томас Стернз Элиот",
    "«Смелость — сила, которая движет миром.» — Карл Юнг",
    "«Победа принадлежит самому упорному.» — Наполеон Бонапарт",
    "«Истинная смелость — это идти к цели несмотря на страх.» — Махатма Ганди",
    "«Самое лучшее время для действия — сейчас.» — Марк Твен",
    "«Ты не проиграл, пока не перестал пытаться.» — Альберт Эйнштейн",
    "«Смелость — это сопротивление страху, а не его отсутствие.» — Марк Твен",
    "«Твоя жизнь меняется в момент принятия решения.» — Антони Роббинс",
    "«Смелость в поступках — путь к великому.» — Конфуций",
    "«Преодолевая страх, мы обретаем свободу.» — Сенека",
    "«В каждом конце есть новое начало.» — Джон Леннон",
]

# HTML стили заголовков
st.markdown(f"<h1 style='text-align: center; color: {main_color};'>{app_title}</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align: center; color: {accent_color};'>{counter_title}</h2>", unsafe_allow_html=True)

# Инициализация прогресса (дни и даты)
if 'day_count' not in st.session_state:
    st.session_state.day_count = 0
if 'progress' not in st.session_state:
    st.session_state.progress = pd.DataFrame(columns=['Дата', 'Дни смелости'])

# Кнопка отметки дня смелости
if st.button("💥 Отметить день смелости"):
    choice = st.radio(
        "Как прошел сегодняшний день?",
        ("Сегодня без сигарет", "Сегодня был сложный день, но я все равно смелый")
    )
    if choice:
        st.session_state.day_count += 1
        today = date.today().strftime("%Y-%m-%d")
        new_row = pd.DataFrame({'Дата': [today], 'Дни смелости': [st.session_state.day_count]})
        st.session_state.progress = pd.concat([st.session_state.progress, new_row], ignore_index=True)
        st.success(random.choice(motivations))

# Показ счетчика
st.markdown(f"<p style='font-size: 24px; text-align: center; color: #555;'>{st.session_state.day_count} {counter_title.lower()}</p>", unsafe_allow_html=True)

# График прогресса
if not st.session_state.progress.empty:
    st.line_chart(data=st.session_state.progress.set_index('Дата')['Дни смелости'], use_container_width=True)

# Кнопка для дополнительной мотивации
if st.button("🌟 Получить мотивацию"):
    st.info(random.choice(motivations))
