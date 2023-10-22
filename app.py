import streamlit as st
import joblib
import pandas as pd

# Loading the model
model = joblib.load("ensemble_model.pkl")

# Create an empty slot for the feature values output
output_feature_values = st.empty()

# Define the function to handle goalkeepers
def handle_goalkeepers(feature_values):
    feature_values["gk"] = st.sidebar.number_input(f"Goalkeeper Proficiency", min_value=1, max_value=10, value=4)
    feature_values["goalkeeping_diving"] = st.sidebar.number_input(f"Goalkeeper Diving", min_value=1, max_value=10, value=4)
    feature_values["goalkeeping_handling"] = st.sidebar.number_input(f"Goalkeeper Handling", min_value=1, max_value=10, value=4)
    feature_values["goalkeeping_kicking"] = st.sidebar.number_input(f"Goalkeeper Kicking", min_value=1, max_value=10, value=4)
    feature_values["goalkeeping_positioning"] = st.sidebar.number_input(f"Goalkeeper Positioning", min_value=1, max_value=10, value=4)
    feature_values["goalkeeping_reflexes"] = st.sidebar.number_input(f"Goalkeeper Reflexes", min_value=1, max_value=10, value=4)
    feature_values["goalkeeping_speed"] = st.sidebar.number_input(f"Goalkeeper Speed", min_value=1, max_value=10, value=4)


    
    attacking_proficiency = st.sidebar.number_input(f"Attacking Proficiency", min_value=1, max_value=2, value=1)
    defending_proficiency = st.sidebar.number_input(f"Defending Proficiency", min_value=1, max_value=3, value=1)
    midfield_proficiency = st.sidebar.number_input(f"Midfield Proficiency", min_value=1, max_value=2, value=1)
    
    for position in strike_positions:
        feature_values[position] = attacking_proficiency
    
    for position in midfield_positions:
        feature_values[position] = midfield_proficiency
    
    for position in defense_positions:
        feature_values[position] = defending_proficiency
        
    features_to_ask = [ 
    "pace", "shooting", "passing", 
    "dribbling", "defending","physic",  ]

    # Ask for the values of each feature
    for feature in features_to_ask:
        if position_value != 0:
            value = st.sidebar.number_input(f"{feature.replace('_', ' ').title()}", min_value=1, max_value=100, value=50)
            feature_values[feature] = value   
        else:
            feature_values[feature] = 0 
    handle_common_features()

# Define the function to handle other players
def handle_other_players(feature_values):
    attacking_proficiency = st.sidebar.number_input(f"Attacking Proficiency / 10", min_value=1, max_value=10, value=5)
    defending_proficiency = st.sidebar.number_input(f"Defending Proficiency / 10", min_value=1, max_value=10, value=3)
    midfield_proficiency = st.sidebar.number_input(f"Midfield Proficiency / 10", min_value=1, max_value=10, value=4)
    goalkeeper_proficiency = st.sidebar.number_input(f"Goalkeeper Proficiency / 10", min_value=1, max_value=2, value=1)
    
    
    for position in strike_positions:
        feature_values[position] = attacking_proficiency
    
    for position in midfield_positions:
        feature_values[position] = midfield_proficiency
    
    for position in defense_positions:
        feature_values[position] = defending_proficiency
    feature_values["gk"] = goalkeeper_proficiency
    
    
    features_to_ask = [ 
    "pace", "shooting", "passing", 
    "dribbling", "defending","physic",  ]

    # Ask for the values of each feature
    for feature in features_to_ask:
        if position_value != 0:
            value = st.sidebar.number_input(f"{feature.replace('_', ' ').title()}", min_value=1, max_value=100, value=50)
            feature_values[feature] = value   
        else:
            feature_values[feature] = 0 
    
    handle_common_features()

