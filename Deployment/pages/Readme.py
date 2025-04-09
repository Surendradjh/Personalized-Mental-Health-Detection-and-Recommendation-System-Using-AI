import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: #ff6347;  /* Background color */
    }

    /* Force all h1 tags (like st.title) to be white */
    h1 {
        color: white !important;
        text-align:left;
    }
    h3{ 
    color: #fffacd !important;
    text-align:left;
    padding-left: 50px;
    }
    p{
    color:#f5f5f5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("EDA For Mental Health Detection")

st.subheader("Background Story")
st.write("In today’s fast-paced world, mental health issues are becoming increasingly common, especially among individuals working in the IT industry. To address this growing concern, the goal of this project is to analyze daily activities of individuals, such as age, gender, sleep hours, stress levels, physical activity, social interaction, and more. By identifying patterns in this data, we aim to build a machine learning model that predicts whether an individual is likely to seek treatment for mental health concerns. This model will help in the early identification of at-risk individuals, enabling timely support and intervention to improve mental well-being.")
st.subheader("Objectice")
st.write("""To thoroughly understand and analyze people's daily activities, a large dataset is essential. However, due to the unavailability of open-source datasets containing such confidential information, we researched data from multiple health organizations, including the World Health Organization (WHO) and others. From these datasets, we extracted common features (e.g., age, gender, sleep hours, stress levels, physical activity, social interaction) for analysis.
         Based on the analyzed data, we aim to apply various machine learning algorithms and select the best-performing one to build a predictive model. By integrating Generative AI (GenAI), the model will take user inputs and provide personalized suggestions to improve mental well-being.""")
st.subheader("Key Steps")
st.write("""
- Analyze Data: Study the collected survey data to identify patterns and trends related to mental health.

- Apply Algorithms: Test multiple machine learning algorithms and select the one with the best performance.

- Build Model: Develop a predictive model using the selected algorithm to identify individuals at risk of mental health issues.

- Add GenAI: Integrate Generative AI to provide personalized suggestions based on user inputs.

- Provide Help: Offer actionable tips and recommendations to improve mental health and well-being.""")
st.subheader("Why This Approach?")
st.write("""
- Data-Driven Insights: Analyzing real-world data ensures accurate and meaningful results.

- Advanced Technology: Combining machine learning with Generative AI enables personalized and effective solutions.

- Proactive Support: Early identification and intervention can significantly improve mental health outcomes.
""")

st.subheader("Data Understaning:-")

st.markdown(
    """
    <style>
    .data-key {
        color: #fffacd;  /* Gold-ish yellow */
        font-weight: bold;
    }
    .data-desc {
        color: #f5f5f5;  /* Light gray for descriptions */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<ul>
  <li><span class="data-key">Age</span>: <span class="data-desc">Represents the age of the individual (in years).</span></li>
  <li><span class="data-key">Sleep Hours</span>: <span class="data-desc">Indicates how many hours of sleep the person gets per day.</span></li>
  <li><span class="data-key">Gender</span>: <span class="data-desc">Represents the gender of the individual (e.g., Male, Female, Others).</span></li>
  <li><span class="data-key">Physical Activity</span>: <span class="data-desc">Time (in minutes) the person spends on physical activity daily.</span></li>
  <li><span class="data-key">Social Interaction</span>: <span class="data-desc">Rating (0–10) of how much time the person spends interacting with people.</span></li>
  <li><span class="data-key">Diet Quality</span>: <span class="data-desc">Indicates if the person follows a healthy diet (e.g., Poor, Average, Good).</span></li>
  <li><span class="data-key">Work Hours</span>: <span class="data-desc">Number of hours the person works per week.</span></li>
  <li><span class="data-key">Family History</span>: <span class="data-desc">Indicates family history of mental health issues (Yes/No).</span></li>
  <li><span class="data-key">Treatment</span>: <span class="data-desc">Indicates whether the person has sought mental health treatment (Yes/No).</span></li>
</ul>
""", unsafe_allow_html=True)
# st.write("""- **Age**: Represents the age of the individual (in years).
# - **Sleep Hours**: Indicates how many hours of sleep the person gets per day.

# - **Gender**: Represents the gender of the individual (e.g., Male, Female, others).

# - **Physical Activity**: Measures the time (in minutes) the person spends on physical activity daily.

# - **Social Interaction**: Represents the Rating (0-10) the person spends interacting with family or other people.

# - **Diet Quality**: Indicates whether the person follows a healthy diet (e.g., Poor, Average, Good).

# - **Work Hours**: Represents the number of hours the individual works per week.

# - **Family History**: Indicates whether there is a history of mental health issues in the person’s family (Yes/No).

# - **Treatment**: Indicates whether the person needs or has sought treatment for mental health issues (Yes/No).""")
# st.write()