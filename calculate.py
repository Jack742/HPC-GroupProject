import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

def calculate_cl(tn, ts, N):
    tp=10.9579  
    return (tn-ts-tp/N)/N

dat = pd.read_csv('1280_amdahls.csv')


vals = []
print(dat.head())
for idx, rows in dat.iterrows():
    rows = rows.to_numpy()
    print("for ",rows[0]," threads, CL is: ",calculate_cl(rows[1], rows[3], rows[0]))
    vals.append(calculate_cl(rows[1], rows[3], rows[0]))

plt.plot(vals)
plt.show()