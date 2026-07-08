import streamlit as st
from parser import (
    extract_text_from_pdf,
    extract_email,
    extract_phone,
    extract_name,
    extract_skills,
    extract_education,
    extract_projects
)

st.set_page_config(page_title="Resume Parser", page_icon="📄")

st.title("📄 Resume Parser")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    text = extract_text_from_pdf(uploaded_file)

    name = extract_name(text)
    email = extract_email(text)
    phone = extract_phone(text)
    education = extract_education(text)
    skills = extract_skills(text)
    projects = extract_projects(text)

    st.success("Resume uploaded successfully!")

    st.markdown("## 👤 Personal Details")
    st.write(f"**Name:** {name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Phone:** {phone}")

    st.markdown("---")

    st.markdown("## 🎓 Education")

    if education:
        for edu in education:
            st.markdown(f"**{edu['course']}**")
            st.write(edu["details"])
            st.write("")
    else:
        st.write("Not Found")

    st.markdown("---")

    st.markdown("## 🛠 Skills")

    if skills:
        cols = st.columns(3)

        for i, skill in enumerate(skills):
            cols[i % 3].write(f"✅ {skill}")
    else:
        st.write("No Skills Found")

    st.markdown("---")

    st.markdown("## 💼 Projects")

    if projects:
        for project in projects:
            st.write(f"• {project}")
    else:
        st.write("Not Found")

    st.markdown("---")

    with st.expander("📄 View Resume Text"):
        st.text(text)