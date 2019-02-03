from videoTest import CameraVideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True,
                help="path to input video file")
args = vars(ap.parse_args())

print("[INFO] starting video file thread...")
cvs = CameraVideoStream(args["video"]).start()
time.sleep(1.0)

fps = FPS().start()

while cvs.more():
    frame = cvs.read()
    frame = imutils.resize(frame, width=450)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = np.dstack([frame, frame, frame])

    cv2.putText(frame, "Queue Size: {}".format(cvs.Q.qsize()),
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Frame", frame)
    cv2.waitKey(1)
    fps.update()

fps.stop()
cv2.destroyAllWindows()
cvs.stop()