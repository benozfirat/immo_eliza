import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from catboost import CatBoostRegressor
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from sklearn.metrics import mean_absolute_error
import pickle

#Function to establish the range of the outliers
def remove_outliers(col: pd.Series) -> tuple:
    """
    Establish the range of the outliers in a given column.
    
    Parameters:
    col (pd.Series): The column to calculate outlier boundaries for.

    Returns:
    tuple: A tuple containing the lower and upper boundaries for outliers.
    """
    Q1 = col.quantile(0.15)
    Q3 = col.quantile(0.85)
    IQR = Q3 - Q1
    lower_boundary = Q1 - 1.5 * IQR
    upper_boundary = Q3 + 1.5 * IQR
    return lower_boundary, upper_boundary

df = pd.read_csv("ML/Data/dataset.csv")

#Transform the value of TypeOfProperty to 0 and 1 and limit number of facades to 5
df['TypeOfProperty'] = df['TypeOfProperty'].map({1: 0, 2: 1})
df['NumberOfFacades'] = df['NumberOfFacades'].apply(lambda x: 4 if x >= 4 else x)

# Drop columns that will not be useful and the rows containing missing values in columns Region and Province 
df = df.drop(["Url","ConstructionYear","Country","Furnished","Fireplace","PropertyId","MonthlyCharges","RoomCount","Locality"], axis=1)
df = df.dropna(subset=['Region','Province','District'])

#Drop the useless values in TypeOfSale
df = df.loc[(df['TypeOfSale'] != "annuity_monthly_amount") & 
            (df['TypeOfSale'] != "annuity_without_lump_sum") & 
            (df['TypeOfSale'] != "annuity_lump_sum")]

#Drop the useless values in PEB
df = df.loc[(df['PEB'] != "F_D") & 
            (df['PEB'] != "E_C") & 
            (df['PEB'] != "F_C") & 
            (df['PEB'] != "A_A+")&
            (df['PEB'] != "G_F")&
            (df['PEB'] != "G_C")&
            (df['PEB'] != "B_A")&
            (df['PEB'] != "E_D")&
            (df['PEB'] != "F_E")]

# Complete the value in GardenArea if it's missing by GardenArea = Surface - Living if SurfaceOfPlot > LivingArea  
for i, row in df.iterrows():
    if pd.isna(row['GardenArea']):
        if row['SurfaceOfPlot'] > row['LivingArea']:  
            df.at[i,'GardenArea'] = row['SurfaceOfPlot'] - row['LivingArea']

# Complete the value in Garden and GardenArea depending on the result of GardenArea
for i, row in df.iterrows():
    if pd.isna(row['GardenArea']):
        df.at[i,'Garden'] = 0
        df.at[i,'GardenArea'] = 0
    else:
        df.at[i,'Garden'] = 1

#Remove outliers with the function from above
columns_with_outliers = df[['BathroomCount','BedroomCount','GardenArea','LivingArea','NumberOfFacades','Price','SurfaceOfPlot','ToiletCount',]]
for col in columns_with_outliers:
    lower_boundary, upper_boundary = remove_outliers(df[col])
    df = df[~((df[col] < (lower_boundary)) |(df[col] > (upper_boundary)))]

#Use KNN to replace missing values by the 5 closest neighbours in attributes
imputed_data_knn = ['BathroomCount', 'LivingArea', 'NumberOfFacades', 'ToiletCount', 'SurfaceOfPlot', 'ShowerCount']
imputer = KNNImputer(n_neighbors=5)
df[imputed_data_knn] = imputer.fit_transform(df[imputed_data_knn])

#Fill missing values with 0
df['SwimmingPool'] = df['SwimmingPool'].fillna(0)
df['Terrace'] = df['Terrace'].fillna(0)

# Use OneHotEncoder to create boolean columns of categorical columns
ohe = OneHotEncoder(handle_unknown='ignore', sparse_output=False).set_output(transform="pandas")
ohetransform = ohe.fit_transform(df[['District','FloodingZone','PEB','StateOfBuilding','Kitchen', 'Region','SubtypeOfProperty','Province', 'TypeOfSale']])
with open("encoder.pkl", 'wb') as file:
    pickle.dump(ohe, file)
df = pd.concat([df,ohetransform],axis=1).drop(columns=['District','FloodingZone','PEB','StateOfBuilding','Kitchen', 'Region','SubtypeOfProperty','Province', 'TypeOfSale'])

#Save cleaned dataset
#df.to_csv('clean_dataset.csv', index=False)

