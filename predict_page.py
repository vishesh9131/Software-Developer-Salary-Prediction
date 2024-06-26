# import streamlit as st
# import pickle 
# import numpy as np

# def load_model():
#     with open('saved_steps.pkl','rb') as file:
#         data = pickle.load(file)
#     return data

# data = load_model()

# regressor = data["model"]
# le_country = data["le_country"]
# le_education = data["le_education"]

# def show_predict_page():
#     st.title("Software developer salary prediction.:")
#     st.write("""### We Need Some Info to Predict Salary""")
#     countries=(
#         "United States of America",
#         "Germany","United Kingdom of Great Britain and Northern Ireland",
#         "Canada", 
#         "France",                                                  
#         "Netherlands",
#         "Australia", 
#         "Brazil",
#         "Spain", 
#         "Sweden", 
#         "Italy",   
#         "Poland", 
#         "Switzerland", 
#         "Denmark",
#         "Israel",
#         )
#     education = (
#         "Less than a Bachelor",
#         "Bachelors degree",
#         "Master's Degree",
#         "Post Grad",
#     )
#     country = st.selectbox("Country",countries)
#     education = st.selectbox("education level",education)
#     experience = st.slider("years of experience", 0,50,3)
#     ok = st.button("calculate salary")
#     if ok:
#         X = np.array([[country, education, experience ]])
#         X[:, 0] = le_country.transform(X[:,0])
#         X[:, 1] = le_education.transform(X[:,1])
#         X = X.astype(float)
#         salary = regressor.predict(X)
#         st.subheader(f"The estimated salary is :${salary[0]:.2f}")

import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor_loaded = data["model"]
le_country= data["ohe_country"]
le_education= data["ohe_education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the salary""")

    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)

    expericence = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country, education, expericence ]])
        X_country_encoded = le_country.fit_transform(X[:, 0].reshape(-1, 1))
        X_education_encoded = le_education.fit_transform(X[:, 1].reshape(-1, 1))
        # X_encoded = np.concatenate((X_country_encoded.toarray(), X_education_encoded.toarray(), X[:, 2:]), axis=1)
        
        
        X_country_encoded = X_country_encoded.reshape(-1, 1)
        X_education_encoded = X_education_encoded.reshape(-1, 1)
        X_encoded = np.concatenate((X_country_encoded, X_education_encoded, X[:, 2:]), axis=1)

        


        salary = regressor_loaded.predict(X_encoded)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")