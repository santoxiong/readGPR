import os

from PIL import Image


def get_file_paths(folder):
    image_file_paths = []

    for filename in os.listdir(folder):
        files_path = os.path.join(folder, filename)
        image_file_paths.append(files_path)

    return image_file_paths


def connect_images(file_paths, combined_image_path):
    if not os.path.exists(combined_image_path):
        os.makedirs(combined_image_path)

    filename = combined_image_path.split('/')[-1]
    print(filename)
    n = len(file_paths)
    img = Image.open(file_paths[0])
    connect_image = Image.new("RGB", (img.size[0] * (3*n+1)/2, img.size[1]))

    for i in range(n):
        img = Image.open(file_paths[i])
        print(file_paths[i])
        connect_image.paste(img, (img.size[0] * 0.75*n, img.size[1]))
        connect_image.save(os.path.join(combined_image_path, f'{filename}.jpg'))


if __name__ == '__main__':
    # dataset_folder = 'C:/Users/HP/PycharmProjects/SignalProcess/crop'
    # all_files_paths = get_file_paths(dataset_folder)
    #
    # for file_path in all_files_paths:
    #     cropped_images_path = os.path.join(dataset_folder, 'cropped_images')
    #     detected_images_path = os.path.join(dataset_folder, 'detected_images')
    #     # assert (len(cropped_images_path) == len(detected_images_path))
    #
    #     connect_images(detected_images_path, file_path)
    #     print('{} images combined'.format(len(all_files_paths)))
    #     break  # prevent combining all images
    dataset_folder = 'C:/Users/HP/PycharmProjects/SignalProcess/crop/3d'

    cropped_images_path = os.path.join(dataset_folder, 'cropped_images')
    detected_images_folder = os.path.join(dataset_folder, 'detected_images')
    detected_images_paths = get_file_paths(detected_images_folder)

    connect_images(detected_images_paths, dataset_folder)
