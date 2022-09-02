# read images and convert to mat files
import os

import numpy as np
import scipy.io as sio
from PIL import Image


def img2mat(imgPath, savePath):
    for im in os.listdir(imgPath):
        img = Image.open(imgPath + '/' + im)
        img_L = img.convert('L')
        img_data = np.array(img_L)
        sio.savemat(savePath + '/' + im[0] + '.mat', {'data': img_data})


if __name__ == '__main__':
    IMG_PATH = r'C:\Users\HP\PycharmProjects\SignalProcess\raw'
    SAVE_PATH = r'C:\Users\HP\PycharmProjects\SignalProcess\rawMat'
    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)
    img2mat(IMG_PATH, SAVE_PATH)
