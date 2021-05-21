FROM alpine:latest as builder

WORKDIR ~/repo

RUN mkdir modelconfig
COPY get_weights.sh get_weights.sh
RUN sh get_weights.sh

FROM python:3

RUN apt-get update && apt-get install -y python3-opencv

WORKDIR ~/repo

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
COPY --from=builder ~/repo/modelconfig/yolov3.weights modelconfig/yolov3.weights

ENTRYPOINT ["python",  "manage.py",  "runserver"]
