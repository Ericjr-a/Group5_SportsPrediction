# -*- coding: utf-8 -*-
"""Group5_SportsPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rpAURPq0rbImgJSwZTHDf9Kcge1KdSdI
"""

import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

p21 = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/players_21.csv')
p22 = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/players_22.csv')
#players_21.head()
p22.head()

p21.tail().iloc[:, :30]

p21.describe()

p21.info()

p21.shape[1]

players = p21

import matplotlib.pyplot as plt

"""Creating scatter plots to visualize relationships between various columns

"""

players.plot(kind="scatter", x="overall", y="potential", alpha=0.4, cmap=plt.get_cmap("jet"), colorbar=True, )

players.plot(kind="scatter", x="overall", y="value_eur", alpha=0.4, cmap=plt.get_cmap("jet"), colorbar=True, )

players.plot(kind="scatter", x="overall", y="wage_eur", alpha=0.4, cmap=plt.get_cmap("jet"), colorbar=True, )

players.plot(kind="scatter", x="overall", y="age", alpha=0.4, cmap=plt.get_cmap("jet"), colorbar=True, )

players.plot(kind="scatter", x="overall", y="height_cm", alpha=0.4, cmap=plt.get_cmap("jet"), colorbar=True, )

players.plot(kind="scatter", x="overall", y="weight_kg", alpha=0.4, cmap=plt.get_cmap("jet"), colorbar=True, )

players.plot(kind="scatter", x="overall", y="skill_moves", alpha=0.4, cmap=plt.get_cmap("jet"), colorbar=True, )

"""Calculating the correlations between columns

"""

correlation = players['overall'].corr(players['wage_eur'])
print("Correlation between column1 and column2:", correlation)

correlation = players['overall'].corr(players['release_clause_eur'])
print("Correlation between column1 and column2:", correlation)

#players2 = p21.drop(columns= ["pace","dribbling", "physic"])

#players2

"""### Players_21 Data Cleaning

Filtering data based on player positions
"""

positions_to_group = ["ST", "CF", "LF", "RF", "RM","LM","CAM","RW","LW"]
mask = p21['player_positions'].apply(lambda x: any(pos in x for pos in positions_to_group))
attackers = p21[mask]

positions_to_remove = ["LB","RB","RWB","LWB","CB"]
condition = attackers['player_positions'].apply(lambda x: any(pos in x for pos in positions_to_remove))
attackers = attackers[~condition]
attackers

positions_to_group = ["CM", "CDM"]
mask = p21['player_positions'].apply(lambda x: any(pos in x for pos in positions_to_group))
midfielders = p21[mask]
midfielders

positions_to_remove = ["ST", "CF", "LF", "RF", "RM", "LM", "CAM","RW","LW"]

condition = midfielders['player_positions'].apply(lambda x: any(pos in x for pos in positions_to_remove))

midfielders = midfielders[~condition]

midfielders

positions_to_group = ["CB", "RB", "LB", "RWB", "LWB"]
mask = p21['player_positions'].apply(lambda x: any(pos in x for pos in positions_to_group))
defenders = p21[mask]
defenders

positions_to_remove = ["CM", "CDM"]

condition = defenders['player_positions'].apply(lambda x: any(pos in x for pos in positions_to_remove))

defenders = defenders[~condition]
defenders

positions_to_group = ["GK"]
mask = p21['player_positions'].apply(lambda x: any(pos in x for pos in positions_to_group))
goalkeepers = p21[mask]
goalkeepers





# Creating a deep copy of the 'goalkeepers' DataFrame to ensure data integrity

oalkeepers = goalkeepers.copy()
# Assign a uniform value of 0 to the 'player_positions' column for data consistency

goalkeepers.loc[:, 'player_positions'] = 0

goalkeepers

defenders = defenders.copy()
defenders.loc[:, 'player_positions'] = 1
defenders

midfielders = midfielders.copy()
midfielders.loc[:, 'player_positions'] = 2
midfielders

attackers = attackers.copy()
attackers.loc[:, 'player_positions'] = 3

attackers

# Calculating the number of missing values in the 'player_positions' column of the 'p21' DataFrame
nan_count = p21['player_positions'].isna().sum()
nan_count

