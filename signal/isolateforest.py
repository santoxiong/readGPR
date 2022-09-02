import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest


# font setting
plt.rcParams['font.sans-serif'] = ['Times New Roman']

rng = np.random.RandomState(88)

# train data
# data = np.load('gpr001.npy')
img1 = sio.loadmat('MatFiles/gpr012.mat')
da1 = img1[list(img1.keys())[-1]]
data1 = da1.T

img2 = sio.loadmat('MatFiles/gpr032.mat')
da2 = img2[list(img2.keys())[-1]]
data2 = da2.T
# print(data1.shape)
# index = np.linspace(0, 1, data.shape[0])
# # 均值法去直流、背景（全道均值）
# for m in range(data.shape[0]):
#     for n in range(data.shape[1]):
#         data[m, n] = data[m, n] - np.mean(data, axis=0)[n]  # 去直流、背景
#         data[m, n] = index[m] * data[m, n]  # 时变增益

# fit the model
clf = IsolationForest(max_samples=data1.shape[0], max_features=data1.shape[1], random_state=rng)
data_lable = clf.fit_predict(data1)
la1 = data_lable.tolist()
lable1 = [1 if i == -1 else None for i in la1]  # None
# print(len(lable1))

clf = IsolationForest(max_samples=data2.shape[0], max_features=data2.shape[1], random_state=rng)
data_lable = clf.fit_predict(data2)
la2 = data_lable.tolist()
lable2 = [1 if i == -1 else None for i in la2]  # None
# print('3:', len(lable2))

x1 = [i for i in np.arange(1, 2582)]
x2 = [i for i in np.arange(1, 3370)]

# plot the anomaly positions
plt.subplot(2, 2, 1)
plt.imshow(da1, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(da2, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
x = [i for i in np.arange(1, 2582)]
plt.scatter(x, lable1)
plt.yticks([])

plt.subplot(2, 2, 4)
x = [i for i in np.arange(1, 3370)]
plt.scatter(x, lable2)
plt.yticks([])
plt.show()

