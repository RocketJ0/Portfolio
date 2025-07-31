# isolates the clouds over Sri Lanka

from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

sri_lanka = plt.imread("Sri Lanka Map.png")

if sri_lanka.shape[2] == 4:
    sri_lanka = sri_lanka[:, :, :3]

X = sri_lanka.reshape(-1,3)
kmeans = KMeans(2)
kmeans.fit(X)
segmented_img = kmeans.cluster_centers_[kmeans.labels_]
segmented_img = segmented_img.reshape(sri_lanka.shape)

plt.imshow(segmented_img)
plt.show()