# Concatenating individual position DataFrames into a comprehensive 'c_players' DataFrame and reset the index

c_players = pd.concat([goalkeepers, defenders, midfielders, attackers], ignore_index=True)
c_players

# Removing any duplicate players based on their 'sofifa_id' to ensure data integrity

c_players = c_players.drop_duplicates(subset='sofifa_id')
c_players

# Concatenate 'c_players' and 'p21' DataFrames, reset the index, and remove rows with identical values across all columns

test = pd.concat([c_players, p21], ignore_index=True).drop_duplicates()

# Remove any duplicate players based on the 'sofifa_id' column to ensure data uniqueness

test = test.drop_duplicates(subset='sofifa_id')
test

test = test.tail(99)
test

# Defining a function to map player positions to corresponding numerical values

def set_position_value(position):
    if "CM" in position.split(',')[0] or "CDM" in position.split(',')[0] or "LM" in position.split(',')[0] or "RM" in position.split(',')[0]:
        return 2
    elif "RB" in position.split(',')[0] or "LB" in position.split(',')[0] or "CB" in position.split(',')[0]:
      return 1
    elif "ST" in position.split(',')[0] or "RW" in position.split(',')[0] or "LW" in position.split(',')[0] or "CAM" in position.split(',')[0]:
      return 3
    return position

# Creating a copy of the 'test' DataFrame

test = test.copy()

# Applying the function to the 'player_positions' column to set numerical values

test['player_positions'] = test['player_positions'].apply(set_position_value)
test
test.tail(99)

# Concatenating the 'c_players' and 'test' DataFrames into a single DataFrame 'F21'.
F21 = pd.concat([c_players, test], ignore_index=True).drop_duplicates()
F21

columns_to_drop1 = ['player_url', 'player_face_url', 'club_logo_url','club_flag_url','nation_logo_url','nation_flag_url','dob',
                    'short_name', 'league_name','club_position' ,'player_tags','club_loaned_from' ,'club_joined' , 'nationality_name' , 'preferred_foot', 'work_rate' ,'body_type' , 'real_face', 'player_traits',
                    'club_name', 'club_team_id','club_jersey_number', 'nation_team_id','nationality_id','nation_jersey_number']
F21 = F21.drop(columns=columns_to_drop1)
F21

"""# To Do:
set player positions for test,
feature engineering and clean data for selected features, and
train 5 models

"""

print(p21.isnull().sum())

missing_values = p21.isnull().sum()
print(missing_values)


columns_with_missing_values = missing_values[missing_values > 0]
print(columns_with_missing_values)

non_numeric_columns = F21.select_dtypes(exclude=['int64', 'float64']).columns
print(non_numeric_columns)

# Calculating correlations of all columns with the 'overall' column in the 'F21' DataFrame
# Filtering for columns with correlation greater than 0.1, sort them in descending order
new_df = F21.corr()['overall'].sort_values(ascending = False)[F21.corr()['overall'] > 0.1].index.tolist()
new_df

object_columns = F21.select_dtypes(include=['object'])
object_columns.info()

# a function to process and bin numeric values (in string format) in the DataFrame.
# If the value has a '+' or '-' sign, the adjustment is applied before binning.

def bin_numeric_values(value):
    if isinstance(value, str):
        if '+' in value:
            base_value, adjustment = value.split('+')
            adjusted_value = int(base_value) + int(adjustment)
        elif '-' in value:
            base_value, adjustment = value.split('-')
            adjusted_value = int(base_value) - int(adjustment)
        else:
            adjusted_value = int(value)
        return adjusted_value // 10
    return value

columns_to_process = [
    "ls", "st", "rs", "lw", "lf", "cf", "rf", "rw", "lam", "cam",'ram', 'lm', 'lcm',
       'cm',"ls", "st", "rs", "lw", "rcm", "rm", "lwb", "ldm", "cdm", "rdm",
    "rwb", "lb", "lcb", "cb", "rcb", "rb", "gk"
]

for col in columns_to_process:
    F21[col] = F21[col].apply(bin_numeric_values)

F21

non_numeric_columns = F21.select_dtypes(exclude=['int64', 'float64']).columns
print(non_numeric_columns)



