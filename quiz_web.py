# quiz_web.py  — NO HINTS VERSION
import json
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Richa's Quiz", page_icon="🎯")
st.title("🎯 Welcome to Richa's Quiz!")

# Always load questions.json from same folder as this file
QUESTIONS_PATH = Path(__file__).parent / "questions.json"
questions = json.loads(QUESTIONS_PATH.read_text(encoding="utf-8"))

# Keep user choices and submit state
if "choices" not in st.session_state:
    st.session_state.choices = [None] * len(questions)
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Render questions (NO hints shown anywhere)
for i, q in enumerate(questions, start=1):
    st.subheader(f"{i}. {q['question']}")
    st.session_state.choices[i-1] = st.radio(
        "Choose one:",
        q["options"],
        index=None if st.session_state.choices[i-1] is None
        else q["options"].index(st.session_state.choices[i-1]),
        key=f"q{i}"
    )
    st.write("")  # spacing

# Submit button
if st.button("Submit"):
    st.session_state.submitted = True

# After submit: show ONLY score (still no hints)
if st.session_state.submitted:
    score = 0
    for i, q in enumerate(questions, start=1):
        chosen = st.session_state.choices[i-1]
        if chosen is not None and chosen == q["options"][q["answer"]]:
            score += 1
    st.markdown(f"## 🏁 You scored **{score}/{len(questions)}** 🎉")

    # (Optional) Answer key toggle — delete this block if you want ZERO answers shown
    if st.checkbox("Show answer key"):
        for i, q in enumerate(questions, start=1):
            st.write(f"**Q{i}**: {q['question']}")
            st.write(f"✅ Correct: {q['options'][q['answer']]}")
            st.write("---")

# Reset button
if st.button("Reset quiz"):
    st.session_state.clear()
    st.rerun()

