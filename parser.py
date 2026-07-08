import pdfplumber
import re


def extract_text_from_pdf(uploaded_file):

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_email(text):

    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_phone(text):

    pattern = r'(\+91[\s-]?)?[6-9]\d{9}'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_name(text):

    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if line:
            return line

    return "Not Found"


def extract_education(text):

    education = []

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        upper = line.upper()

        if "B.TECH" in upper:

            education.append({
                "course": "B.Tech (ECE)",
                "details": line
            })

        elif "INTERMEDIATE" in upper:

            education.append({
                "course": "Intermediate",
                "details": line
            })

        elif upper.startswith("SSC"):

            education.append({
                "course": "SSC",
                "details": line
            })

    return education


def extract_skills(text):

    skills_list = [
        "Python",
        "Java",
        "JavaScript",
        "HTML",
        "CSS",
        "SQL",
        "MySQL",
        "Git",
        "GitHub",
        "Flask",
        "Streamlit",
        "Machine Learning",
        "Deep Learning",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "TensorFlow",
        "PyTorch",
        "OpenCV",
        "REST API",
        "Google Gemini API"
    ]

    found_skills = []

    for skill in skills_list:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills


def extract_projects(text):

    projects = []

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        upper = line.upper()

        if "QUIZ MANAGEMENT" in upper:
            projects.append("Quiz Management Web Application")

        if "AI SECOND BRAIN" in upper:
            projects.append("AI Second Brain")

    return list(dict.fromkeys(projects))