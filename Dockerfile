FROM alpine:latest as builder

WORKDIR ~/repo

RUN mkdir modelconfig
COPY get_weights.sh get_weights.sh
RUN sh get_weights.sh

FROM python:3

COPY requirements.txt ~/repo
RUN pip install -r requirements.txt

COPY . ~/repo
COPY --from=builder ~/repo/modelconfig/yolov3.weights ~/repo/modelconfig/yolov3.weights

ENTRYPOINT ["python",  "manage.py",  "runserver"]
