import pandas as pd



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

