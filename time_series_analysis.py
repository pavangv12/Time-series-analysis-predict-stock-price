# -*- coding: utf-8 -*-
"""time series analysis.ipynb

This is an attempt to predict Stock prices based on Stock prices of previous days. The stock market refers to the collection of markets and exchanges where regular activities of buying, selling, and issuance of shares of publicly-held companies take place.

This is a time series analysis and we will see simple eight ways to predict the Stock prices. The various models to be used are:

Average

Weighted Average

Moving Average

Moving Weighted Average

Linear Regression

Weighted Linear Regression

Lasso Regression

Moving Window Neural Network
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error as mse
import kagglehub
import os

path = kagglehub.dataset_download("atulanandjha/national-stock-exchange-time-series")

# Find the CSV file within the downloaded directory
for filename in os.listdir(path):
    if filename.endswith(".csv"):
        file_path = os.path.join(path, filename)
        break

data = pd.read_csv(file_path, usecols=['Date', 'Close'], parse_dates=['Date'], index_col='Date')
data.head()

data.info()

data.shape

data.loc['2015-01-07',:]

print("Min:",data.index.min())
print("Max:",data.index.max())

plt.figure(figsize=(17,5))
data.Close.plot()
plt.title("Closing Price",fontsize=20)
plt.show()

"""**Adjustment for split-up**

If we take this whole data, the prediction might not be as expected as there is a split in between!

