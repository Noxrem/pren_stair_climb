#!/bin/sh

BASE_PATH="/Users/stofers/Development/HSLU/PREN/pren_stair_climb/Raspberry_Pi/pictograms/training"
SAMPLE_NAME=$1
IDX=0
INPUT_FORMAT=".jpg"

if [ $# -eq 0 ]; then
    echo "No arguments provided, specify the name of the icon"
    exit 1
fi
echo "move up"
echo "  cd $BASE_PATH"

echo "Collect negative sample data"
echo "  find ${SAMPLE_NAME}_negatives -name '*.jpg' > ${SAMPLE_NAME}_negatives.txt"
echo "\n"

echo "Create positive samples"
echo "  /Users/stofers/openCV/opencv/cmake-build-debug/bin/opencv_createsamples -info ${BASE_PATH}/$SAMPLE_NAME/${SAMPLE_NAME}_${IDX}/${SAMPLE_NAME}_${IDX}.txt -bg $BASE_PATH/${SAMPLE_NAME}_negatives.txt -img $BASE_PATH/sources/$SAMPLE_NAME/${SAMPLE_NAME}_${IDX}${INPUT_FORMAT} -num 1500 -w 48 -h 48 -maxxangle 0.0 -maxzangle 0.0 -maxyangle 0.0 -bgcolor 255"
echo "\n"


echo "Collect all sample-files"
echo "  find $SAMPLE_NAME -name '*.txt' | xargs -I{} cat {} > ${SAMPLE_NAME}_samples.txt"
echo "!!! ajust image path in ${SAMPLE_NAME}_samples.txt before running command above - use BBedit or similar tool !!!"
echo "\n"
#echo "find */hammer_0 -name '*.jpg' >> ${SAMPLE_NAME}_negatives.txt"
#echo "find */paintbucket_0 -name '*.jpg' >> ${SAMPLE_NAME}_negatives.txt"
#echo "find */pencil_0 -name '*.jpg' >> ${SAMPLE_NAME}_negatives.txt"
#echo "find */ruler_0 -name '*.jpg' >> ${SAMPLE_NAME}_negatives.txt"
#echo "find */wrap_0 -name '*.jpg' >> ${SAMPLE_NAME}_negatives.txt"
#echo "find */wrench_0 -name '*.jpg' >> ${SAMPLE_NAME}_negatives.txt"

echo "Create Vec-File"
echo "  /Users/stofers/openCV/opencv/cmake-build-debug/bin/opencv_createsamples -info $BASE_PATH/${SAMPLE_NAME}_samples.txt -bg $BASE_PATH/${SAMPLE_NAME}_negatives.txt -vec $BASE_PATH/${SAMPLE_NAME}.vec -num 1500 -w 48 -h 48 -maxxangle 0.0 -maxzangle 0.0 -maxyangle 0.0 -bgcolor 255"
echo "\n"

echo "Run training"
echo "  nohup /Users/stofers/openCV/opencv/cmake-build-debug/bin/opencv_traincascade -data ${SAMPLE_NAME} -vec ${SAMPLE_NAME}.vec -bg ${SAMPLE_NAME}_negatives.txt -numPos 1350 -numNeg 900 -numStages 7 -w 48 -h 48  -precalcValBufSize 2048 precalcIdxBufSize 2048 -mode ALL -numThreads 8 -minHitRate 0.999 -maxFalseAlarmRate 0.2 > ${SAMPLE_NAME}/log_${SAMPLE_NAME}_training.txt"