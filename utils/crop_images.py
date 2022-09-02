import os

from PIL import Image

"""
高度为512，只向右滑动即可
"""


def getImages(images_folder):
    images_ids = []
    for filename in os.listdir(images_folder):
        images_ids.append(filename)
    return images_ids


def main(imgDir, saveDir):
    imgIDs = getImages(imgDir)
    for imgID in imgIDs:
        # print(imgID)
        savePath = os.path.join(saveDir, imgID.split('.')[0])
        if not os.path.exists(savePath):
            os.makedirs(savePath)
        print('make dir:', savePath)

        img = Image.open(os.path.join(imgDir, imgID))
        w, h = img.size
        # print(w, h)

        count = 1
        # 向右滑动窗口裁剪图片，1/4区域重叠
        for i in range(0, w, int(h * 0.75)):
            box = (i, 0, i + h, h)
            print(box)
            if box[2] <= w:
                region = img.crop(box)
                region.save(os.path.join(savePath, f'{count}.png'))
            count += 1
            print(f'Saved {os.path.join(savePath, f"{count}.png")}')

        print(f'{imgID} has been cropped into {count} images')


if __name__ == '__main__':
    # 原始B-scan图像文件夹
    IMG_DIR = r'C:\Users\HP\PycharmProjects\SignalProcess\dataset\IMG_C'
    # 每张B-scan图像裁剪成多张图像
    SAVE_DIR = r'C:\Users\HP\PycharmProjects\SignalProcess\dataset\CROP_IMG_C'

    main(IMG_DIR, SAVE_DIR)
    print('Done!')
