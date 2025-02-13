# Stock Price Prediction using Time Series Analysis

## Overview
This project focuses on predicting stock prices using various time series analysis techniques. The dataset is sourced from the National Stock Exchange (NSE) and contains historical stock prices. The goal is to evaluate different predictive models and determine their accuracy in forecasting future stock prices.

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

##Data Set : path = kagglehub.dataset_download("atulanandjha/national-stock-exchange-time-series")

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


