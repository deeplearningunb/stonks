from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pre processing data
base = pd.read_csv('../Dataset/Training/TSLA.csv')
base = base.dropna()
base_training = base.iloc[:, 1:5].values
base_open_value = base.iloc[:, 3:4].values
base_close_value = base.iloc[:, 4:5].values

normalizer = MinMaxScaler(feature_range=(0,1))
base_training_normalized = normalizer.fit_transform(base_training)
base_open_value_normalized = normalizer.fit_transform(base_open_value)
base_close_value_normalized = normalizer.fit_transform(base_close_value)

# Adding multiple predictors
predictors = []
open_price = []
close_price = []

for i in range(90, 2352):
    predictors.append(base_training_normalized[i-90:i, 0:4])
    open_price.append(base_open_value_normalized[i, 0])
    close_price.append(base_close_value_normalized[i, 0])

predictors = np.array(predictors)
open_price = np.array(open_price)
close_price = np.array(close_price)


    
    