# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt

# %%
img = cv2.imread('einstein3.jpg', cv2.IMREAD_GRAYSCALE)
print('Shape:', img.shape)

# %%
# SVD on image
u, singular_values, vt = np.linalg.svd(img)
min_component = min(img.shape[0], img.shape[1])
sig = np.zeros((u.shape[0], vt.shape[0]), dtype=float)
sig[:min_component, :min_component] = np.diag(singular_values)

#print(np.allclose(img, np.dot(u, np.dot(sig, vt))))
n_components = int(img.shape[1]*0.3)          # Since, we need to use 30% eigenvalues
print('Shape of U={}, sigma={} and V_T={}'.format(u[:, :n_components].shape, sig[:n_components, :n_components].shape, vt[:n_components, :].shape))
svd_reconstructed_img = u[:, :n_components] @ sig[:n_components, :n_components] @ vt[:n_components, :]

# %%
# Try using PCA
from sklearn.decomposition import PCA

pca_obj = PCA(n_components=int(img.shape[1]*0.3))
img_reduced = pca_obj.fit_transform(img)
pca_reconstructed_img = pca_obj.inverse_transform(img_reduced)



