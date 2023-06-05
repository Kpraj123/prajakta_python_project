import pandas as pd

from matplotlib import pyplot as pyt
from  sklearn import linear_model
import seaborn as se

a=pd.read_excel("Gold.xlsx")
print(a)

se.lineplot(x='Year',y='Price',data=a)
#pyt.show()

reg=linear_model.LinearRegression()
f=reg.fit(a[['Year']],a['Price'])
print(f)
print(reg.predict([[2024]]))
