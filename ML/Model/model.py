import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from sklearn.preprocessing import OneHotEncoder
from catboost import CatBoostRegressor
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import pickle


df = pd.read_csv("ML/Data/clean_dataset.csv")

# Split the data and target
y = df['Price']
X = df.drop(['Price'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=29)

#Define the parameters
params = {'n_estimators': 1952, 
          'learning_rate': 0.09958080678882802, 
          'depth': 10, 
          'subsample': 0.9024150233634263, 
          'colsample_bylevel': 0.26048065199333004, 
          'min_data_in_leaf': 24
    }

# Initialize the model
model = CatBoostRegressor(**params,loss_function='MAE',verbose=100)
model.fit(X_train, y_train,verbose=100) 

with open('model.pkl','wb') as file:
    pickle.dump(model,file)

# Print the results
prediction = model.predict(X_test)
mae = mean_absolute_error(y_test, prediction)
print(f'MAE score: {mae}')
rmse = np.sqrt(mean_squared_error(y_test, prediction))
print(f'RMSE score: {rmse}')
r2 = r2_score(y_test, prediction)
print(f'R2 score: {r2}')