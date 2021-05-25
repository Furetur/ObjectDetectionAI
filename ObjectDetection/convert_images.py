import base64
import numpy as np
import cv2 as cv


def decode_cv_image(bytes):
    arr = np.fromstring(bytes, np.uint8)
    return cv.imdecode(arr, cv.IMREAD_COLOR)


def encode_image_uri(img):
    success, encoded_img = cv.imencode(".png", img)
    encoded_base = base64.b64encode(encoded_img).decode()
    return "data:image/png;base64,{}".format(encoded_base)
