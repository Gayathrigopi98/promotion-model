# import necessary libraries
import streamlit as st
import pandas as pd
import joblib

st.title("Promotion prediction")

# Add a description to the app
st.markdown("""
    This app predicts if an employee will be promoted based on their attributes such as department, region, education level, gender, etc.
    Please fill in the following details to predict the promotion status.
""")

# Sidebar for better layout organization
st.sidebar.header("Input Employee Information")

# read the dataset to fill list values
df = pd.read_csv('train.csv')

# create input fields 
department = st.sidebar.selectbox("Department", pd.unique(df['department']))
region = st.sidebar.selectbox("Region", pd.unique(df['region']))
education = st.sidebar.selectbox("Education Level", pd.unique(df['education']))
gender = st.sidebar.selectbox("Gender", pd.unique(df['gender']))
recruitment_channel = st.sidebar.selectbox("Recruitment Channel", pd.unique(df['recruitment_channel']))
no_of_trainings = st.sidebar.number_input("Number of Trainings", min_value=0, max_value=10, step=1)
age = st.sidebar.number_input("Age", min_value=18, max_value=100, step=1)
previous_year_rating = st.sidebar.number_input("Previous Year Rating", min_value=0.0, max_value=5.0, step=0.1)
length_of_service = st.sidebar.number_input("Length of Service (in years)", min_value=0, max_value=40, step=1)
KPIs_met = st.sidebar.selectbox("KPIs Met", pd.unique(df['KPIs_met >80%']))
awards_won = st.sidebar.selectbox("Awards Won", pd.unique(df['awards_won?']))
avg_training_score = st.sidebar.number_input("Average Training Score", min_value=0, max_value=100, step=1)


# convert the input values to dict
inputs = {
    "department": department,
    "region": region,
    "education": education,
    "gender": gender,
    "recruitment_channel": recruitment_channel,
    "no_of_trainings": no_of_trainings,
    "age": age,
    "previous_year_rating": previous_year_rating,
    "length_of_service": length_of_service,  
    "KPIs_met >80%": KPIs_met,
    "awards_won?": awards_won,
    "avg_training_score": avg_training_score
}

# Button to trigger prediction
if st.sidebar.button("Predict Promotion"):
    try:
        # Load the pre-trained model
        model = joblib.load('promotion_model.pkl')
        
        # Convert input values to a DataFrame (necessary for prediction)
        X_input = pd.DataFrame(inputs, index=[0])

        # Predict the target (promotion status)
        prediction = model.predict(X_input)

        # Display the result in a formatted manner
        st.write("### Prediction Result")
        if prediction == 1:
            st.success("The employee is likely to be promoted.")
        else:
            st.error("The employee is unlikely to be promoted.")
    
    except Exception as e:
        st.error(f"Error in prediction: {e}")
