import os

import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio

MAT_FILES_DIR = '../dataset/MAT/'
SAVE_DIR = '../dataset/IMG/'

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)
mat_files = os.listdir(MAT_FILES_DIR)

for filename in mat_files:
    mat_file = f'{MAT_FILES_DIR}{filename}'
    save_path = f'{SAVE_DIR}{filename[:-4]}.jpg'

    mat = sio.loadmat(mat_file)
    data = mat['data']
    data = np.array(data)

    # 按列减均值(解震荡）
    data = data - np.mean(data, axis=0)

    # 时变增益
    index = np.linspace(0.55, 1, data.shape[0])[:, np.newaxis]
    data = data * index

    # # MS
    # data = data - np.mean(data, axis=1)[:, np.newaxis]
    # # SVD
    # U, S, V = np.linalg.svd(data, full_matrices=False)
    # # 第一个奇异值归零
    # S[0] = 0
    # data = np.dot(U, np.dot(np.diag(S), V))

    # 选取范围
    out = data[int(0.5 * data.shape[0]):int(0.75 * data.shape[0]), :]
    print('out.shape:', out.shape)
    # 保存图片
    plt.imsave(save_path, out, cmap='gray')
    print(f'{filename} has been saved')

