#!/bin/sh

BASE_PATH="/Users/stofers/Development/HSLU/PREN/pren_stair_climb/Raspberry_Pi/pictograms/training"
IMG_NAME=$1
IMG_TO_COMPOSITE=(pencil.png hammer.png ruler.png paintbucket.png wrap.png)
GRAVITY=(East South West North Center)


if [ $# -eq 0 ]; then
    echo "No arguments provided, specify the name of the icon"
    exit 1
fi

#echo "find . -name '*.png' -not -name '${IMG_NAME}*'"

#for i in `find . -name '*.png' -not -name '${IMG_NAME}*'`
#do
#
#    echo $i
#    ${IMG_TO_COMPOSITE}+=(${i})
#done
#
for image in `ls -1 ${BASE_PATH}/negatives`
do
#	echo $image
	for idx in ${!IMG_TO_COMPOSITE[@]}
	do
#		echo $idx
#		echo ${GRAVITY[${idx}]}
#		echo ${IMG_TO_COMPOSITE[${idx}]}
		composite -gravity ${GRAVITY[${idx}]} ${IMG_TO_COMPOSITE[${idx}]} $BASE_PATH/${IMG_NAME}_negatives/$image $BASE_PATH/${IMG_NAME}_negatives/$image
	done
done
