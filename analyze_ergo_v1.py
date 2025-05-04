#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%

df_raw = pd.read_csv('concept2-result-101767274.csv', sep=',')

# %%

plt.figure()
plt.plot(df_raw['Number'], df_raw['Stroke Rate'])
plt.show()

# %%

plt.figure()
plt.scatter(df_raw['Watts'], df_raw['Stroke Rate'], 
            c=df_raw['Number'], cmap='gist_ncar')
plt.show()

# %%