F21['nation_position'] = (~F21['nation_position'].isna()).astype(int)
F21

# Replacing missing values in 'release_clause_eur' column with 0
F21['release_clause_eur'] = F21['release_clause_eur'].fillna(0)

# Replacing missing values in 'goalkeeping_speed' column with 0
F21['goalkeeping_speed'] = F21['goalkeeping_speed'].fillna(0)

# Replacing missing values in 'pace' column with 0
F21['pace'] = F21['pace'].fillna(0)

# Replacing missing values in 'shooting' column with 0
F21['shooting'] = F21['shooting'].fillna(0)

# Replacing missing values in 'passing' column with 0
F21['passing'] = F21['passing'].fillna(0)

# Replacing missing values in 'dribbling' column with 0
F21['dribbling'] = F21['dribbling'].fillna(0)

# Replacing missing values in 'defending' column with 0
F21['defending'] = F21['defending'].fillna(0)

# Replacing missing values in 'physic' column with 0
F21['physic'] = F21['physic'].fillna(0)

# Display the updated 'F21' DataFrame
F21

missing_values = F21.isnull().sum()
print(missing_values)
columns_with_missing_values = missing_values[missing_values > 0]
print(columns_with_missing_values)

"""# Imputing"""

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean')
columns_to_impute = ['value_eur', 'wage_eur', 'league_level', 'physic']
selected_columns = F21[columns_to_impute]
imputer.fit(F21[columns_to_impute])
imputed_Data = imputer.transform(selected_columns)
F21[columns_to_impute] = imputed_Data
F21

missing_values = F21.isnull().sum()
print(missing_values)
columns_with_missing_values = missing_values[missing_values > 0]
print(columns_with_missing_values)

F21['club_contract_valid_until'] = F21['club_contract_valid_until'].fillna(0)
F21['club_contract_valid_until'] = F21['club_contract_valid_until'].astype(int)
F21['club_contract_valid_until']

column_names = F21.columns

column_list = column_names.tolist()

print(column_list)

new_df = F21.corr()['overall'].sort_values(ascending = False)[F21.corr()['overall'] > 0.1].index.tolist()
len(new_df)

columns_to_drop = ['sofifa_id','long_name']
F21 = F21.drop(columns = columns_to_drop)
y=F21['overall']
X=F21.drop('overall',axis=1)

# Save the 'F21' DataFrame to a CSV file without including the index

F21.to_csv("F21csvFile.csv", index=False)

"""### Training"""

from sklearn.preprocessing import StandardScaler
x = StandardScaler().fit_transform(X.copy())

import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, KFold, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, VotingRegressor
import xgboost as xgb
scaler = StandardScaler()

rf = RandomForestRegressor()
xgb_model = xgb.XGBRegressor()
gb = GradientBoostingRegressor()
k = 5

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

rf_param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}

# Initializing GridSearchCV for RandomForestRegressor with specified parameters


rf_grid_search = GridSearchCV(estimator=RandomForestRegressor(),
                              param_grid=rf_param_grid,
                              scoring='neg_mean_squared_error',
                              cv=3,
                              verbose=2,
                              n_jobs=-1)

rf_grid_search.fit(X_train_scaled, y_train)

best_rf_model = rf_grid_search.best_estimator_

#rf_param_grid = {
 #   'n_estimators': [100, 200, 300],
  #  'max_depth': [None, 10, 20],
   # 'min_samples_split': [2, 5, 10],
    #'min_samples_leaf': [1, 2, 4]
#}
#rf_grid_search = GridSearchCV(estimator=RandomForestRegressor(), param_grid=rf_param_grid, cv=k)
#rf_grid_search.fit(X_train_scaled, y_train)
#best_rf_model = rf_grid_search.best_estimator_








xgb_param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [3, 4],
    'learning_rate': [0.1, 0.01],
    'n_jobs': [-1]
}
# Initializing GridSearchCV for XGBRegressor with the specified parameters

xgb_grid_search = GridSearchCV(estimator=xgb.XGBRegressor(),
                               param_grid=xgb_param_grid,
                               scoring='neg_mean_squared_error',
                               cv=3,
                               verbose=2,
                               n_jobs=-1)

# Fiting the model to the scaled training data

