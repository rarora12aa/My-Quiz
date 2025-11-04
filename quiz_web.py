import streamlit as st
import json

st.set_page_config(page_title="Richa's Quiz", page_icon="🎯")

st.title("🎯 Welcome to Richa's Quiz!")

with open("questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

score = 0
for i, q in enumerate(questions, start=1):
    st.subheader(f"{i}. {q['question']}")
    answer = st.radio("Choose one:", q["options"], key=i)
    correct = q["options"][q["answer"]]
    if answer == correct:
        st.success("✅ Correct!")
        score += 1
    else:
        st.info(f"💡 Correct answer: {correct}")
    st.divider()

st.markdown(f"## 🏁 You scored **{score}/{len(questions)}** points! 🎉")