def handle_common_features():
    feature_values["potential"] = st.sidebar.number_input(f"Potential", min_value=1, max_value=100, value=50)
    feature_values["wage_eur"] = st.sidebar.number_input(f"Salary (Euros)", min_value=1, max_value=100000000000, value=1000000)
    feature_values["value_eur"] = st.sidebar.number_input(f"Player Value (Euros)", min_value=1, max_value=100000000000, value=100000)
    feature_values["release_clause_eur"] = st.sidebar.number_input(f"Release Clause (Euros)", min_value=0, max_value=100000000000, value=100000)
    feature_values["age"] = st.sidebar.number_input(f"Age", min_value=14, max_value=60, value=18)
    feature_values["height_cm"] = st.sidebar.number_input(f"Height (cm)", min_value=30, max_value=230, value=160)
    feature_values["weight_kg"] = st.sidebar.number_input(f"Weight (kg)", min_value=30, max_value=230, value=80)
    feature_values["league_level"] = st.sidebar.number_input(f"League Level", min_value=1, max_value=5, value=3)
    
    # Create a list of years from 2022 to 2027
    years = list(range(2022, 2028))
    # Create a dropdown to select the year
    feature_values["club_contract_valid_until"] = st.sidebar.selectbox("Year Contract Ends", years)
    # Create a dictionary to map the dropdown options for nation_position
    nation_position_options = {"Plays for Nation": 1, "Does Not Play for Nation": 0}
    # Create a dropdown list for nation_position
    value = st.sidebar.selectbox("Nation Position", ["Plays for Nation", "Does Not Play for Nation"])
    # Map the selected option to a numerical value using the nation_position_options dictionary
    feature_values["nation_position"] = nation_position_options.get(value, 0)
    feature_values["weak_foot"] = st.sidebar.number_input("Weak Foot", min_value=1, max_value=5, value=3)
    feature_values["skill_moves"] = st.sidebar.number_input("Skill Moves", min_value=1, max_value=5, value=3)
    feature_values["international_reputation"] = st.sidebar.number_input("International Reputation", min_value=1, max_value=5, value=3)
    feature_values["attacking_crossing"] = st.sidebar.number_input("Attacking Crossing", min_value=0, max_value=100, value=60)
    feature_values["attacking_finishing"] = st.sidebar.number_input("Attacking Finishing", min_value=0, max_value=100, value=60)
    feature_values["attacking_heading_accuracy"] = st.sidebar.number_input("Heading Accuracy", min_value=0, max_value=100, value=60)
    feature_values["attacking_short_passing"] = st.sidebar.number_input("Short Passing", min_value=0, max_value=100, value=60)
    feature_values["attacking_volleys"] = st.sidebar.number_input("Volleys", min_value=0, max_value=100, value=60)
    feature_values["skill_dribbling"] = st.sidebar.number_input("Dribbling", min_value=0, max_value=100, value=60)
    feature_values["skill_curve"] = st.sidebar.number_input("Curve", min_value=0, max_value=100, value=60)
    feature_values["skill_fk_accuracy"] = st.sidebar.number_input("Free Kick Accuracy", min_value=0, max_value=100, value=60)
    feature_values["skill_long_passing"] = st.sidebar.number_input("Long Passing", min_value=0, max_value=100, value=60)
    feature_values["skill_ball_control"] = st.sidebar.number_input("Ball Control", min_value=0, max_value=100, value=60)
    feature_values["movement_acceleration"] = st.sidebar.number_input("Acceleration", min_value=0, max_value=100, value=60)
    feature_values["movement_sprint_speed"] = st.sidebar.number_input("Sprint Speed", min_value=0, max_value=100, value=60)
    feature_values["movement_agility"] = st.sidebar.number_input("Agility", min_value=0, max_value=100, value=60)
    feature_values["movement_reactions"] = st.sidebar.number_input("Reactions", min_value=0, max_value=100, value=60)
    feature_values["movement_balance"] = st.sidebar.number_input("Balance", min_value=0, max_value=100, value=60)
    feature_values["power_shot_power"] = st.sidebar.number_input("Shot Power", min_value=0, max_value=100, value=60)
    feature_values["power_jumping"] = st.sidebar.number_input("Jumping", min_value=0, max_value=100, value=60)
    feature_values["power_stamina"] = st.sidebar.number_input("Stamina", min_value=0, max_value=100, value=60)
    feature_values["power_strength"] = st.sidebar.number_input("Strength", min_value=0, max_value=100, value=60)
    feature_values["power_long_shots"] = st.sidebar.number_input("Long Shots", min_value=0, max_value=100, value=60)
    feature_values["mentality_aggression"] = st.sidebar.number_input("Aggression", min_value=0, max_value=100, value=60)
    feature_values["mentality_interceptions"] = st.sidebar.number_input("Interceptions", min_value=0, max_value=100, value=60)
    feature_values["mentality_positioning"] = st.sidebar.number_input("Positioning", min_value=0, max_value=100, value=60)
    feature_values["mentality_vision"] = st.sidebar.number_input("Vision", min_value=0, max_value=100, value=60)
    feature_values["mentality_penalties"] = st.sidebar.number_input("Penalties", min_value=0, max_value=100, value=60)
    feature_values["mentality_composure"] = st.sidebar.number_input("Composure", min_value=0, max_value=100, value=60)
    feature_values["defending_marking_awareness"] = st.sidebar.number_input("Marking Awareness", min_value=0, max_value=100, value=60)
    feature_values["defending_standing_tackle"] = st.sidebar.number_input("Standing Tackle", min_value=0, max_value=100, value=60)
    feature_values["defending_sliding_tackle"] = st.sidebar.number_input("Sliding Tackle", min_value=0, max_value=100, value=60)


