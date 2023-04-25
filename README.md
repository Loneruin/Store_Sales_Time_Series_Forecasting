# Store Sales Time-Series Forecasting

### [Store Sales Data](https://www.kaggle.com/competitions/store-sales-time-series-forecasting)

## Project Goals

The task is to make a sales forecast for numerous product families that are sold at Favorita stores in Ecuador. The data used for training the model contains information such as dates, store and product details, promotion status, and sales figures.
## EDA
!['Store Sale Summary'](output\figures\store_sales_summary.png)

The dataset is about store sales forecasting where contaning 54 stores, having 33 family of products and 3 years of data in Ecuador

### 1. Average Sales Analysis

!['Average Sales Ananlysis'](output\figures\average_sales_analysis.png)

Highest sales are made by grocery and beverage products and store A has the highest sales which is 38%. Moreover, cluster 1 has the highest sales in 16 clusters

### 2. Average Sales Analysis for Year-Month

!['Average Sales for each Year'](output\figures\average_sales_each_year.png)

Highest sales are made in December and then decrecrease in January. Sales are increasing gradually from 2013 - 2017. Note: we don't have data for 2017: 9th - 12th month 

### 3. Average Sales Analysis: Time Series

!['Average Sales Analysis: Time Series'](output\figures\average_sales_analysis_time_series.png)

The chart above shows that sales have been consistently increasing over time, despite fluctuations at various points. The fluctuations appear to occur in a somewhat regular pattern, suggesting the presence of a seasonal trend. To gain a better understanding of this pattern, it would be useful to analyze data from specific years. One notable finding is that the highest sales occur on Sundays, while December has the highest overall sales. However, it should be noted that data is missing for the last four months of 2017.

### 4. Store Analysis

!['Average Sales: Store Types Vs Holiday Type'](output\figures\average_sales_store_holiday.png)

!['Average Sales: Store Types Vs Year(Month)'](output\figures\average_sales_store_year.png)

!['Average Sales: Holiday Types Vs Month'](output\figures\average_sales_holiday_month.png)

The chart indicates that the highest sales were recorded during transfer holidays, particularly in November (pre-Christmas), December (Christmas holiday), and January (New Year holiday). Additionally, there is a significant shopping trend in May.

!['Average Sales: Holiday Type Vs Year(Month)'](output\figures\average_sales_holiday_year.png)

!['Total Sales by Weekdays'](output\figures\Total_Sales_by_Weekday_and_Year.png)

Sunday and Saturday are the days with the highest sales and Thurdasy is the days with the lowest sales.

### 5. Average Sales by Cities

!['Average Sales by Cities'](output\figures\average_sales_by_cities.png)

Quito and Cayambe in Pichincha are the cities with the highest sales.

### 6. Average Oil Price Ananlysis

!['Average Oil Price Vs Average Sales by Year'](output\figures\Average_Sales_and_Oil_Price_by_Year.png)

Ecuador is an oil-dependent country and it's economical health is highly vulnerable to shocks in oil prices. Furthermore, we can see that there is a negative correlation between oil price and store sales which When oil price changes, the sales changes in the `opposite` direction.

### 7. Average Oil Price Analysis

!['Average Oil Price by Month and Weeks'](output\figures\average_oil_price_month_quarter.png)

## Time Series Forecasting

### 1. Decomposition of Time Series

![Decomposition](output\figures\decomposition.png)

Patterns appear when we decompose the series and plot the data. The time-series has seasonality pattern, peaking right before year end. Sales had been trending upward throughout the year.

### 2. Validate Model Using Diagnostic Plot

![Diagnostic Plot](output\figures\diagnostics.png)

Observations from diagnostics:
1. The residual errors fluctuate around a mean of zero and have a uniform variance.
2. The density plot suggest near normal distribution..
3. Most of the points fall in line with the red line. Distribution is not skewed. Normal data distribution is observed.
4. The Correlogram shows no autocorrelation on the residual errors.
5. Model is a good fit to proceed to forecasting.

### 3. Validate Forecast with Actual Sales Data

![Validate Forecast](output\figures\prediction.png)

To understand the accuracy of the forecast, the predicted sales are compared to actual sales data. From the graph above, forecast date is to start on 01-01-2017 to the end of the data. We can see that forecast prediction looks acceptable as it follows the actual data closely.

### 4. Forecasting Store Sales

![Forecasting](output\figures\prediction2.png)

I am utilizing three distinct forecasting methods for time-series analysis, namely one-step ahead forecasting, dynamic forecasting, and truth forecasting. The forecast seems satisfactory since it conforms to the seasonal trend of a sales uptick just prior to the end of the year, similar to previous years. The forecast is also in line with the actual data, which is a good sign.