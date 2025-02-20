import streamlit as st
import pandas as pd

# Header
st.title("Clinical Technology 2025 Intake")
#st.subheader("Select a person to view their details or select a question to view the responses.")

# Staff data
staff = {
    "Dr Lisa Repsold": {"Role":"Section Head & 1st Year Guardian","Subject speciality":"Physiology","LinkdIn profile":"xxxx","Office number":"012 382 6169","Email address":"RepsoldL@tut.ac.za", "Image":"./group.jpg"},
    "Ms Botlhale Magoshi": {"Role":"2nd Year Guardian","Subject speciality":"Anatomy","LinkdIn profile":"xxxx","Office number":"012 382 6119","Email address":"MagoshiB@tut.ac.za", "Image":"./botlhale.jpg"},
    "Ms Zelneri van Coppenhagen": {"Role":"3th Year Guardian","Subject speciality":"Work-integrated learning","LinkdIn profile":"xxxx","Office number":"012 382 6210","Email address":"VanCoppenhagen@tut.ac.za", "Image":"./zelneri.jpg"},
    "Ms Marinda Swart": {"Role":"4th Year Guardian","Subject speciality":"Biomedical Apparatus","LinkdIn profile":"xxxxc","Office number":"012 382 6263","Email address":"SwartM1@tut.ac.za", "Image":"./marinda.jpg"},
    "Mr Lynton Hazelhurst": {"Role":"Mentor","Subject speciality":"Pathophysiology","LinkdIn profile":"www.linkedin.com/in/lyntonhazelhurst","Office number":"012 382 6423","Email address":"HazelhurstLT@tut.ac.za", "Image":"./lynton.jpg"},
    "Ms Obakeng Botshielo": {"Role":"Post graduate Assistant","Subject speciality":"Research","LinkdIn profile":"xxxx","Office number":"012 382 6169","Email address":"BotshieloO@tut.ac.za", "Image":"./obakeng.jpg"}
}

# Staff questionnaire data
staff_data = {"Staff": ["Dr Lisa Repsold","Ms Botlhale Magoshi","Ms Zelneri van Coppenhagen","Ms Marinda Swart","Mr Lynton Hazelhurst","Ms Obakeng Botshielo"],
        "Favorite category(s)": ["Reproductive Biology","Reproductive Biology","Critical Care","Cardiology","Cardio-Vascular & Neurophysiology","Nephrology & Cardiology"],
        "Netflix / Showmax": ["Netflix","Netflix","Netflix","Netflix","Netflix","Showmax"],
        "Waffles / Pancakes": ["Pancakes","Waffles","Pancakes","Waffles","Waffles","Pancakes"],
        "Sunrise / Sunset": ["Sunset","Sunrise","Sunset","Sunrise","Sunrise","Sunset"],
        "Crunchy Peanut Butter / Smooth Peanut Butter": ["CRUNCHY!","Crunchy","Crunchy","Crunchy","Smooth","Smooth"],
        "Summer / Winter": ["Winter","Summer","Summer","Summer","Summer","Summer"],
        "Android / iPhone": ["Android","Android","Android","Android","iPhone","Android"],
        "Bushveld / Beach": ["Bushveld","Beach","Bushveld","Beach","Beach","Bushveld"],
        "Word to describe the future":  ["promising","bright","hopeful","action","optimistic","exciting"],
        }

# Convert staff questionnaire data to dataframe
staff_data_df = pd.DataFrame(staff_data)

# Sidebar
view_option = st.sidebar.radio("", ["Staff Member Profile", "Student Question Responses"])

if view_option == "Staff Member Profile":
    selected_person = st.sidebar.selectbox("Select a person", [""] + staff_data_df["Staff"].tolist())
    if selected_person:
        details = next((v for k, v in staff.items() if selected_person in k), None)
        if details:
            st.write(f"**Name:** {selected_person}")
            st.write(f"**Role:** {details['Role']}")
            st.write(f"**Subject speciality:** {details['Subject speciality']}")
            st.write(f"**LinkdIn profile:** {details['LinkdIn profile']}")
            st.write(f"**Office number:** {details['Office number']}")
            st.write(f"**Email address:** {details['Email address']}")
            # Display image with specified dimensions
            st.image(details["Image"], width=150)
        
        # Display responses in a table
        person_responses = staff_data_df[staff_data_df["Staff"] == selected_person]
        st.write("**Responses:**")
        st.table(person_responses.T.rename(columns={person_responses.index[0]: "Response"}).drop("Staff"))

elif view_option == "Student Question Responses":
    question = st.sidebar.selectbox("Select a question", [
        "",
        "Category Choice",
        "Netflix/Showmax", 
        "Pancakes/Waffles", 
        "Sunrise/Sunset", 
        "Crunchy Peanut Butter/Smooth Peanut Butter", 
        "Summer/Winter", 
        "Android/iPhone", 
        "Bushveld/Beach",
        "WordCloud"
    ])
    if question:
        if question == "Category Choice":
            st.image("./category.png")
        elif question == "Netflix/Showmax":
            st.image("./q1.png")
        elif question == "Pancakes/Waffles":
            st.image("./q2.png")
        elif question == "Sunrise/Sunset":
            st.image("./q3.png")
        elif question == "Crunchy Peanut Butter/Smooth Peanut Butter":
            st.image("./q4.png")
        elif question == "Summer/Winter":
            st.image("./q5.png")
        elif question == "Android/iPhone":
            st.image("./q6.png")
        elif question == "Bushveld/Beach":
            st.image("./q7.png")
        elif question == "WordCloud":
           st.image("./wordcloud.png")

# Footer
st.markdown("---")
st.write("BHSc Clinical Technology")

# Styling
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    .stApp {
        background-color: #ffffff;
        color: #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)