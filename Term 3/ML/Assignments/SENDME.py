import itertools

import numpy as np
from sklearn.linear_model import Lasso

x = np.array(
    [
        [0.94, 0.37, 0.76, 0.56, 0.77, 0.51, 0.80],
        [-0.88, -0.33, -0.68, -0.51, -0.75, -0.47, -0.76],
        [1.32, -0.31, 0.78, 0.23, 0.47, 0.10, 0.90],
        [-0.21, 0.79, 0.13, 0.46, 0.27, 0.54, 0.05],
        [0.75, -0.70, 0.28, -0.22, -0.07, -0.34, 0.39],
        [-0.33, -1.30, -0.66, -0.98, -0.86, -1.06, -0.57],
        [1.27, 0.81, 1.14, 0.96, 1.08, 0.92, 1.15],
        [-0.60, 0.84, -0.13, 0.36, 0.35, 0.48, -0.24],
        [0.15, -1.35, -0.35, -0.85, -0.47, -0.98, -0.22],
        [-0.33, 0.86, 0.07, 0.46, 0.37, 0.56, -0.03],
    ]
)

y = np.array([0.66, -0.60, 0.50, 0.29, 0.03, -0.82, 1.04, 0.12, -0.60, 0.26])

# 3(iii)

lasso_reg = Lasso(alpha=10e-8).fit(x, y)
y_hat = lasso_reg.predict(x)
rss = np.sum((y - y_hat) ** 2)
print(rss)

# 4(iv)

# a

rss = []
for i in range(7):
    temp_x = x[:, i].copy()
    temp_x = temp_x.T
    xTx = np.matmul(temp_x.T, temp_x)
    xTx_inv = 1 / xTx
    weight = xTx_inv * np.matmul(temp_x.T, y)
    y_hat = weight * temp_x
    rss.append(np.sum((y - y_hat) ** 2))
rss = np.array(rss)

print(rss.argmin())

x_5 = x[:, 4].copy()
rss = []
for i in range(7):
    if i == 4:
        continue
    temp_x = x[:, i].copy()
    temp_x = np.array([x_5, temp_x])
    temp_x = temp_x.T
    xTx = np.matmul(temp_x.T, temp_x)
    xTx_inv = np.linalg.inv(xTx)
    weights = np.matmul(np.matmul(xTx_inv, temp_x.T), y)
    y_hat = np.matmul(temp_x, weights)
    rss.append(np.sum((y - y_hat) ** 2))
rss = np.array(rss)

print(rss.argmin())

# Ans: Feature 5 and 3


i = 6
features = [0, 1, 2, 3, 4, 5, 6]
while i != 1:
    comb = list(itertools.combinations(features, i))
    rss = []
    for j in comb:
        temp_x = x.copy()
        temp_x = temp_x.T
        temp_x = temp_x[list(j)].T
        xTx = np.matmul(temp_x.T, temp_x)
        xTx_inv = np.linalg.inv(xTx)
        weights = np.matmul(np.matmul(xTx_inv, temp_x.T), y)
        y_hat = np.matmul(temp_x, weights)
        rss_ = np.sum((y - y_hat) ** 2)
        rss.append(rss_)
    rss = np.array(rss)
    features = list(comb[rss.argmin()])
    i -= 1
print(features)

# Ans: Feature 2 and 4
