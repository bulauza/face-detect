#!/usr/bin/python3
# cording=utf-8

'''
face_detector.py
==================================================
Usage:
    face_detector.py -src [<video_sourse>]

Keys:
    ESC, q      - Exit
--------------------------------------------------
'''
__autor__='TAKAHASHI_Masaharu'
__version__='1.0.0'
__data__='2019/06/15'

import dlib
import cv2
import time
from imutils import face_utils
import argparse

def main(args):
    cap = cv2.VideoCapture(args.video_source)

    font = cv2.FONT_HERSHEY_SIMPLEX
    #predictor_path = "./shape_predictor_68_face_landmarks.dat"

    detector = dlib.get_frontal_face_detector()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("video is finished")
            break

        # face detecte
        start = time.time()
        dets = detector(frame, 1)
        elapsed_time = time.time() - start
        print ("detector processing time:{:.2f} [sec]".format(elapsed_time))

        detect_result = "Did not detect frontal face"
        text = "NG"
        color = (255, 0, 0)
        if not len(dets) == 0:
            detect_result = "Detected frontal face"
            text = "OK"
            color = (0, 0, 255)
        print(detect_result)

        for i, det in enumerate(dets):
            p1, p2 = (det.left(), det.bottom()), (det.right(), det.top())
            cv2.rectangle(frame, p1, p2, (0, 0, 255), 3)

        cv2.putText(frame, text, (50, 50), font, 1, color, 4)
        cv2.imshow('face detector', frame)

        key = cv2.waitKey(1)
        if key == 27 or key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-src',
        '--source',
        dest='video_source',
        default=0,
        help='Device index of the camera.')
    args = parser.parse_args()
    print(__doc__)
    main(args)
