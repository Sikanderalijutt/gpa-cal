import streamlit as st
import pandas as pd

# --------------------------- #
# 🎓 SMART GPA & CGPA CALCULATOR
# --------------------------- #

st.set_page_config(page_title="Smart CGPA Calculator", layout="centered")

# Title & intro
st.title("🎓 Smart GPA & CGPA Calculator")
st.write("Enter your marks, credit hours, and semester information to calculate your GPA and CGPA.")

# --------------------------- #
# 🧮 Grade Conversion Function
# --------------------------- #
def marks_to_gpa(marks):
    if marks >= 84:
        return 4.0
    elif marks >= 80:
        return 3.7
    elif marks >= 75:
        return 3.3
    elif marks >= 70:
        return 3.0
    elif marks >= 65:
        return 2.7
    elif marks >= 60:
        return 2.3
    elif marks >= 55:
        return 2.0
    elif marks >= 50:
        return 1.7
    else:
        return 0.0

# --------------------------- #
# 📘 Semester Input Section
# --------------------------- #
semester = st.number_input("Enter Current Semester Number", min_value=1, step=1)
num_subjects = st.number_input("Enter Number of Subjects This Semester", min_value=1, step=1)

subjects = []
total_points = 0.0
total_credits = 0

st.subheader("📚 Subject Details")

# Subject input fields
for i in range(int(num_subjects)):
    st.markdown(f"**Subject {i+1}**")
    col1, col2 = st.columns(2)
    with col1:
        marks = st.number_input(f"Marks (0–100)", min_value=0, max_value=100, step=1, key=f"marks_{i}")
    with col2:
        credit = st.number_input(f"Credit Hours", min_value=1, max_value=5, step=1, key=f"credit_{i}")
    
    gp = marks_to_gpa(marks)
    subjects.append({
        "Subject": f"Subject {i+1}",
        "Marks": marks,
        "Credit Hours": credit,
        "Grade Point": gp
    })
    total_points += gp * credit
    total_credits += credit

# Show table
df = pd.DataFrame(subjects)
st.dataframe(df, use_container_width=True)

# --------------------------- #
# 🎯 GPA Calculation
# --------------------------- #
if total_credits > 0:
    gpa = total_points / total_credits
else:
    gpa = 0.0

st.subheader("🎯 Current Semester GPA:")
st.success(f"{gpa:.2f}")

# --------------------------- #
# 🏆 CGPA Calculation
# --------------------------- #
if semester > 1:
    st.subheader("🧾 Previous Semester Details")
    prev_cgpa = st.number_input("Enter Previous CGPA", min_value=0.0, max_value=4.0, step=0.01)
    prev_credits = st.number_input("Enter Total Credit Hours Till Previous Semester", min_value=1, step=1)

    cgpa = ((prev_cgpa * prev_credits) + (gpa * total_credits)) / (prev_credits + total_credits)
    st.subheader("🏆 Updated CGPA:")
    st.success(f"{cgpa:.2f}")
else:
    st.info("You're in 1st Semester — CGPA = GPA")

# --------------------------- #
# 📄 Footer
# --------------------------- #
st.markdown("---")
st.caption("Developed by **Sikandar Ali | COMSATS University**")