xgb_grid_search.fit(X_train_scaled, y_train)

best_xgb_model = xgb_grid_search.best_estimator_

gb_param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [3, 4],
    'learning_rate': [0.1, 0.01]
}

gb_grid_search = GridSearchCV(estimator=GradientBoostingRegressor(),
                              param_grid=gb_param_grid,
                              scoring='neg_mean_squared_error',
                              cv=3,
                              verbose=2,
                              n_jobs=-1)

gb_grid_search.fit(X_train_scaled, y_train)

best_gb_model = gb_grid_search.best_estimator_

# Initializing a VotingRegressor which combines predictions from three models: RandomForest, XGBoost, and GradientBoosting

ensemble = VotingRegressor(estimators=[
    ('rf', best_rf_model),
    ('xgb', best_xgb_model),
    ('gb', best_gb_model)
], weights=[0.33, 0.33, 0.34])


# Training the ensemble model using the scaled training data

ensemble.fit(X_train_scaled, y_train)

# Predicting the target values for the scaled test data using the ensemble model

ensemble_predictions = ensemble.predict(X_test_scaled)
ensemble_predictions

#print('hello')

import pickle
# saving the trained ensemble model to a file named 'ensemble_model.pkl'

with open('ensemble_model.pkl', 'wb') as model_file:
    pickle.dump(ensemble, model_file)

"""cleaning players_22"""

p22.shape[1]

players1 = p22

import matplotlib.pyplot as plt

players1.plot(kind="scatter", x="overall", y="potential", alpha=0.4, cmap=plt.get_cmap("jet"), colorbar=True, )

players1.plot(kind="scatter", x="overall", y="value_eur", alpha=0.4, cmap=plt.get_cmap("jet"), colorbar=True, )

players1.plot(kind="scatter", x="overall", y="wage_eur", alpha=0.4, cmap=plt.get_cmap("jet"), colorbar=True, )

players1.plot(kind="scatter", x="overall", y="age", alpha=0.4, cmap=plt.get_cmap("jet"), colorbar=True, )

players1.plot(kind="scatter", x="overall", y="height_cm", alpha=0.4, cmap=plt.get_cmap("jet"), colorbar=True, )

players1.plot(kind="scatter", x="overall", y="weight_kg", alpha=0.4, cmap=plt.get_cmap("jet"), colorbar=True, )

players1.plot(kind="scatter", x="overall", y="skill_moves", alpha=0.4, cmap=plt.get_cmap("jet"), colorbar=True, )

correlation_22 = players1['overall'].corr(players1['wage_eur'])
print("Correlation between column1 and column2:", correlation_22)

correlation_22 = players1['overall'].corr(players1['release_clause_eur'])
print("Correlation between column1 and column2:", correlation_22)

positions_to_group_22 = ["ST", "CF", "LF", "RF", "RM","LM","CAM","RW","LW"]
mask_22 = p22['player_positions'].apply(lambda x: any(pos in x for pos in positions_to_group_22))
attackers_22 = p22[mask_22]

positions_to_remove_22 = ["LB","RB","RWB","LWB","CB"]
condition_22 = attackers_22['player_positions'].apply(lambda x: any(pos in x for pos in positions_to_remove_22))
attackers_22 = attackers_22[~condition_22]
attackers_22

positions_to_group_22 = ["CM", "CDM"]
mask_22 = p22['player_positions'].apply(lambda x: any(pos in x for pos in positions_to_group_22))
midfielders_22 = p22[mask_22]
midfielders_22

positions_to_remove_22 = ["ST", "CF", "LF", "RF", "RM", "LM", "CAM","RW","LW"]

condition_22 = midfielders_22['player_positions'].apply(lambda x: any(pos in x for pos in positions_to_remove_22))

midfielders_22 = midfielders_22[~condition_22]

midfielders_22

positions_to_group_22 = ["CB", "RB", "LB", "RWB", "LWB"]
mask_22 = p22['player_positions'].apply(lambda x: any(pos in x for pos in positions_to_group_22))
defenders_22 = p22[mask_22]
defenders_22

positions_to_remove_22 = ["CM", "CDM"]

condition_22 = defenders_22['player_positions'].apply(lambda x: any(pos in x for pos in positions_to_remove_22))

