# from flask import Flask, render_template, request, redirect, url_for
# import pandas as pd
# import numpy as np
# from weather_predictor import predict_weather
# from temperature_predictor import predict_temperature
#
# app = Flask(__name__)
#
# # Load the dataset
# data = pd.read_csv('Weather-Prediction-Data-Sheet1.csv')
#
# # Define the provinces and cities
# locations = {
#     "Cavite": ["Cawit", "Dasmariñas", "Silang", "Tagaytay"],
#     "Laguna": ["Santa Rosa", "San Pablo", "Santa Cruz", "Siniloan"],
#     "Batangas": ["Batangas City", "Lipa", "Tanauan", "Calaca"],
#     "Rizal": ["Antipolo", "Pillilia", "Binangonan"],
#     "Quezon": ["Tiaong", "Lucena", "Gumaca", "Tagkawayan"]
# }
#
# weather_conditions = ["Sunny", "Rainy", "Windy", "Cloudy", "Stormy"]
#
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         province = request.form['province']
#         city = request.form['city']
#         day1_weather = request.form['day1_weather']
#         day2_weather = request.form['day2_weather']
#         day3_weather = request.form['day3_weather']
#
#         return redirect(url_for('result', province=province, city=city,
#                                 day1_weather=day1_weather, day2_weather=day2_weather,
#                                 day3_weather=day3_weather))
#
#     return render_template('index.html', locations=locations, weather_conditions=weather_conditions)
#
#
# @app.route('/result', methods=['GET'])
# def result():
#     province = request.args.get('province')
#     city = request.args.get('city')
#     day1_weather = request.args.get('day1_weather')
#     day2_weather = request.args.get('day2_weather')
#     day3_weather = request.args.get('day3_weather')
#
#     day4_weather = predict_weather(day1_weather, day2_weather, day3_weather)
#     temperature = predict_temperature(province, city, day1_weather, day2_weather, day3_weather)
#
#     return render_template('result.html', province=province, city=city,
#                            day1_weather=day1_weather, day2_weather=day2_weather,
#                            day3_weather=day3_weather, day4_weather=day4_weather,
#                            temperature=temperature)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#


from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np
from weather_predictor import predict_weather
from temperature_predictor import predict_temperature

app = Flask(__name__)

# Load the dataset
data = pd.read_csv('D:\Pycharm\IS\Mga Copies\WeatherApp\Weather-Prediction-Data-Sheet1.csv')

# Define the provinces and cities
locations = {
    "Cavite": ["Kawit", "Dasmarinas", "Silang", "Tagaytay"],
    "Laguna": ["Santa Rosa", "San Pablo", "Santa Cruz", "Siniloan"],
    "Batangas": ["Batangas City", "Lipa", "Tanauan", "Calaca"],
    "Rizal": ["Antipolo", "Binangonan", "Pillilia", "Quezon"],
    "Quezon": ["Tiaong", "Lucena", "Gumaca", "Tagkawayan"]
}

weather_conditions = ["Sunny", "Rainy", "Windy", "Cloudy", "Stormy"]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        province = request.form['province']
        city = request.form['city']
        day1_weather = request.form['day1_weather']
        day2_weather = request.form['day2_weather']
        day3_weather = request.form['day3_weather']

        return redirect(url_for('result', province=province, city=city,
                                day1_weather=day1_weather, day2_weather=day2_weather,
                                day3_weather=day3_weather))

    return render_template('index.html', locations=locations, weather_conditions=weather_conditions)


@app.route('/result', methods=['GET'])
def result():
    province = request.args.get('province')
    city = request.args.get('city')
    day1_weather = request.args.get('day1_weather')
    day2_weather = request.args.get('day2_weather')
    day3_weather = request.args.get('day3_weather')

    day4_weather = predict_weather(province, city, day1_weather, day2_weather, day3_weather)
    temperature = predict_temperature(province, city, day1_weather, day2_weather, day3_weather)

    return render_template('result.html', province=province, city=city,
                           day1_weather=day1_weather, day2_weather=day2_weather,
                           day3_weather=day3_weather, day4_weather=day4_weather,
                           temperature=temperature)
    
    
@app.route('/submit', methods=['POST'])
def submit():
    day1_weather = request.form['day1_weather']
    day2_weather = request.form['day2_weather']
    day3_weather = request.form['day3_weather']
    day4_weather = predict_weather(day1_weather, day2_weather, day3_weather)  # Your prediction logic here

    return render_template('result.html', day1_weather=day1_weather, day2_weather=day2_weather, day3_weather=day3_weather, day4_weather=day4_weather)



if __name__ == '__main__':
    app.run(debug=True)
