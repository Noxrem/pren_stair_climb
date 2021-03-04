#!/bin/sh
NUMIMG=$1
CREATE_SAMPLES_PATH="/Users/stofers/openCV/opencv/cmake-build-debug/bin"
BASE_PATH="/Users/stofers/Development/HSLU/PREN1/pren_stair_climb/Raspberry_Pi/pictograms/training"
COUNT=1

for image in `ls -1 ${BASE_PATH}/sources/*.jpg`
do
    echo ${image}
	RETURN_CODE=1

	while [ ${RETURN_CODE} != 0 ]
	do
echo		${CREATE_SAMPLES_PATH}/opencv_createsamples -info ${BASE_PATH}/training/${image}.txt -bg ${BASE_PATH}/negatives_${image}.txt -img ${BASE_PATH}/training/${image}/${image} -num ${NUMIMG} -w 24 -h 24 -maxxangle 0.1 -maxzangle 0.1 -maxyangle 0.1 -bgcolor 100
            RETURN_CODE=$?
	done
    COUNT=$((COUNT+1))
done
