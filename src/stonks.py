from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pre processing data
base = pd.read_csv('../Dataset/Training/TSLA.csv')
base = base.dropna()
base_open_value = base.iloc[:, 3:4].values
base_close_value = base.iloc[:, 4:5].values

normalizer = MinMaxScaler(feature_range=(0,1))
base_open_value_normalized = normalizer.fit_transform(base_open_value)
base_close_value_normalized = normalizer.fit_transform(base_close_value)