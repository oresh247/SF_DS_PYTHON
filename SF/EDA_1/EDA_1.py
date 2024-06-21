import pandas as pd
from ydata_profiling import ProfileReport
import sweetviz as sv
import dtale


df = pd.read_csv('C:/Users/aoreshkin.IT-ONE/VSProject/SF_DS_PYTHON-1/SF/EDA_1/data/wine.csv', sep=',') 
d = dtale.show(df)
print(d)