defenders_22 = defenders_22[~condition_22]
defenders_22

positions_to_group_22 = ["GK"]
mask_22 = p22['player_positions'].apply(lambda x: any(pos in x for pos in positions_to_group_22))
goalkeepers_22 = p22[mask_22]
goalkeepers_22

goalkeepers_22 = goalkeepers_22.copy()
goalkeepers_22.loc[:, 'player_positions'] = 0
goalkeepers_22

defenders_22 = defenders_22.copy()
defenders_22.loc[:, 'player_positions'] = 1
defenders_22

midfielders_22 = midfielders_22.copy()
midfielders_22.loc[:, 'player_positions'] = 2
midfielders_22

attackers_22 = attackers_22.copy()
attackers_22.loc[:, 'player_positions'] = 3
attackers_22

nan_count_22 = p22['player_positions'].isna().sum()
nan_count_22

c_players_22 = pd.concat([goalkeepers_22, defenders_22, midfielders_22, attackers_22], ignore_index=True)
c_players_22
c_players_22 = c_players_22.drop_duplicates(subset='sofifa_id')
c_players_22

test_22 = pd.concat([c_players_22, p22], ignore_index=True).drop_duplicates()
test_22 = test_22.drop_duplicates(subset='sofifa_id')
test_22

test_22 = test_22.tail(99)
test_22

def set_position_value_22(position_22):
    if "CM" in position_22.split(',')[0] or "CDM" in position_22.split(',')[0] or "LM" in position_22.split(',')[0] or "RM" in position_22.split(',')[0]:
        return 2
    elif "RB" in position_22.split(',')[0] or "LB" in position_22.split(',')[0] or "CB" in position_22.split(',')[0]:
      return 1
    elif "ST" in position_22.split(',')[0] or "RW" in position_22.split(',')[0] or "LW" in position_22.split(',')[0] or "CAM" in position_22.split(',')[0]:
      return 3
    return position_22


test_22 = test_22.copy()
test_22['player_positions'] = test_22['player_positions'].apply(set_position_value_22)
test_22
test_22.tail(99)

F22 = pd.concat([c_players_22, test_22], ignore_index=True).drop_duplicates()
F22

columns_to_drop_22 = ['player_url', 'player_face_url', 'club_logo_url','club_flag_url','nation_logo_url','nation_flag_url','dob',
                    'short_name', 'league_name','club_position' ,'player_tags','club_loaned_from' ,'club_joined' , 'nationality_name' , 'preferred_foot', 'work_rate' ,'body_type' , 'real_face', 'player_traits',
                    'club_name', 'club_team_id','club_jersey_number', 'nation_team_id','nationality_id','nation_jersey_number']
F22 = F22.drop(columns=columns_to_drop_22)
F22

print(p22.isnull().sum())

missing_values_22 = p22.isnull().sum()
print(missing_values_22)


columns_with_missing_values_22 = missing_values_22[missing_values_22 > 0]
print(columns_with_missing_values_22)

non_numeric_columns_22 = F22.select_dtypes(exclude=['int64', 'float64']).columns
print(non_numeric_columns_22)

new_df_22 = F22.corr()['overall'].sort_values(ascending = False)[F22.corr()['overall'] > 0.1].index.tolist()
new_df_22

object_columns_22 = F22.select_dtypes(include=['object'])
object_columns_22.info()

def bin_numeric_values_22(value_22):
    if isinstance(value_22, str):
        if '+' in value_22:
            base_value, adjustment = value_22.split('+')
            adjusted_value = int(base_value) + int(adjustment)
        elif '-' in value_22:
            base_value, adjustment = value_22.split('-')
            adjusted_value = int(base_value) - int(adjustment)
        else:
            adjusted_value = int(value_22)
        return adjusted_value // 10
    return value_22

columns_to_process_22 = [
    "ls", "st", "rs", "lw", "lf", "cf", "rf", "rw", "lam", "cam",'ram', 'lm', 'lcm',
       'cm',"ls", "st", "rs", "lw", "rcm", "rm", "lwb", "ldm", "cdm", "rdm",
    "rwb", "lb", "lcb", "cb", "rcb", "rb", "gk"
]