st.title("FIFA Overall Predictor\nby Eric Afari, Sedem Amediku")
st.sidebar.header("Enter the required information to predict your player's rating")

features = [
    "player_positions", "potential", "value_eur", "wage_eur", "age", "height_cm", "weight_kg",
    "league_level", "club_contract_valid_until", "nation_position", "weak_foot", "skill_moves", "international_reputation",
    "release_clause_eur", "pace", "shooting", "passing", "dribbling", "defending", "physic", "attacking_crossing",
    "attacking_finishing", "attacking_heading_accuracy", "attacking_short_passing", "attacking_volleys", "skill_dribbling",
    "skill_curve", "skill_fk_accuracy", "skill_long_passing", "skill_ball_control", "movement_acceleration", "movement_sprint_speed",
    "movement_agility", "movement_reactions", "movement_balance", "power_shot_power", "power_jumping", "power_stamina",
    "power_strength", "power_long_shots", "mentality_aggression", "mentality_interceptions", "mentality_positioning",
    "mentality_vision", "mentality_penalties", "mentality_composure", "defending_marking_awareness", "defending_standing_tackle",
    "defending_sliding_tackle", "goalkeeping_diving", "goalkeeping_handling", "goalkeeping_kicking", "goalkeeping_positioning",
    "goalkeeping_reflexes", "goalkeeping_speed", "ls", "st", "rs", "lw", "lf", "cf", "rf", "rw", "lam", "cam", "ram", "lm", "lcm",
    "cm", "rcm", "rm", "lwb", "ldm", "cdm", "rdm", "rwb", "lb", "lcb", "cb", "rcb", "rb", "gk"
]

print(len(features))

strike_positions = ["ls", "st", "rs", "cf", "lf", "rf", "cam", "lam", "ram", "lm", "rm", "lw", "rw"]
goalkeeper_positions = ["gk"]
defense_positions = ["lb", "lcb", "cb", "rcb", "rb", "rwb", "lwb"]
midfield_positions = ["lcm", "cm", "rcm", "ldm", "cdm", "rdm"]

feature_values = {feature: 0 for feature in features}


# setting player_positions based on input
player_positions = st.sidebar.selectbox("Player Position", ["Attacker", "Midfielder", "Defender", "Goalkeeper"])
position_mapping = {"Attacker": 3, "Midfielder": 2, "Defender": 1, "Goalkeeper": 0}

position_value = position_mapping.get(player_positions, 0)
feature_values["player_positions"] = position_value

# Handle goalkeepers and other players
if position_value == 0:
    handle_goalkeepers(feature_values)
else:
    handle_other_players(feature_values)


st.write("Enter the values to get the player's rating....\n\n\n") 
    
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
    
    st.write(f"Predicted Output: {round(prediction)}")
    st.write("The accuracy of the model is 95%")

