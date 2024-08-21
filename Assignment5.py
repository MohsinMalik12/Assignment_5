import requests
import smtplib

# ***********************************************************************

SHEETY_API_URL = "https://api.sheety.co/5bbfea1b90a734ec9220eb3768269753/intermediateStudentsData/intermediateStudentsData"

def student_details() :
    
    response = requests.get(url=SHEETY_API_URL)
    data = response.json()
    return data.get("intermediateStudentsData")

# ***********************************************************************

def check_student_percentage(intermediate_total_marks, student_obtained_marks) :

    student_percentage_float =  ( student_obtained_marks / intermediate_total_marks ) * 100
    student_percentage_integer = int(student_percentage_float)
    return student_percentage_integer

# ***********************************************************************

def check_fields(student_percentage, student_study_group) :

    recommended_fields = []

    if student_percentage >= 75 and student_study_group == 'Engineering':
        recommended_fields.append(' BS COMPUTER SCIENCE')
        recommended_fields.append(' SOFTWARE ENGINEERING')
        recommended_fields.append(' BIOMEDICAL ENGINEERING')
    if student_percentage >= 65 and student_study_group == 'Engineering':
        recommended_fields.append(' MECHANICAL ENGINEERING')
        recommended_fields.append(' ELECTRICAL ENGINEERING')
        recommended_fields.append(' TEXTILE ENGINEERING')
    if student_percentage >= 50 and student_study_group == 'Engineering':
        recommended_fields.append(' CIVIL ENGINEERING')
        recommended_fields.append(' CHEMICAL ENGINEERING')
        recommended_fields.append(' ENVIRONMENTAL ENGINEERING')
        recommended_fields.append(' ARCHITECTURE ENGINEERING')

    if student_percentage >= 85 and student_study_group == 'Biology':
        recommended_fields.append(' MEDICINE (MBBS)')
        recommended_fields.append(' DENTISTRY (BDS)')
    if student_percentage >= 75 and student_study_group == 'Biology':
        recommended_fields.append(' BS MICRO BIOLOGY')
        recommended_fields.append(' BS BIOCHEMISTRY')
        recommended_fields.append(' DR OF PHARMACY')
    if student_percentage >= 60 and student_study_group == 'Biology':
        recommended_fields.append(' BS PHYSIOLOGY')
        recommended_fields.append(' BS BIOSTATICS')
        recommended_fields.append(' BS ZOOLOGY')
        recommended_fields.append(' BS BOTANY')

    if student_percentage >= 85 and student_study_group == 'Commerce':
        recommended_fields.append(' ACCA')
        recommended_fields.append(' CA')
    if student_percentage >= 70 and student_study_group == 'Commerce':
        recommended_fields.append(' BUSINESS ADMINISTRATION')
        recommended_fields.append(' B.SC. IN ECONOMICS')
    if student_percentage >= 60 and student_study_group == 'Commerce':
        recommended_fields.append(' CERTIFIED PUBLIC ACCOUNTANT')
        recommended_fields.append(' BACHELOR IN FOREIGN TRADE')
        recommended_fields.append(' JOURNALISM AND MASS COMMUNICATION')
        recommended_fields.append(' DIGITAL MARKETING')
        
    if student_percentage >= 70 and student_study_group == 'Computer':
        recommended_fields.append(' SOFTWARE ENGINEERING')
        recommended_fields.append(' COMPUTER SCIENCE IN ARTIFICIAL INTELLIGENCE')
    if student_percentage >= 60 and student_study_group == 'Computer':
        recommended_fields.append(' COMPUTER SCIENCE IN CYBER SECURITY')
        recommended_fields.append(' COMPUTER SCIENCE IN NETWORKING')

    return recommended_fields

# ***********************************************************************

def send_email_to_student(student_email, recommend_fields, student_name, student_father_name) :

    Sender_Email = "your@gmail.com"
    Password = "xxxx xxxx xxxx xxxx"
    subject = f" RECOMMENDED FIELDS "
    body = f""" 
            STUDENT NAME : {student_name} .
            STUDENT FATHER NAME : {student_father_name} .
            RECOMMENDED FIELDS : {recommend_fields} .
            """
    message = f"Subject: {subject} \n\n {body}"
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(Sender_Email, Password)
    s.sendmail(Sender_Email, student_email, message)
    print(f"Email sent to {student_email} Successfully !")

# ***********************************************************************

for details in student_details() :
    student_name_lower = details["studentName"]
    student_name = student_name_lower.upper()
    student_father_name_lower = details["studentFatherName"]
    student_father_name = student_father_name_lower.upper()
    student_obtained_marks = details["studentObtainedMarks"]
    student_study_group = details["studentStudyGroup"]
    student_email = details["studentEmail"]
    intermediate_total_marks = 1100
    student_percentage = check_student_percentage(intermediate_total_marks, student_obtained_marks)
    recommend_fields = check_fields(student_percentage, student_study_group)
    send_email_to_student(student_email, recommend_fields, student_name, student_father_name)

# ***********************************************************************