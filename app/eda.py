import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import numpy as np

st.set_page_config(
    #bikin judul pagenya
    page_title= 'Hello',
    #agar gaada padding
    layout= 'wide',
    #expand page
    initial_sidebar_state = 'expanded'
)

def run():

    #Membuat title
    st.title('Data Bender')

    #membuat sub-header
    st.subheader('Sales Volume Forecasting')

    #menambahkan gambar
    image= Image.open('image.jpg')
    st.image(image, caption= 'Inventory Volume Capacity')

    #menambhkan deskripsi
    st.write('Page ini dibuat oleh Aumedi, David dan Rahma')

    #membuat garis lurus
    st.markdown('---')

    #load dataframe
    df = pd.read_csv('File1.csv')
    st.dataframe(df)
    selected_sales = df

    #membuat pie plot
    st.title('Top 5 Categories Sales')
    top_categories = selected_sales.groupby(['Category']).sum()['Ship_Qty'].nlargest(5)
    fig, ax = plt.subplots()
    top_categories.plot(kind='pie', autopct='%1.0f%%', legend=False, fontsize=8, ax=ax)
    plt.title('Top 5 Categories')
    st.pyplot(fig)
    st.write("""Dominant category: The largest slice of the pie chart belongs to the category labeled "PVC Chair Mat," accounting for 40% of sales.
             
    Other categories: The remaining four slices represent the following categories and their sales percentages:
        Desk Pad: 22%
        Anti-Fatigue Mat: 11%
        Recycled Chair Mat: 14%
        Polycarbonate Chair Mat: 14%""")

    # Group by Year and aggregate sum of 'Current Cost' and 'Profit'
    monthly_data = selected_sales.groupby(['Year']).agg({'Current Cost': 'sum', 'Profit': 'sum'}).reset_index()
    st.title('Revenue Breakdown by Year')
    st.bar_chart(monthly_data.set_index('Year'))
    st.write("""The graph shows that the business made a profit steadily increasing over the past three years in 2018, 2019 and 2020. The most profitable years in 2022.""")

    grouped_sales = selected_sales.groupby(['Month', 'Category']).sum()['Profit'].unstack()
    st.title('Total Profit per Month Grouped by Category')
    st.line_chart(grouped_sales, use_container_width=True)
    st.write("""The graph shows the total profit per month for a company, grouped by category. The data appears to be for the year 2018-2022.
Here are some insights based on the graph:
* Overall, the company's profitability seems to be increasing. The total profit per month is trending upwards throughout the year. This suggests that the company's strategies are working and that it is on track to meet its financial goals.
* PVC chair mats are the most profitable product category. They generate significantly more profit than any other category. This suggests that the company should focus on marketing and promoting anti-fatigue mats even more.
* Desk pads, entrance mats, and Anti-fatigue mats  are also relatively profitable. The company may want to consider investing in these product categories as well.
* The least profitable product categories are polycarbonate chair mats, porcelain whiteboards, recycled chair mats, steel whiteboards, tempered glass chair mats, and tempered glass whiteboards. The company may want to consider discontinuing these product categories or finding ways to make them more profitable.
""")

    pivot_table_yearly = pd.pivot_table(selected_sales, values='Profit', index='Category', columns='Year', aggfunc='sum', fill_value=0)
    st.title('Total Profit per Year (USD)')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(pivot_table_yearly, cmap='YlGnBu', annot=True, fmt=".2f", cbar_kws={'label': 'Total Profit'})
    st.pyplot(fig)
    st.write("""*Overall profit has increases steadily over the past five years. This is a positive trend and business is doing well.

*PVC Chair Mat appears to be the most profitable product category. In 2020, it generated a total profit of $364112, which is significantly higher than any other category.

* Some product categories, such as Porcelain Whiteborad and Tempered Glass Chair Mat, have seen a decline in profitability in recent years. This could be due to a number of factors, such as increased competition, changes in customer preferences, or rising costs.

*The largest decrease in profit from 2021 to 2022 was fro Anti-Fatigue mat, with decrease of $14.000.""")

    pivot_table_yearly_units = pd.pivot_table(selected_sales, values='Ship_Qty', index='Category', columns='Year', aggfunc='sum', fill_value=0)
    st.title('Total Sales Volume')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(pivot_table_yearly_units, cmap='YlGnBu', annot=True, fmt=".2f", cbar_kws={'label': 'Total Sales Volume'})
    ax.set_title('Total Sales Volume')
    ax.set_xlabel('Year')
    ax.set_ylabel('Category')
    st.pyplot(fig)
    st.write("""* Desk Pad: This product seems to have consistently high sales volume compared to others.
* PVC Chair Mat: This product also has relatively high sales volume, but it shows a significant drop in 2022.
* Tempered Glass Chair Mat and Tempered Glass Whiteboard: These products have the lowest sales volume among those listed""")

    grouped_sales_volume = selected_sales.groupby(['Month', 'Category']).sum()['Ship_Qty'].unstack().reset_index()
    melted_df = pd.melt(grouped_sales_volume, id_vars='Month', var_name='Category', value_name='Ship_Qty')  
    st.title('Total Sales Volume per Month and Category')
    fig, ax = plt.subplots(figsize=(12, 6))
    for category, data in melted_df.groupby('Category'):
        ax.fill_between(data['Month'], data['Ship_Qty'], label=category)
    ax.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Sales Volume')
    st.pyplot(fig)
    st.write("""* Overall, sales volume appears to be highest in the months of January,Feburary and March. This could be due to a number of factors, such as seasonality, marketing campaigns, or new product releases.
* There is a significant dip in sales volume in the month of May to July and November to December. This is likely due to the holiday season, when many businesses experience a slowdown in sales.
* The category of Anti-Fatigue Mats appears to have the most consistent sales volume throughout the year. This suggests that there is steady demand for this product category, regardless of the season.
* The category of Steel Whiteboards appears to have the most volatile sales volume. This could be due to the fact that this product is typically purchased by businesses, which may have more variable purchasing patterns than consumers.""")
    
    st.title('Inventory Distribution by Category')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Category', y='On Hand', data=df)
    plt.title('Inventory Distribution by Category')
    plt.xticks(rotation='vertical')
    st.pyplot(fig)
    st.write("""The box plot visualizes the distribution of on-hand quantities based on the availability status of products (e.g., available, unavailable).
Inventory management decisions, such as Enrance mat need to restock priorities or Steel Whiteboard have to identify slow-moving products.""")

    st.title('Unit Price Over Time')
    st.line_chart(df.set_index('Invoice_Date')['Unit_Price'])
    st.write("""The line plot visualizes 
* The unit price has been increasing steadily over time. From 2018 to 2023, the unit price has increased from around 50 to around 250.
* There have been a few significant fluctuations in the unit price over time. For example, the price spiked in 2019 and then again in 2020 and 2022
* There have been some small fluctuations in the price, but the overall trend is upward.
* The largest increase in price was in 2019.""")
    
    

if __name__ == '__main__':
    run()