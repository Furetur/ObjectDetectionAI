apt-get update
apt-get install ffmpeg libsm6 libxext6  -y
wget https://pjreddie.com/media/files/yolov3.weights
mv yolov3.weights ${BUILD_DIR}/modelconfig/yolov3.weights
