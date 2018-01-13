# import pandas_datareader as pdr
# a = pdr.get_data_yahoo('600110')
# print(a.head())

import pandas as pd
import tushare as ts
import matplotlib.pyplot as plt
# df = ts.get_hist_data('600110')
# print(df.head())

df = pd.read_csv('600110.csv')
print(df.head())
plt.plot(df.index, df.open)
plt.show()
