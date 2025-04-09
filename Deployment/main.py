import streamlit as st
import pickle

st.title("🧠 Mental Health Detection")

st.subheader("Enter Your Details")

work_hours = st.number_input("🕒 Working hours per week", min_value=20, max_value=70)
Family_history = st.selectbox("👨‍👩‍👧 Family history of mental health issues?", ("Yes", "No"))
sleep = st.number_input("😴 Sleep hours per day", min_value=4, max_value=10)
stress = st.slider("😰 Stress levels (1-10)", min_value=0, max_value=10)
physical_activity = st.number_input("🏃 Physical activity (minutes/day)", min_value=0, max_value=180)
social_interaction = st.slider("🗣️ Social interaction level (1-10)", min_value=0, max_value=10)
Diet = st.selectbox("🍽️ Diet quality", ("Good", "Average", "Poor"))

with open("encoder.pkl",'rb') as file:
    encode=pickle.load(file)
with open("xgboost_model.pkl","rb") as file:
    model=pickle.load(file)
import pandas as pd
# df=pd.DataFrame([[Age,Gender,work_hours,Family_history,sleep,stress,physical_activity,social_interaction,Diet]],columns=['Age', 'Gender', 'Work Hours', 'Family History', 'Sleep Hours','Stress Level', 'Physical Activity', 'Social Interaction','Diet Quality'])
df=pd.DataFrame([[work_hours,Family_history,sleep,stress,physical_activity,social_interaction,Diet]],columns=['Work Hours', 'Family History', 'Sleep Hours','Stress Level', 'Physical Activity', 'Social Interaction','Diet Quality'])



from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
if st.button("🔍 Predict"):
    transformed_df = encode.transform(df)

    prediction = model.predict(transformed_df)[0]

    if prediction == 1:
        st.warning("⚠️ You may be at risk for mental health issues. It's recommended to take some self-care actions.")
    else:
        st.success("✅ You're doing well! Keep up the good habits.")


    st.subheader("💡 Personalized Tips to Boost Your Mental Health")

    prompt_template = ChatPromptTemplate(messages=[
        ("system", "You're an AI mental health improving suggester based on the user's details. "
                   "Suggest simple and effective daily activities that match their lifestyle, such as listening to music, "
                   "maintaining a proper diet, improving social interactions, and similar beneficial habits. "
                   "Return suggestions with 2 lines of explanation."),
        ("human", "Here's my details about daily activities: {activity_details}")
    ])

    api_key = "AIzaSyC9j5KaPVcanw9nvPAfKfORBqsCzBjx37I"

    genai_model = ChatGoogleGenerativeAI(api_key=api_key, model="gemini-2.0-flash")
    output_parser = StrOutputParser()
    chain = prompt_template | genai_model | output_parser

    # Get personalized suggestion
    tips = chain.invoke({"activity_details": str(df)})
    st.write(tips)