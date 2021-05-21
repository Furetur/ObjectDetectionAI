apt-get update
apt-get install -y python3-opencv
wget https://pjreddie.com/media/files/yolov3.weights
mv yolov3.weights ${BUILD_DIR}/modelconfig/yolov3.weights
