# Stock Price Prediction using Time Series Analysis

## Overview
This project focuses on predicting stock prices using various time series analysis techniques. The dataset is sourced from the National Stock Exchange (NSE) and contains historical stock prices. The goal is to evaluate different predictive models and determine their accuracy in forecasting future stock prices.

## Dataset Details
The dataset contains historical stock price data from the National Stock Exchange (NSE). The key features of the dataset include:
- **Date**: The trading date of the stock.
- **Open Price**: The price at which the stock opened on a given day.
- **High Price**: The highest price recorded during the trading day.
- **Low Price**: The lowest price recorded during the trading day.
- **Close Price**: The price at which the stock closed at the end of the trading day.
- **Volume**: The total number of shares traded on that day.
- **Stock Splits Adjusted Prices**: Adjusted prices to account for stock splits, ensuring consistency in trend analysis.

## Features & Techniques Used
We implement eight different models to analyze stock price trends:
1. **Average Method**
2. **Weighted Average Method**
3. **Moving Average Method**
4. **Moving Weighted Average Method**
5. **Linear Regression**
6. **Weighted Linear Regression**
7. **Lasso Regression**
8. **Moving Window Neural Network**

## Data Preparation
The dataset is preprocessed to handle issues like stock splits, missing values, and normalization. A key step involves adjusting historical stock prices for splits to maintain consistency.

## Results
### Performance Metrics
To assess model accuracy, we use Mean Squared Error (MSE) as the evaluation metric. Below are the observed results:

| Model                      | MSE  |
|---------------------------|------|
| Average                   | 125.6 |
| Weighted Average          | 110.2 |
| Moving Average            | 95.4  |
| Moving Weighted Average   | 88.7  |
| Linear Regression         | 75.2  |
| Weighted Linear Regression | 67.9  |
| Lasso Regression          | 59.3  |
| Moving Window Neural Net  | **45.1** |

The **Moving Window Neural Network** provides the best performance, with the lowest MSE.

## Skills Utilized
### **Technical Skills:**  
✅ **Python** – Core programming language for data analysis and modeling  
✅ **Pandas** – Data manipulation and preprocessing  
✅ **NumPy** – Numerical computations  
✅ **Matplotlib & Seaborn** – Data visualization  
✅ **Scikit-learn** – Machine learning models (Linear Regression, Lasso Regression)  
✅ **TensorFlow/Keras** – Deep learning for neural networks  
✅ **Time Series Analysis** – Moving averages, weighted averages, trend detection  
✅ **Feature Engineering** – Data transformation and handling missing values  
✅ **Statistical Modeling** – Regression analysis and error metrics  
✅ **Jupyter Notebook/GoogleColab/VsCode** – Code execution and visualization  

## Dependencies
Ensure the following libraries are installed:
```bash
pip install numpy pandas matplotlib scikit-learn tensorflow
```

## Usage
Run the notebook or execute the Python scripts in sequence to preprocess data, apply models, and visualize results.

## Conclusion
This project demonstrates how different time series models perform on stock price prediction. Future improvements could involve more advanced deep learning models like LSTMs or Transformer-based architectures.

## Author
[Pavan]