import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a= np.array([1,2,3,4,5])
b= np.array([6,7,8,9,10])
c= np.array([11,12,13,14,15])   

df= pd.DataFrame({'a':a, 'b':b, 'c':c})
print(df)

D= 2*df
print(D)

import math
print(D*math.pi)