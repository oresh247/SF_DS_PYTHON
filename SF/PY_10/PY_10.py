import pandas as pd
import numpy as np


# def create_medications(names, counts):
#     medications_series = pd.Series(data=counts, index=names)
#     return medications_series

# def get_percent(medications, name):
#    item_col = medications.loc[name]
#    item_sum = medications.sum()
#    return (item_col / item_sum) * 100


# names=['chlorhexidine', 'cyntomycin', 'afobazol']
# counts=[15, 18, 7]
# medications = create_medications(names, counts)

# print(get_percent(medications, "chlorhexidine")) #37.5


# def create_companyDF(income, expenses, years):
#     company_df = pd.DataFrame({
#         'Income': income,
#         'Expenses': expenses,
#     }, index = years)
#     return company_df


# def get_profit(df, year):
#     if year in df.index:
#         income = df.loc[year, 'Income']
#         expenses = df.loc[year, 'Expenses']
#         return (income - expenses)
#     else:
#         return None


# print(get_profit(year = 2013, df = create_companyDF([612, 516, 329, 158], [136,163,250,361], [2017,2018,2019,2020])))
# data = pd.DataFrame([[0,1], [1, 0], [1, 1]], columns=['А', 'B'])
# print(data.shape)
# melb_data = pd.read_csv('https://raw.githubusercontent.com/esabunor/MLWorkspace/master/melb_data.csv')
melb_data = pd.read_csv(
    'C:/Users/aoreshkin.IT-ONE/VSProject/SF_DS_PYTHON/SF/PY_10/data/melb_data.csv', sep=',')

# melb_data['Car'] = melb_data['Car'].fillna(0)
# melb_data['Bedroom'] = melb_data['Bedroom'].fillna(0)
# melb_data['Bathroom'] = melb_data['Bathroom'].fillna(0)
# melb_data['Propertycount'] = melb_data['Propertycount'].fillna(0)
# melb_data['YearBuilt'] = melb_data['YearBuilt'].fillna(0)

melb_data['Car'] = melb_data['Car'].astype('int64')
melb_data['Bedroom'] = melb_data['Bedroom'].astype('int64')
melb_data['Bathroom'] = melb_data['Bathroom'].astype('int64')
melb_data['Propertycount'] = melb_data['Propertycount'].astype('int64')
melb_data['YearBuilt'] = melb_data['YearBuilt'].astype('int64')
melb_data.info()

BuildingArea_median = melb_data['BuildingArea'].median()
BuildingArea_mean = melb_data['BuildingArea'].mean()
print(int(round((abs(BuildingArea_median - BuildingArea_mean)/BuildingArea_mean)*100, 0)))
