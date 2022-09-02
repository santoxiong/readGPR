import cv2


# resize image
def resize_image(image, size):
    img = cv2.resize(image, size)
    return img


if __name__ == '__main__':
    IMAGE_PATH = r'C:\Users\HP\PycharmProjects\SignalProcess\data\bscan\3d.jpg'
    image_raw = cv2.imread(IMAGE_PATH)
    image_new = resize_image(image_raw, (10400, 416))
    cv2.imwrite(IMAGE_PATH, image_new)