for col in columns_to_process_22:
    F22[col] = F22[col].apply(bin_numeric_values)

F22

non_numeric_columns_22 = F22.select_dtypes(exclude=['int64', 'float64']).columns
print(non_numeric_columns_22)

# Set values in the 'column_name' column
F22['nation_position'] = (~F22['nation_position'].isna()).astype(int)
F22

F22['release_clause_eur'] = F22['release_clause_eur'].fillna(0)
F22['goalkeeping_speed'] = F22['goalkeeping_speed'].fillna(0)
F22['pace'] = F22['pace'].fillna(0)
F22['shooting'] = F22['shooting'].fillna(0)
F22['passing'] = F22['passing'].fillna(0)
F22['dribbling'] = F22['dribbling'].fillna(0)
F22['defending'] = F22['defending'].fillna(0)
F22['physic'] = F22['physic'].fillna(0)
F22

missing_values_22 = F22.isnull().sum()
print(missing_values_22)
columns_with_missing_values_22 = missing_values_22[missing_values_22 > 0]
print(columns_with_missing_values_22)

from sklearn.impute import SimpleImputer

imputer_22 = SimpleImputer(strategy='mean')
columns_to_impute_22 = ['value_eur', 'wage_eur', 'league_level', 'physic']
selected_columns_22 = F22[columns_to_impute_22]
imputer_22.fit(F22[columns_to_impute_22])
imputed_Data_22 = imputer_22.transform(selected_columns_22)
F22[columns_to_impute_22] = imputed_Data_22
F22

missing_values_22 = F22.isnull().sum()
print(missing_values_22)
columns_with_missing_values_22 = missing_values_22[missing_values_22 > 0]
print(columns_with_missing_values_22)

F22['club_contract_valid_until'] = F22['club_contract_valid_until'].fillna(0)
F22['club_contract_valid_until'] = F22['club_contract_valid_until'].astype(int)
F22['club_contract_valid_until']

column_names_22 = F22.columns

column_list_22 = column_names_22.tolist()

print(column_list_22)

new_df_22 = F22.corr()['overall'].sort_values(ascending = False)[F22.corr()['overall'] > 0.1].index.tolist()
len(new_df_22)
#F22.columns

F22.info()

columns_to_drop_22 = ['sofifa_id','long_name']
F22 = F22.drop(columns = columns_to_drop_22)
y_22= F22['overall']
X_22= F22.drop('overall',axis=1)
#F22.column_names_22

F22.columns

column_names_22 = F22.drop('overall',axis=1).columns
X_22 = F22[column_names_22]
y_22 = F22['overall']
scaler.fit(X_22)
X_22_scaled = scaler.transform(X_22)

rf_predictions = best_rf_model.predict(X_22_scaled)

xgb_predictions = best_xgb_model.predict(X_22_scaled)

gb_predictions = best_gb_model.predict(X_22_scaled)

ensemble_predictions = ensemble.predict(X_22_scaled)

from sklearn.metrics import mean_absolute_error

rf_mae = mean_absolute_error(y_22, rf_predictions)
xgb_mae = mean_absolute_error(y_22, xgb_predictions)
gb_mae = mean_absolute_error(y_22, gb_predictions)
em_mae = mean_absolute_error(y_22, ensemble_predictions)

rf_mae

xgb_mae

gb_mae

em_mae

from scipy.stats import t

mae_scores = [0.5066611491970142, 0.538189384910772,0.5311798584019283,0.5178980693575034]

mean_mae = np.mean(mae_scores)
se = np.std(mae_scores) / np.sqrt(len(mae_scores))

confidence_level = 0.95

dof = len(mae_scores) - 1
t_critical = t.ppf((1 + confidence_level) / 2, dof)

margin_of_error = t_critical * se
confidence_interval = (mean_mae - margin_of_error, mean_mae + margin_of_error)

confidence_percentage = confidence_level * 100

print(f"Mean MAE: {mean_mae}")
print(f"Confidence Level: {confidence_percentage}%")
print(f"Confidence Interval: {confidence_interval}")

import pickle
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

with open("scaler2.pkl", "wb") as file:
    pickle.dump(scaler, file)

F22.to_excel("22_dataset.xlsx", index='True')