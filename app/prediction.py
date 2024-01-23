import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from PIL import Image
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Load dataset
df = pd.read_csv('pro.csv')

# Convert the 1st column of the dataset into index
sales = df.set_index('Date')['Ship Quantity']

# Load model & scaler
with open('model.pkl', 'rb') as file1:
    model_lr = pickle.load(file1)

with open('scaler.pkl', 'rb') as file2:
    scaler = pickle.load(file2)


# Form for month input

def run():

    st.write('# Bend the Data')
    st.write('###### Enter the number of month and see how much product manufactured by then.')

    with st.form('forecastMonth'):
        month = st.number_input('Months', min_value = 0, value = 4)

        # Submit button
        submitted = st.form_submit_button('Forecast')   
    
    # Function to predict
    def forecasting(month):
        sales_forecast = sales.copy()
        window = 4
        for i in range(month):
            X = sales_forecast[-window:].values.reshape(1, -1)
            X_scaled = scaler.transform(X)

            last_month_str = sales_forecast.index[-1]
            last_month = datetime.strptime(last_month_str, '%y-%m')

            # Increment the month, handling overflow
            new_month = last_month + relativedelta(months=1)  # Increment by 1 month

            # Predict and round the sales value
            predicted_sales = round(model_lr.predict(X_scaled)[0])

            # Add a new row with the predicted sales and the new index
            new_row = pd.Series([predicted_sales], index=[new_month.strftime('%y-%m')], name='sales')
            sales_forecast = sales_forecast._append(new_row)

        # Create a DateTime index using the 'Date' column
        sales_forecast.index = pd.to_datetime(sales_forecast.index, format='%y-%m')

        # Drop the 'Date' column
        sales_forecast = sales_forecast.drop(columns=['Date'])

        return sales_forecast
    
    # If submit button is pressed
    if submitted:
        fig = plt.figure(figsize=(20,5))
        sales_forecast = forecasting(month)
        sales_forecast.index = sales_forecast.index.strftime('%y-%m')  # Convert Periods to strings
        sales_forecast.plot(color='blue', label='forecast', figsize=(20, 5))

        # Convert PeriodIndex to strings
        sales.index = sales.index.astype(str)
        sales.plot(color='red', label='real')

        plt.legend()
        plt.show()
        st.pyplot(fig)


if __name__ == '__main__':
    run()
