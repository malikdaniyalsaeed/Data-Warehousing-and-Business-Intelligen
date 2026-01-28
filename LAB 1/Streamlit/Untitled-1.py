# filename: gpa_cgpa_app.py
import streamlit as st

st.title("GPA & CGPA Calculator")

# --- GPA Section ---
st.header("GPA Calculator")

courses = ["DS", "AI", "DB", "IS"]

credits = []
marks = []

col1, col2 = st.columns(2)

for course in courses:
    with col1:
        cr = st.number_input(f"{course} Credit Hours", min_value=0, value=3)
    with col2:
        mk = st.number_input(f"{course} Marks", min_value=0, max_value=100, value=75)
    credits.append(cr)
    marks.append(mk)


def marks_to_gp(mark):
    if mark >= 85:
        return 4.0
    elif mark >= 80:
        return 3.7
    elif mark >= 75:
        return 3.3
    elif mark >= 70:
        return 3.0
    elif mark >= 65:
        return 2.7
    elif mark >= 60:
        return 2.3
    elif mark >= 55:
        return 2.0
    elif mark >= 50:
        return 1.7
    else:
        return 0.0


if st.button("Calculate GPA"):
    total_points = sum([marks_to_gp(marks[i]) * credits[i] for i in range(4)])
    total_credits = sum(credits)
    gpa = total_points / total_credits
    st.success(f"Your GPA is: {gpa:.2f}")

# --- CGPA Section ---
st.header("CGPA Calculator")

prev_gpa = st.number_input("Previous GPA", min_value=0.0, max_value=4.0, value=2.8)
prev_credits = st.number_input("Previous Credit Hours", min_value=0, value=11)
current_gpa = st.number_input("Current GPA", min_value=0.0, max_value=4.0, value=3.0)
current_credits = st.number_input("Current Credit Hours", min_value=0, value=11)

if st.button("Calculate CGPA"):
    cgpa = ((prev_gpa * prev_credits) + (current_gpa * current_credits)) / (
        prev_credits + current_credits
    )
    st.success(f"Your CGPA is: {cgpa:.2f}")
