#!/bin/sh

BASE_PATH="/Users/stofers/Development/HSLU/PREN/pren_stair_climb/Raspberry_Pi/pictograms/training"
SAMPLE_NAME=$1

if [ $# -eq 0 ]; then
    echo "No arguments provided, specify the name of the icon"
    exit 1
fi

echo "Collect all sample-files"
echo "cd $BASE_PATH && find $SAMPLE_NAME -name '*.txt' | xargs -I{} cat {} > $SAMPLE_NAME/${SAMPLE_NAME}_samples.txt"

echo "Collect negative sample data"
echo "find . -name '*.jpg' \( ! -path './${SAMPLE_NAME}/*'' \) > ${SAMPLE_NAME}_negatives.txt"

echo "Create Vec-File"
echo /Users/stofers/openCV/opencv/cmake-build-debug/bin/opencv_createsamples -info $BASE_PATH/$SAMPLE_NAME/${SAMPLE_NAME}_samples.txt -bg $BASE_PATH/${SAMPLE_NAME}_negatives.txt -vec $BASE_PATH/$SAMPLE_NAME/${SAMPLE_NAME}.vec -num 15000 -w 48 -h 48

