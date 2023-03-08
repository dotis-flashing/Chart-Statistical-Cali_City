import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


cities = pd.read_csv('./duy/california_cities.csv')
# cities.head()
lat, lon = cities['latd'], cities['longd']
population, area = cities['population_total'], cities['area_total_km2']
label = 'log$_{10}$(population)'
cmap = 'red'
# Plot using pyplot API
plt.scatter(lon, lat,
            np.log10(population),
            cmap)
# Lam cho dep hon
plt.axis('equal')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.colorbar(label)

#%%
