from flask import Flask, request, jsonify, render_template
import pandas as pd
from prophet import Prophet
import joblib

app = Flask(__name__)

# Load the pre-trained Prophet model
model = joblib.load("prophet_model.joblib")

# Load the historical data
df = pd.read_csv('NFLX.csv')
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)
df['Date'] = pd.to_datetime(df['Date'])

# Fit the model with historical data
m = Prophet()
m.add_regressor('Volume')
m.add_regressor('Open')
m.add_regressor('High')
m.add_regressor('Low')

train = df[['Date', 'Close', 'Volume', 'Open', 'High', 'Low']]
train.columns = ['ds', 'y', 'Volume', 'Open', 'High', 'Low']
m.fit(train)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Prepare data for prediction
    future = pd.DataFrame({'ds': [data['date']]})
    future['Volume'] = data['Volume']
    future['Open'] = data['Open']
    future['High'] = data['High']
    future['Low'] = data['Low']

    # Perform prediction using the loaded model
    forecast = m.predict(future)
    prediction = forecast['yhat'].iloc[0]  # Extract the prediction for the specified date

    # Return prediction result
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(debug=True)
