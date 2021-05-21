from typing import List

import cv2 as cv
import numpy as np

from ObjectDetection.model.boxes import BoxRenderer, BoxCollector
from ObjectDetection.model.net import Net

CLASSES_FILE = "modelconfig/coco.names"


class Model:
    net = Net(416, 416)

    def __init__(self):
        with open(CLASSES_FILE, "rt") as f:
            self.classes = f.read().rstrip("\n").split("\n")

    def process(self, img):
        img = np.array(img, copy=True)
        renderer = BoxRenderer(img)
        outs = self.net.run(img)

        boxes = BoxCollector(img, 0.5, 0.4).collect_boxes(outs)
        for (class_id, conf, box) in boxes:
            renderer.draw_box(self.classes[class_id], conf, box)
        return img
