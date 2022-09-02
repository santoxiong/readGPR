import os

from PIL import Image

from utils.crop_images import getImages

bscan_folder = 'C:/Users/HP/PycharmProjects/SignalProcess/data/bscan'
crop_folder = 'C:/Users/HP/PycharmProjects/SignalProcess/crop'

images = getImages(bscan_folder)

for img in images:
    imgPath = os.path.join(bscan_folder, img)
    savePath = os.path.join(bscan_folder, img.split('.')[0])
    if not os.path.exists(savePath):
        os.makedirs(savePath)

    while imgPath:
        img = Image.open(imgPath)

        while img:
            w, h = img.size  # 根据情况调整size
            # print(w, h)

            # 50% overlap
            index = 1
            for i in range(0, w, 208):
                for j in range(0, h, 416):

                    while i + 416 < w and j + 416 < h:
                        region = img.crop((i, j, i + 416, j + 416))
                        region.save(os.path.join(savePath, '{:04d}.jpg'.format(index)))
                        print(f'{index}.jpg saved')
                        i += 416
                        j += 416
                        index += 1
