
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


# Load the dataset
data = pd.read_csv('Weather-Prediction-Data-Sheet1.csv')


def predict_weather(province, city, day1_weather, day2_weather, day3_weather):
    # Filter data for the specific location
    location_data = data[(data['Province'] == province) & (data['City'] == city)]

    # Encode weather conditions to numerical values
    weather_encoding = {"Sunny": 0, "Rainy": 1, "Windy": 2, "Cloudy": 3, "Stormy": 4}
    location_data['Day1_Weather'] = location_data['Day1_Weather'].map(weather_encoding)
    location_data['Day2_Weather'] = location_data['Day2_Weather'].map(weather_encoding)
    location_data['Day3_Weather'] = location_data['Day3_Weather'].map(weather_encoding)
    location_data['Day4_Weather'] = location_data['Day4_Weather'].map(weather_encoding)

    # Prepare the training data
    X = location_data[['Day1_Weather', 'Day2_Weather', 'Day3_Weather']]
    y = location_data['Day4_Weather']

    # Train the decision tree classifier
    clf = DecisionTreeClassifier()
    clf.fit(X, y)

    # Predict the weather for the given input
    input_data = [[weather_encoding[day1_weather], weather_encoding[day2_weather], weather_encoding[day3_weather]]]
    prediction = clf.predict(input_data)

    # Reverse encoding for the output
    reverse_weather_encoding = {v: k for k, v in weather_encoding.items()}
    return reverse_weather_encoding[prediction[0]]

