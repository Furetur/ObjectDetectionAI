from typing import List

import cv2 as cv

MODEL_CONFIG = "modelconfig/yolov3.cfg"
MODEL_WEIGHTS = "modelconfig/yolov3.weights"


class Net:
    def __init__(self, image_width, image_height):
        self.net = cv.dnn.readNetFromDarknet(MODEL_CONFIG, MODEL_WEIGHTS)
        self.net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
        self.net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

        self.image_width = image_width
        self.image_height = image_height

    def output_layers_names(self) -> List[str]:
        layers_names = self.net.getLayerNames()
        return [layers_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

    def run(self, image):
        blob = cv.dnn.blobFromImage(image, 1 / 255, (self.image_width, self.image_height), [0, 0, 0], 1, crop=False)
        self.net.setInput(blob)
        return self.net.forward(self.output_layers_names())
