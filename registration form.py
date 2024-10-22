%%writefile app.py

import streamlit as st

# Function to create the registration form
st.title("University Registration Form")

st.header("Student Details")

# Student information
student_name = st.text_input("Student Name")
student_number = st.text_input("Student Phone Number",max_chars=10)
student_gender = st.selectbox("Gender", ["","Male", "Female", "Other"],placeholder="Select Gender")
student_blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"],placeholder="Select Blood group")
student_age = st.number_input("Age", min_value=1,max_value=100, step=1)
student_email = st.text_input("Student Email ID")

st.header("Parents or Guardian Information")

# Choose between Parents or Guardian
option = st.radio("Are you registering with Parents or a Guardian?", ("Parents", "Guardian"))

if option == "Parents":
    st.subheader("Parents Details")

    # Parent details
    father_name = st.text_input("Father's Name")
    mother_name = st.text_input("Mother's Name")
    father_phone = st.text_input("Father's Phone Number",max_chars=10)
    mother_phone = st.text_input("Mother's Phone Number",max_chars=10)
    father_email = st.text_input("Father's Email ID")
    mother_email = st.text_input("Mother's Email ID")

else:
    st.subheader("Guardian Details")

    # Guardian details
    guardian_name = st.text_input("Guardian's Name")
    guardian_phone = st.text_input("Guardian's Phone Number",max_chars=10,)
    guardian_email = st.text_input("Guardian's Email ID")
    guardian_relationship = st.text_input("Relationship with Student")

st.header("Academic Information")

# Academic information (marks)
grade_10 = st.number_input("Grade 10 Marks (%)", min_value=0.0, max_value=100.0, step=0.1)
grade_11 = st.number_input("Grade 11 Marks (%)", min_value=0.0, max_value=100.0, step=0.1)
grade_12 = st.number_input("Grade 12 Marks (%)", min_value=0.0, max_value=100.0, step=0.1)

# Submit button
if st.button("Submit"):
    st.success("Form submitted successfully!")
    # Display the entered information (for testing purposes)
    st.write("Student Name:", student_name)
    st.write("Phone Number:", student_number)
    st.write("Gender:", student_gender)
    st.write("Blood Group:", student_blood_group)
    st.write("Age:", student_age)
    st.write("Email ID:", student_email)

    if option == "Parents":
        st.write("Father's Name:", father_name)
        st.write("Mother's Name:", mother_name)
        st.write("Father's Phone Number:", father_phone)
        st.write("Mother's Phone Number:", mother_phone)
        st.write("Father's Email ID:", father_email)
        st.write("Mother's Email ID:", mother_email)
    else:
        st.write("Guardian's Name:", guardian_name)
        st.write("Guardian's Phone Number:", guardian_phone)
        st.write("Guardian's Email ID:", guardian_email)
        st.write("Relationship with Student:", guardian_relationship)

    st.write("Grade 10 Marks:", grade_10)
    st.write("Grade 11 Marks:", grade_11)
    st.write("Grade 12 Marks:", grade_12)

