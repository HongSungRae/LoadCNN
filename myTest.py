import pandas as pd
import numpy as np

from dataProcess import *

df = loadData("df_timeSeries.csv")


print('===day 298===')
print(observe(df,1002,298))

'''
print('===day 451===')
observe(df,1002,451)
'''

print('===day 452===')
print(observe(df,1002,452))

'''
print('===day 453===')
observe(df,1002,453)
'''

print('===day 669===')
print(observe(df,1002,669))

print(findNAN(df))


#print(8064/64)