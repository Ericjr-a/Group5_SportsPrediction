import streamlit as st
import joblib
import pandas as pd

# Loading the model
model = joblib.load("ensemble_model.pkl")
rf_modelm = joblib.load("rf_model.pkl")

# Create an empty slot for the feature values output
output_feature_values = st.empty()

def handle_common_features():
    feature_values["value_eur"] = st.sidebar.number_input("Value (Euros)", min_value=1, max_value=100000000000, value=1000000)
    feature_values["release_clause_eur"] = st.sidebar.number_input("Release Clause (Euros)", min_value=0, max_value=100000000000, value=1000000)
    feature_values["wage_eur"] = st.sidebar.number_input("Wage (Euros)", min_value=1, max_value=100000000000, value=10000000)
    feature_values["international_reputation"] = st.sidebar.number_input("International Reputation (5 is the highest reputation)", min_value=1, max_value=5, value=1)
    feature_values["potential"] = st.sidebar.number_input("Potential", min_value=1, max_value=100, value=50)
    feature_values["movement_reactions"] = st.sidebar.number_input("Reactions", min_value=1, max_value=100, value=50)
    feature_values["mentality_composure"] = st.sidebar.number_input("Composure", min_value=1, max_value=100, value=50)


st.title("FIFA Overall Predictor\nby Eric Afari, Sedem Amediku")
st.sidebar.header("Enter the required information to predict your player's rating")

features =  [
    "value_eur",
    "release_clause_eur",
    "wage_eur",
    "international_reputation",
    "potential",
    "movement_reactions",
    "mentality_composure"
]

print(len(features))

feature_values = {feature: 0 for feature in features}

st.write("Enter the values to get the player's rating....\n\n\n") 
    
handle_common_features()
    
F21 = pd.read_csv("F21.csv")
F21 = F21.drop(columns="overall")
scaler = joblib.load("scaler.pkl")
scaler.fit(F21)

# When the user clicks the "Predict" button
if st.sidebar.button("Predict"):
    # Prepare the input data as a list or numpy array
    input_data = list(feature_values.values())

    scaled_input_data = scaler.transform([input_data])
    
    # Make predictions using the loaded model on scaled input data
    prediction = model.predict(scaled_input_data)[0]
    
    st.write(f"Predicted Output: {round(prediction)} Overall")
    st.write("The Condfidence Percentage of the model is 97.2965%")

