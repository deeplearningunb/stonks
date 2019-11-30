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

normalizer = MinMaxScaler(feature_range=(0,1))
base_training_normalizer = normalizer.fit_transform(base_training)
base_max_valor_normalizer = normalizer.fit_transform(base_max_valor)

predictors = []
real_price = []
for i in range(90, 1242):
    predictors.append(base_training_normalizer[i-90:i, 0])
    real_price.append(base_training_normalizer[i, 0])
predictors, real_price = np.array(predictors), np.array(real_price)
predictors = np.reshape(predictors.sahpe[0], predictors.shape[1], 1)