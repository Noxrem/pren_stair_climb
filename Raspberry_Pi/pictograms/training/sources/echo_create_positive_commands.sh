#!/bin/sh

ITERATIONS=4
IDX=0
BASE_PATH="/Users/stofers/Development/HSLU/PREN/pren_stair_climb/Raspberry_Pi/pictograms/training"
IMG_NAME=$1
INPUT_FORMAT=".jpg"

if [ $# -eq 0 ]; then
    echo "No arguments provided, specify the name of the icon"
    exit 1
fi

while [ $IDX -le $ITERATIONS ]
do
	echo /Users/stofers/openCV/opencv/cmake-build-debug/bin/opencv_createsamples -info ${BASE_PATH}/$IMG_NAME/${IMG_NAME}_${IDX}/${IMG_NAME}_${IDX}.txt -bg $BASE_PATH/${IMG_NAME}_negatives.txt -img $BASE_PATH/sources/$IMG_NAME/${IMG_NAME}_${IDX}${INPUT_FORMAT} -num 1500 -w 48 -h 48 -maxxangle 0.0 -maxzangle 0.0 -maxyangle 0.0 -bgcolor 255
	IDX=$((IDX+1))
done
