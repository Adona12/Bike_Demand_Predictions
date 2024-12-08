import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


training_data =  pd.read_csv('training_data_fall2024.csv', sep=',')
print(training_data.head())

print(training_data.info())
print(training_data.describe())
print(training_data.isnull().sum())