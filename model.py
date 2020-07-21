import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

import pickle

train_data = pd.read_csv('train-data.csv')

train_data = train_data[train_data['Mileage'].notna()]
train_data = train_data[train_data['Engine'].notna()]
train_data = train_data[train_data['Power'].notna()]
train_data = train_data[train_data['Seats'].notna()]

train_data = train_data.reset_index(drop=True)

for i in range(train_data.shape[0]):
    train_data.at[i, 'Company'] = train_data['Name'][i].split()[0]
    train_data.at[i, 'Mileage(km/kg)'] = train_data['Mileage'][i].split()[0]
    train_data.at[i, 'Engine(CC)'] = train_data['Engine'][i].split()[0]
    train_data.at[i, 'Power(bhp)'] = train_data['Power'][i].split()[0]

train_data['Mileage(km/kg)'] = train_data['Mileage(km/kg)'].astype(float)
train_data['Engine(CC)'] = train_data['Engine(CC)'].astype(float)

position = []
for i in range(train_data.shape[0]):
    if train_data['Power(bhp)'][i] == 'null':
        position.append(i)

train_data = train_data.drop(train_data.index[position])
train_data = train_data.reset_index(drop=True)

train_data['Power(bhp)'] = train_data['Power(bhp)'].astype(float)

train_data.drop(["Name"], axis=1, inplace=True)
train_data.drop(["Mileage"], axis=1, inplace=True)
train_data.drop(["Engine"], axis=1, inplace=True)
train_data.drop(["Power"], axis=1, inplace=True)
train_data.drop(["New_Price"], axis=1, inplace=True)

var = 'Location'
Location = train_data[[var]]
Location = pd.get_dummies(Location)
Location.head()

var = 'Fuel_Type'
Fuel_t = train_data[[var]]
Fuel_t = pd.get_dummies(Fuel_t)
Fuel_t.head()

var = 'Transmission'
Transmission = train_data[[var]]
Transmission = pd.get_dummies(Transmission)
Transmission.head()

train_data.replace({"First": 1, "Second": 2, "Third": 3, "Fourth & Above": 4}, inplace=True)
train_data.head()

final_train = pd.concat([train_data, Location, Fuel_t, Transmission], axis=1)
final_train.head()

final_train.drop(["Location", "Fuel_Type", "Transmission", 'Company'], axis=1, inplace=True)
final_train.head()

X = final_train.loc[:, ['Year', 'Kilometers_Driven', 'Owner_Type', 'Seats', ''
                        'Mileage(km/kg)', 'Engine(CC)', 'Power(bhp)', 'Location_Ahmedabad',
                        'Location_Bangalore', 'Location_Chennai',
                        'Location_Coimbatore', 'Location_Delhi',
                        'Location_Hyderabad', 'Location_Jaipur',
                        'Location_Kochi', 'Location_Kolkata',
                        'Location_Mumbai', 'Location_Pune',
                        'Fuel_Type_CNG', 'Fuel_Type_Diesel', 'Fuel_Type_LPG',
                        'Fuel_Type_Petrol', 'Transmission_Automatic',
                        'Transmission_Manual']]

y = final_train.loc[:, ['Price']]

linear_reg = LinearRegression()
linear_reg.fit(X, y)

rf_reg = RandomForestRegressor()
rf_reg.fit(X, y)

pickle.dump(linear_reg, open('lin_reg_model.pkl', 'wb'))
pickle.dump(rf_reg, open('rf_reg_model.pkl', 'wb'))