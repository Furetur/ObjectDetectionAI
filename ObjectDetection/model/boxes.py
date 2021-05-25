import cv2 as cv
import numpy as np


class BoxCollector:
    def __init__(self, image, min_confidence, nms_threshold):
        self.height = image.shape[0]
        self.width = image.shape[1]
        self.min_confidence = min_confidence
        self.nms_threshold = nms_threshold

    def collect_boxes(self, outs):
        classIds = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > self.min_confidence:
                    classIds.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append(self.get_box(detection))

        indices = cv.dnn.NMSBoxes(boxes, confidences, self.min_confidence, self.nms_threshold)
        return [(classIds[i[0]], confidences[i[0]], boxes[i[0]]) for i in indices]

    def get_box(self, detection):
        center_x = int(detection[0] * self.width)
        center_y = int(detection[1] * self.height)
        width = int(detection[2] * self.width)
        height = int(detection[3] * self.height)
        left = int(center_x - width / 2)
        top = int(center_y - height / 2)
        return left, top, width, height


class BoxRenderer:
    def __init__(self, image):
        self.image = image

    def draw_box(self, class_name, confidence, box):
        left, top, width, height = box[0], box[1], box[2], box[3]

        cv.rectangle(self.image, (left, top), (left + width, top + height), (255, 178, 50), 3)

        label = f"{class_name}:{round(confidence, 2)}"

        labelSize, baseLine = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        top = max(top, labelSize[1])
        cv.rectangle(
            self.image,
            (left, top - round(1.5 * labelSize[1])),
            (left + round(1.5 * labelSize[0]), top + baseLine),
            (255, 255, 255),
            cv.FILLED,
        )
        cv.putText(self.image, label, (left, top), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 1)
