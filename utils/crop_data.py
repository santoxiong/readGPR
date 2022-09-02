import os

import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio

MAT_FILES_DIR = '../dataset/MAT/'
SAVE_DIR = '../dataset/IMG_CROP/'

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)
mat_files = os.listdir(MAT_FILES_DIR)

for filename in mat_files:
    mat_file = f'{MAT_FILES_DIR}{filename}'

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

    imgID = filename.split('_')[0]

    savePath = os.path.join(SAVE_DIR, imgID.split('.')[0])
    if not os.path.exists(savePath):
        os.makedirs(savePath)
    print('make dir:', savePath)

    h, w = out.shape
    print('w:', w, 'h:', h)

    count = 1
    # 向右滑动窗口裁剪数据，1/4区域重叠
    for i in range(0, w, int(h * 0.75)):
        print('i:', i)
        if i + h > w:
            break
        sub_data = out[:, i:i + h]
        print('sub_data.shape:', sub_data.shape)
        plt.imsave(os.path.join(savePath, f'{count}.jpg'), sub_data, cmap='gray')
        print(f'{count}.jpg has been saved')
        count += 1