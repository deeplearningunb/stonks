from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

base = pd.read('anyfile.csv')
base = base.dropna()
base_training = base.iloc[:, 1:2].values]
base_max_valor = base.iloc[:, 2:3].values]