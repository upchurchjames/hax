import cv2
import matplotlib
import numpy
import pytesseract
import sys
import queue
import threading


class CameraVideoStream:
    def __init__(self, path, queueSize=128):
        self.stream = cv2.VideoCapture(path)
        self.stopped = False
        self.Q = queue(maxsize=queueSize)

    pass

    def start_stream(self):
        t = threading(target=self.update, args=())
        t.daemon = True
        t.start_stream()
        return self
    pass

    def update(self):
        while True:
            if self.stopped:
                return

            if not self.Q.full():
                (grabbed, frame) = self.stream.read()

            if not grabbed:
                self.stop()
                return

        self.Q.put(frame)

    def read(self):
        return self.Q.get()

    def more(self):
        return self.Q.qsize() > 0

    def stop(self):
        self.stopped = True

def start(file_name):
    fo = open(file_name, "a+")
    get_video(0, fo)
    fo.close()
    pass


def get_video(cam_id, file_name):
    cap = cv2.VideoCapture(cam_id)
    config = ' -l eng --oem 1 --psm 3'
    while True:
        okay, frame = cap.read()
        if not okay:
            break
        text = pytesseract.image_to_string(frame, config=config)
        file_name.write(text + '\n')
        cv2.imshow('video', frame)
        cv2.waitKey(1)

    cap.release()
    pass


if __name__ == '__main__':
    start(sys.argv[1])
    cv2.destroyAllWindows()
