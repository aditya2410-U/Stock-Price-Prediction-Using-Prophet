# Netflix Stock Price Prediction

This project is a simple web application for predicting the stock price of Netflix. Users can input various parameters such as date, volume, open price, high price, and low price, and the application will provide a prediction based on those inputs.

## **Features**

- **User-friendly Interface:** The web application provides an intuitive interface for users to input the required parameters.

- **Prediction:** Upon submitting the form, the application predicts the stock price based on the input parameters.

- **Field Details:** As the user focuses on each input field, detailed information about that field is displayed below the form.

- **Backend with ML Model:** The application utilizes a Flask backend to handle form submissions and integrate with a machine learning model. The ML model, Prophet, is used for predicting stock prices based on historical data.

## **Technologies Used**

- **Frontend:** HTML, CSS, JavaScript

- **Backend:** Python (Flask)

- **Machine Learning:** Prophet (Facebook's time series forecasting library)

## **How to Use**

1. **Clone the repository to your local machine.**

2. **Install the necessary dependencies using `pip install -r requirements.txt`.**

3. **Run the Flask server using `python app.py`.**

4. **Open the provided URL in your web browser.**

5. **Input the required parameters in the form fields.**

6. **Click the "Predict" button to see the prediction.**

