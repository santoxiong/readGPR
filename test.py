from PIL import Image

img1 = Image.open(r'C:\Users\HP\PycharmProjects\SignalProcess\crop\3d\cropped_images\0001.jpg')
img2 = Image.open(r'C:\Users\HP\PycharmProjects\SignalProcess\crop\3d\cropped_images\0002.jpg')
img3 = Image.open(r'C:\Users\HP\PycharmProjects\SignalProcess\crop\3d\cropped_images\0003.jpg')
img4 = Image.open(r'C:\Users\HP\PycharmProjects\SignalProcess\crop\3d\cropped_images\0004.jpg')
img5 = Image.open(r'C:\Users\HP\PycharmProjects\SignalProcess\crop\3d\cropped_images\0005.jpg')
img6 = Image.open(r'C:\Users\HP\PycharmProjects\SignalProcess\crop\3d\cropped_images\0006.jpg')
img7 = Image.open(r'C:\Users\HP\PycharmProjects\SignalProcess\crop\3d\cropped_images\0007.jpg')
img8 = Image.open(r'C:\Users\HP\PycharmProjects\SignalProcess\crop\3d\cropped_images\0008.jpg')
img9 = Image.open(r'C:\Users\HP\PycharmProjects\SignalProcess\crop\3d\cropped_images\0009.jpg')
img10 = Image.open(r'C:\Users\HP\PycharmProjects\SignalProcess\crop\3d\cropped_images\0010.jpg')


combined_image = Image.new("RGB", (img1.size[0] * 5.5, img1.size[1]))
combined_image.paste(img1, (0, 0))
combined_image.paste(img2, (int(img1.size[0]) * 0.5, 0))
combined_image.paste(img3, (int(img1.size[0]) * 1.5, 0))
combined_image.paste(img4, (int(img1.size[0]) * 2.5, 0))
combined_image.paste(img5, (int(img1.size[0]) * 3.5, 0))
combined_image.paste(img6, (int(img1.size[0]) * 4.5, 0))
combined_image.paste(img7, (int(img1.size[0]) * 5.5, 0))
combined_image.paste(img8, (int(img1.size[0]) * 6.5, 0))
combined_image.paste(img9, (int(img1.size[0]) * 7.5, 0))
combined_image.paste(img10, (int(img1.size[0]) * 8.5, 0))

combined_image.save(r'C:\Users\HP\PycharmProjects\SignalProcess\crop\3d\3d_cropped.jpg')