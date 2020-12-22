#!/bin/sh
NUMIMG=$1
CREATE_SAMPLES_PATH="/Users/stofers/openCV/opencv/cmake-build-debug/bin"
BASE_PATH="/Users/stofers/Development/HSLU/PREN1/tests/haar-training"

for image in `ls -1 ${BASE_PATH}/positives`
do

	RETURN_CODE=1

	while [ ${RETURN_CODE} != 0 ]
	do
		${CREATE_SAMPLES_PATH}/opencv_createsamples -info ${BASE_PATH}/${image}.txt -bg ${BASE_PATH}/negatives.txt -img ${BASE_PATH}/positives/${image} -num ${NUMIMG} -w 48 -h 48 -maxxangle 0.4 -maxzanlge 2.0 -maxyangle 2.0 -bgcolor 255 -bgthresh 8
		RETURN_CODE=$?
	done

done
