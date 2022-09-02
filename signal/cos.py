import numpy as np
import matplotlib.pyplot as plt
from scipy import io as sio
from sklearn.metrics.pairwise import cosine_similarity


im = sio.loadmat('C:/Users/HP/PycharmProjects/clutter_removal/RPCA_master/Version2/MatFiles/CAS_S500Y_6.mat')
img = im[list(im.keys())[3]]
img_t = img.T
data = cosine_similarity(img_t)

plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(data, cmap='gray')
plt.axis('off')
plt.show()
