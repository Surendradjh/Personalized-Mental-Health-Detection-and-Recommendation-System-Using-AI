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

st.title("Data Analysis")

a=option = st.selectbox("Choose an option", ["Single Feature analysis", "MultiFeature Analysis"])

if a=="Single Feature analysis":
    st.image(r"Deployment\plots\Count of Treatment.png")
    st.write("The number of individuals needing treatment is higher than those who do not in this dataset.")
    st.image(r"Deployment\plots\Age Distribution.png")
    st.write("""
    - The age distribution is looks like almost following the uniform distribution 

    - The minimum age is 18-20

    - The maximum age is 95-98""")

    st.image(r"Deployment/plots/count based on Gender.png")
    st.write("Half of the participants in this dataset are male, while the other half include females and individuals of other gender identities.")
    st.image(r"Deployment/plots/sleeping Hours.png")
    st.write("Here the Sleeping hours are following the normal distribution ")
    st.image(r"Deployment/plots/Social Interaction.png")
    st.write("People's social Interaction is almost following the uniform distribution")
    st.image(r"Deployment/plots/Physical Activity.png")
    st.write("People's Pysical activity timing's are following the uniform distribution")
else:
    st.subheader("multiple feature's analysis ")
    st.image(r"Deployment/plots/Age vs Treatment.png")
    st.write("Older age groups show a significantly higher count of individuals seeking treatment, while the group not requiring treatment appears steady and much smaller in comparison.")
    st.image(r"Deployment/plots/Data Distributions.png")
    st.write("""
            - ✅ No significant outliers are observed across the features, so there’s no immediate need for outlier handling techniques like trimming or winsorization.
             
            - Sleep Hours shows a narrow distribution, indicating consistency in how much people sleep.

            - Physical Activity has a wide spread, showing high variability. This suggests people have very different levels of physical activity, which might be an important factor to consider in the analysis.""")

    st.image(r"Deployment/plots/Gender-Diet-Treatment.png")
    st.write("""
    - 👨‍⚕️ Males with poor diet quality represent the largest group seeking treatment, highlighting a strong link between poor nutrition and mental health issues.

    - 👩‍⚕️ Females with poor diets also show a high number of treatment seekers, reinforcing the impact of diet across genders.

    - ✅ This trend strongly suggests that diet quality is a key factor influencing mental health, and maintaining a healthy diet may reduce the likelihood of needing mental health treatment.

""")
    st.image(r"Deployment/plots/Family History vs Treatment.png")
    st.write("The plot suggests no strong relationship between family history and treatment, as many individuals without a family history still seek mental health support.")

