import cv2
import numpy as np
import os
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
vcap = cv2.VideoCapture("rtsp://192.168.1.13:8080/h264_ulaw.sdp", cv2.CAP_FFMPEG)
while(1):
    ret, frame = vcap.read()
    if ret == False:
        print("Frame is empty")
        break;
    else:
        frame_resized = cv2.resize(frame, (640, 640))
        print(frame_resized.shape)
        # cv2.imshow('VIDEO', frame)
        # cv2.waitKey(1)
vcap.release()