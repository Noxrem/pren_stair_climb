#!/bin/bash

BASE_PATH="/Users/stofers/Development/HSLU/PREN/pren_stair_climb/Raspberry_Pi/pictograms/training"
IMG_NAME=$1
GRAVITY=(East South West North Center)

if [ $# -eq 0 ]; then
    echo "No arguments provided, specify the name of the icon"
    exit 1
fi

mkdir -p $BASE_PATH/${IMG_NAME}_negatives
cp -r $BASE_PATH/negatives/ $BASE_PATH/${IMG_NAME}_negatives

if [ ${IMG_NAME} == "hammer" ]; then
IMG_TO_COMPOSITE=(pencil.png wrench.png ruler.png paintbucket.png wrap.png) # hammer
fi

if [ ${IMG_NAME} == "pencil" ]; then
IMG_TO_COMPOSITE=(wrench.png hammer.png ruler.png paintbucket.png wrap.png) # pencil
fi

if [ ${IMG_NAME} == "ruler" ]; then
IMG_TO_COMPOSITE=(pencil.png hammer.png wrench.png paintbucket.png wrap.png) # ruler
fi

if [ ${IMG_NAME} == "paintbucket" ]; then
IMG_TO_COMPOSITE=(pencil.png hammer.png ruler.png wrench.png wrap.png) # paint-bucket
fi

if [ ${IMG_NAME} == "wrap" ]; then
IMG_TO_COMPOSITE=(pencil.png hammer.png ruler.png paintbucket.png wrench.png) # wrap
fi

if [ ${IMG_NAME} == "wrench" ]; then
IMG_TO_COMPOSITE=(pencil.png hammer.png ruler.png paintbucket.png wrap.png) # wrench
fi

for image in `ls -1 ${BASE_PATH}/negatives`
do
#	for idx in ${!IMG_TO_COMPOSITE[@]}
#	do
#		composite -gravity ${GRAVITY[${idx}]} \( ${IMG_TO_COMPOSITE[${idx}]} -resize 96x96 \) $BASE_PATH/negatives/$image $BASE_PATH/${IMG_NAME}_negatives/${idx}_${image}
#	done
	for idx in ${!IMG_TO_COMPOSITE[@]}
	do
		composite -gravity ${GRAVITY[${idx}]} \( ${IMG_TO_COMPOSITE[${idx}]} -resize 96x96 \) $BASE_PATH/${IMG_NAME}_negatives/$image $BASE_PATH/${IMG_NAME}_negatives/$image
	done
done
