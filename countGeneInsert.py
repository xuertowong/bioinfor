import pandas as pd
import numpy as np
tafile = pd.read_csv("C:\\Users\\lenovo\\425ta.csv")
chrfile = pd.read_csv("C:\\Users\\lenovo\\425chr2.csv")

tasite = list(tafile['tasite'])
tanums = list(tafile['num'])
start = list(chrfile['start'])
end = list(chrfile['end'])
c = np.zeros((np.shape(start)))
for j in range(len(start)):
    length = end[j] - start[j]
    length = 0.1*length
    start[j] = start[j] + length
    end[j] = end[j] - length
for i in range(len(tanums)):
    if tanums[i] > 0:
        for j in range(len(start)):
            if tasite[i] > start[j] and tasite[i] < end[j]:
                c[j] = c[j] + tanums[i]
    else:
        continue
                
e = pd.DataFrame(c)
e.to_csv("C:\\Users\\lenovo\\15.csv")
