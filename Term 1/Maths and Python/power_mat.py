import numpy as np
l = [[0.8, 0.5],
    [0.2, 0.5]]

l = np.matrix(l)

k = [50,50]
k = np.matrix(k)
k = k.T

print(k)
for i in range(10):
    k = l@k
print(k)

