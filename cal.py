import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart CGPA Calculator", layout="centered")

st.title("🎓 Smart GPA & CGPA Calculator")
st.write("Enter your subjects, marks, and credit hours to calculate your GPA and CGPA.")

# Semester Information
semester = st.number_input("Enter Current Semester Number", min_value=1, step=1)
num_subjects = st.number_input("Number of Subjects in this Semester", min_value=1, step=1)

# Data entry for subjects
subjects = []
total_points = 0
total_credits = 0

st.subheader("📘 Subject Details")
for i in range(int(num_subjects)):
    st.markdown(f"**Subject {i+1}**")
    marks = st.number_input(f"Enter Marks for Subject {i+1}", min_value=0, max_value=100, step=1)
    credit = st.number_input(f"Enter Credit Hours for Subject {i+1}", min_value=1, step=1, key=f"credit_{i}")

    # Convert marks to grade points
    if marks >= 84:
        gp = 4.0
    elif marks >= 80:
        gp = 3.7
    elif marks >= 75:
        gp = 3.3
    elif marks >= 70:
        gp = 3.0
    elif marks >= 65:
        gp = 2.7
    elif marks >= 60:
        gp = 2.3
    elif marks >= 55:
        gp = 2.0
    elif marks >= 50:
        gp = 1.7
    else:
        gp = 0.0

    total_points += gp * credit
    total_credits += credit
    subjects.append({"Subject": f"Subject {i+1}", "Marks": marks, "Credit Hours": credit, "GPA": gp})

# Display subject-wise table
df = pd.DataFrame(subjects)
st.table(df)

# GPA calculation
if total_credits > 0:
    gpa = total_points / total_credits
else:
    gpa = 0

st.subheader("🎯 Current Semester GPA:")
st.success(f"{gpa:.2f}")

# CGPA section
if semester > 1:
    st.subheader("🧾 Previous Semester Details")
    prev_cgpa = st.number_input("Enter Previous CGPA", min_value=0.0, max_value=4.0, step=0.01)
    prev_credits = st.number_input("Enter Total Credit Hours Till Last Semester", min_value=1, step=1)
    cgpa = ((prev_cgpa * prev_credits) + (gpa * total_credits)) / (prev_credits + total_credits)
    st.subheader("🏆 Updated CGPA:")
    st.success(f"{cgpa:.2f}")
else:
    st.info("Only 1st Semester Data — CGPA = GPA")

# Footer
st.markdown("---")
st.caption("Developed by Sikandar Ali | COMSATS University")
