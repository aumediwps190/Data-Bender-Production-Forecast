# Data-Bender-Production-Forecast
This repository contains a project created as a final project to Hacktiv8 FTDS course.

**************************************************************************************

Final Project

Batch : RMT-025

========================================

Project Team : 

1. David Tjoe (Data Analyst)

2. Aumedi Wibisana (Data Engineer and Data Scientist)

3. Wahyuni Rahmawati (Data Scientist)


========================================

<center><img src="https://raw.githubusercontent.com/wahyunirahmawati/data/main/image.jpg" height=500, width=1000></img></centerleft>

Forecasting production volumes is a critical aspect of business planning and operations management. By accurately predicting the demand for our products, we can optimize our production processes, manage inventory levels efficiently, and make informed decisions about resource allocation.

One effective method for forecasting production volumes is by utilizing sales values.

In this project, we focused on improving the inventory planning process of an anonymous company in Q1 2024. This anonymous company acts as a product distributor by purchasing office products from manufacturers, holding them and then reselling them to retailers and end-users.

By analyzing their office products' purchases, sales and product details data, we created a data model that makes predictions of predicted sales quantities
Knowing how much will be sold of each product category in the future can help determine how much of each product category should be ordered or kept in stock at any given time.

Having a tool that assists in determining the ideal inventory levels at any given time is crucial to:

- Meet customer demand and ensure customer satisfaction
- Avoid having too much inventory which can lead to unnecessary storage and handling costs
- Avoid stockouts which can result in sales loss and/or fines from customers
- Maintain high profitability

For predicting future sales volumes, we will comparing three models, SARIMAX, LSTM, and Linear Rgression then we will choose one model with the best evaluation result and deploy it in to web app.


**Target Users of Data Model**

The target users for this model are:

- the anonymous company whose data was analyzed as well as other distributors, manufacturers or retailers that depend on predicting future sales for goods procurement
- all product sales planning, supply chain, and procurement professionals.

**Data Sources**
- The data used for this project comes in the form of CSV files obtained from the anonymous company.
- The original data has been anonymized for the purposes of this project.
- The CSVs contain 5-years worth of data (2018 to 2022) for Purchases, Sales as well as Product Details.

**Conclusion**
In our project, we created a forecasting model to estimate the future sales of a distribution company. This model was based on an analysis of the historical sales (unit sales volume) over for 5 year period (2018 - 2022).

From three models : SARIMA, LSTM, Linear Regression, the best model is Linear Regression with 10% the value of evaluation result using MAPE.

The result of data inference

Prediction of Sales Quantity for Q1 in 2024 :

January 2024  =  2326 products

Feburary 2024 =   2402 products

March =  2426 products

April =  2332 products
