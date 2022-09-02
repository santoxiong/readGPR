# read txt file and return a list of boxes
import os

from PIL import Image


def getBoxes(txt_path):
    with open(txt_path, 'r') as f:
        lines = f.readlines()
    boxes = []
    for line in lines:
        line = line.strip().split()
        # print(line)
        if len(line) == 6:
            boxes.append(line)
    return boxes


def updateLOC(labels_path):
    """
    子图及其boxes信息
    """
    labels_dic = dict()

    for file in os.listdir(labels_path):
        factor = int(file.split('.')[0])
        # print(factor)
        txt_path = os.path.join(LABELS_PATH, file)
        boxes_label = getBoxes(txt_path)
        # print(box_label)
        labels_dic[factor] = boxes_label

    return labels_dic


def getALLBoxes(labels_dic, img_size):
    all_boxes = []
    for key, value in labels_dic.items():
        # 只修改xy，hw不变
        new_value = [[(128 + key * 256 * x) / img_size[0] if i in [1, 2] else x for i, x in list(value)] for _ in
                     range(len(value))]
        all_boxes.append(new_value)
        all_boxes.extend(labels_dic[key])
    return all_boxes


if __name__ == '__main__':
    # img = ''
    # annotator = Annotator(img, line_width=line_thickness, example=str(names))
    # annotator.box_label(xyxy, label, color=colors(c, True))
    #
    # im0 = annotator.result()
    #
    # # Save results (image with detections)
    # cv2.imwrite(save_path, im0)
    LABELS_PATH = 'C:/Users/HP/PycharmProjects/yolo_2.0/runs/032/exp/labels'
    IMG_PATH = os.path.join(LABELS_PATH, '1.jpg')
    ALL_BOXES_PATH = 'C:/Users/HP/PycharmProjects/yolo_2.0/runs/032/exp/all_boxes.txt'

    IMG_SIZE = Image.open(IMG_PATH).size
    labelsDic = updateLOC(LABELS_PATH)

    # write all boxes to txt file
    with open(ALL_BOXES_PATH, 'w') as f:
        for key, value in labelsDic.items():
            print(f'writing {str(key)}')
            for i in value:
                f.write(' '.join(i) + '\n')

    all_boxes = getBoxes(ALL_BOXES_PATH)

