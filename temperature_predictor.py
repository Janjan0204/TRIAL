import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Load the dataset
data = pd.read_csv('Weather-Prediction-Data-Sheet1.csv')


def predict_temperature(province, city, day1_weather, day2_weather, day3_weather):
    # Filter data for the specific location
    location_data = data[(data['Province'] == province) & (data['City'] == city)]

    # Prepare the training data
    X = location_data[['Day1_Weather', 'Day2_Weather', 'Day3_Weather']]
    y = location_data['Day4_Temperature']  # Ensure this matches the column name in your CSV

    # Encode weather conditions to numerical values
    weather_encoding = {"Sunny": 0, "Rainy": 1, "Windy": 2, "Cloudy": 3, "Stormy": 4}
    X_encoded = X.applymap(lambda w: weather_encoding[w])

    # Train the decision tree regressor
    regressor = DecisionTreeRegressor()
    regressor.fit(X_encoded, y)

    # Predict the temperature for the given input
    input_data = [[weather_encoding[day1_weather], weather_encoding[day2_weather], weather_encoding[day3_weather]]]
    temperature_prediction = regressor.predict(input_data)
    return temperature_prediction[0]
