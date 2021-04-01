#!/bin/sh

ITERATIONS=4
IDX=1
BASE_PATH="/Users/stofers/Development/HSLU/PREN/pren_stair_climb/Raspberry_Pi/pictograms/training/sources"
IMG_NAME=$1
OUTPUT_FORMAT=".jpg"
INPUT_FORMAT=".jpg"

if [ $# -eq 0 ]; then
    echo "No arguments provided, specify the name of the icon"
    exit 1
fi

convert $BASE_PATH/${IMG_NAME}${INPUT_FORMAT} -fuzz 20% -transparent white $BASE_PATH/$IMG_NAME.png
mkdir -p $BASE_PATH/$IMG_NAME
convert $BASE_PATH/${IMG_NAME}${INPUT_FORMAT} $BASE_PATH/$IMG_NAME/${IMG_NAME}_0${OUTPUT_FORMAT}
while [ $IDX -le $ITERATIONS ]
do
	RANDOM_BRIGHT=`jot -r 1 -10 60`
	convert -brightness-contrast $RANDOM_BRIGHT $BASE_PATH/${IMG_NAME}.png $BASE_PATH/$IMG_NAME/${IMG_NAME}_${IDX}.png
	convert $BASE_PATH/$IMG_NAME/${IMG_NAME}_${IDX}.png -fuzz 50% -fill none -draw "color 0,0 floodfill" -background white -flatten $BASE_PATH/$IMG_NAME/${IMG_NAME}_${IDX}${OUTPUT_FORMAT}
	IDX=$((IDX+1))
done
#rm $BASE_PATH/${IMG_NAME}*.png
rm $BASE_PATH/$IMG_NAME/${IMG_NAME}*.png