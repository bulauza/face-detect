#!/bin/bash
source ./check.sh

echo $(colored $cyan "Start")
check pip3 install -r requirements.txt

# Download landmarks detect file
#if [ ! -e "./shape_predictor_68_face_landmarks.dat" ]; then
#    check wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
#    check bzip2 -d shape_predictor_68_face_landmarks.dat.bz2
#fi

echo $(colored $cyan "Finished")
