import pandas as pd
import joblib
from prophet import Prophet
import streamlit as st

# Load the saved model
loaded_model = joblib.load('prophet_model.joblib')

# Streamlit app layout
st.title('Netflix Stock Price Prediction')

# Input widgets for user to enter feature values
volume = st.number_input('Volume', value=1000000)
open_value = st.number_input('Open', value=500)
high = st.number_input('High', value=550)
low = st.number_input('Low', value=450)

# Predict button
predict_button = st.button('Predict')

# Perform prediction when the button is clicked
if predict_button:
    # Generate future dates dataframe with user-entered feature values
    future_dates = pd.DataFrame({
        'ds': pd.to_datetime(['2023-07-10']),  # Replace with your desired future dates
        'Volume': [volume],
        'Open': [open_value],
        'High': [high],
        'Low': [low]
    })

    # Generate forecasts using the loaded model and user-entered feature values
    forecast = loaded_model.predict(future_dates)

    # Display the predicted values
    st.subheader('Predicted Close Price')
    st.write(forecast['yhat'].values[0])