We have to either drop the data or adjust the values before split. Since the split is 2 for 1, we can normalize the data prior to split by dividing them by 2. (Old shares are half that of today's share).
"""

# The Split
plt.figure(figsize=(17,5))
stock_price = pd.concat([data.Close[:'2015-06-12']/2,data.Close['2015-06-15':]]) # adjustment
plt.plot(stock_price)
plt.title("Closing Price Adjusted",fontsize=20)
plt.show()

"""And now we have an adjusted time series of Infosys stock prices.

Lets now Predict the Stock price based on various methods.

We will predict the values on last 68 days in the series.
We will use Mean squared error as a metrics to calculate the error in our prediction.
We will compare the results of various methods at the end.
"""

#helper function to plot the stock prediction
prev_values = stock_price.iloc[:180] #train
y_test = stock_price.iloc[180:] #test

def plot_pred(pred,title):
    plt.figure(figsize=(17,5))
    plt.plot(prev_values,label='Train')
    plt.plot(y_test,label='Actual')
    plt.plot(pred,label='Predicted')
    plt.ylabel("Stock prices")
    plt.title(title,fontsize=20)
    plt.legend()
    plt.show()

#Average of previous values
y_av = pd.Series(np.repeat(prev_values.mean(),68),index=y_test.index)
mse(y_av,y_test)

np.sqrt(mse(y_av,y_test))

plot_pred(y_av,'Average')

"""2. **Weighted Mean**

We shall give more weightage to the data which are close to the last day in training data, while calculating the mean. The last day in the training set will get a weightage of 1(=180/180) and the first day will get a weightage of 1/180.
"""

weight = np.array(range(0,180))/180
weighted_train_data =np.multiply(prev_values,weight)

# weighted average is the sum of this weighted train data by the sum of the weight

weighted_average = sum(weighted_train_data)/sum(weight)
y_wa = pd.Series(np.repeat(weighted_average,68),index=y_test.index)

print("MSE: " ,mse(y_wa,y_test))
print("RMSE: " ,np.sqrt(mse(y_wa,y_test)))

plot_pred(y_wa,'Weighted Average')

"""For the other methods we will predict the value of stock price on a day based on the values of stock prices of 80 days prior to it. So in our series we will not consider the first eight days (since there previous eighty days is not in the series).
We have to test the last 68 values. This would be based on the last 80 days stock prices of each day in the test data.
Since we have neglected first 80 and last 68 is our test set, the train dataset will be between 80 and 180 (100 days).
"""

y_train = stock_price[80:180]
y_test = stock_price[180:]
print("y train:",y_train.shape,"\ny test:",y_test.shape)

"""There are 100 days in training and 68 days in testing set. We will construct the features, that is the last 80 days stock for each date in the y_train and y_test. This would be our target variable."""

X_train = pd.DataFrame([list(stock_price[i:i+80]) for i in range(100)],
                       columns=range(80,0,-1),index=y_train.index)
X_test = pd.DataFrame([list(stock_price[i:i+80]) for i in range(100,168)],
                       columns=range(80,0,-1),index=y_test.index)

X_train

"""X_train is now a collection of 100 dates as index and a collection of stock prices of previous 80 days as features.

  Similarlily, X_test is now a collection of 68 dates as index and a collection of stock prices of previous 80 days as features.
  
  NOTE: Here 76 working days from '2015-05-04', the stock had a price of 986.725 and 77 working days from '2015-05-05', the stock has the same value. You can see the similarity of values along the diagonal. This is because consecutitive data will be similar to the previous except it drops the last value, shifts and has a new value.
  
  We will use these values for stock price prediction in the other four methods.

3. **Moving Average**

We have to predict the 68 values in data set and for each values we will get the average of previous 80 days.

This will be a simple mean of each column in the y_test.
"""

y_ma = X_test.mean(axis=1)
mse(y_ma,y_test), np.sqrt(mse(y_ma,y_test))

plot_pred(y_ma,"Moving Average")

"""4. **Weighted Moving Average**

We will obtain the stock price on the test date by calculating the weighted mean of past 80 days. The last of the 80 day will have a weightage of 1(=80/80) and the first will have a weightage of 1/80.
"""

weight = np.array(range(1,81))/80
#weighted moving average
y_wma = X_test@weight/sum(weight)
mse(y_wma,y_test),np.sqrt(mse(y_wma,y_test))

plot_pred(y_wma,"Weighted Moving Average")

"""4. **Linear regression**

In this method, we will perform a linear regression on our dataset. The values will be predicted as a linear combination of the previous 80 days values.
"""

from sklearn.linear_model import LinearRegression
lr=LinearRegression()

lr.fit(X_train,y_train) # Training the models
y_lr = lr.predict(X_test) # inference
y_lr = pd.Series(y_lr,index=y_test.index)

mse(y_test,y_lr), np.sqrt(mse(y_test,y_lr))

plot_pred(y_lr,"Linear Regression")

"""6. **Weighted Linear Regression**

We will provide weightage to our input data rather than the features.
"""

weight = np.array(range(1,101))/100
wlr = LinearRegression()

wlr.fit(X_train,y_train,weight)
y_wlr = wlr.predict(X_test)
y_wlr = pd.Series(y_wlr,index=y_test.index)

mse(y_test,y_wlr), np.sqrt(mse(y_test,y_wlr))

plot_pred(y_wlr,"Weighted Linear Regression")

"""7. **Lasso Regression**

Linear Regression with L1 regulations.
"""

from sklearn.linear_model import Lasso
lasso = Lasso()

las = lasso.fit(X_train,y_train)
y_las = las.predict(X_test)
y_las = pd.Series(y_las,index = y_test.index)

mse(y_las,y_test), np.sqrt(mse(y_test,y_wlr))

plot_pred(y_las,"Lasso Regression")

"""8. **Moving window Neural Network**

We construct a simple Feed Forward network taking 80 features as our input.
"""

from keras.models import Sequential
from keras.layers import Dense

#moving average Neural Network
ma_nn = Sequential([Dense(64,input_shape=(80,),activation='relu'),
                    Dense(32,activation='linear'),Dense(1)])

ma_nn.compile(loss='mse',optimizer='rmsprop',metrics=['mae','mse'])

history = ma_nn.fit(X_train, y_train, epochs=250, batch_size=32, validation_split=0.25)

plt.plot(history.history['mse'],label='Training loss')
plt.plot(history.history['val_mse'], label='Validation loss')
plt.title("Mean Squared error")
plt.xlabel("Number of Epochs")
plt.legend()
plt.show()

loss_nn,mae_nn,mse_nn = ma_nn.evaluate(X_test,y_test)
print("\nloss:",loss_nn,"\nmae:",mae_nn,"\nmse:",mse_nn)

y_nn = ma_nn.predict(X_test)
y_nn = pd.Series(y_nn[:,0],index=y_test.index)
mse(y_nn,y_test),np.sqrt(mse(y_nn,y_test))

plot_pred(y_nn,"Moving Average Prediction")