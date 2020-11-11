#!/bin/sh

ITERATIONS=10
IDX=1
IMG_IN_PATH="/Users/stofers/Development/HSLU/PREN1/tests/haar-training/positives/Hammer.jpg"
IMG_OUT_PATH="/Users/stofers/Development/HSLU/PREN1/tests/haar-training/positives/new"

while [ $IDX -le $ITERATIONS ]
do
	RANDOM_BRIGHT=`jot -r 1 -100 100`
	RANDOM_CONTRAST=`jot -r 1 -100 100`
	convert -brightness-contrast $RANDOM_BRIGHTx$RANDOM_CONTRAST $IMG_IN_PATH ${IMG_OUT_PATH}/Hammer_${IDX}.jpg
	IDX=$((IDX+1))
done
