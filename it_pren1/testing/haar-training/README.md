# HaarCascade Training
Bis ich mit dem Training effektiv beginnen konnte brauchte ich einige Stunden und viele Nerven. 

## Prerequisits
* openCV: https://docs.opencv.org/master/d0/db2/tutorial_macos_install.html
* imagemagick: brew install imagemagick
* ghostscript: brew install ghostscript

## Negative Samples
Negative Samples sind beliebige Bilder, welche das Objekt nicht enthalten dürfen.
1. Download Negative Bilder https://github.com/sonots/tutorial-haartraining/tree/master/data/negatives
2. in Arbeitsverzeichnis ablegen
3. TXT-Dokument mit Pfad zu allen negativen Bilder erstellen: `find negatives -type f > negatives.txt`

## Positive Samples
1. Piktogramm mit verschiedenen Kontrast- und Helligkeitsstufen anlegen. Für das Training habe ich 31 verschiedene Bilder vom gleichen Piktogramm erzeugt.
1. versch. Ansichten erstellen
    1. `create_positive_variants.sh` ![Skript](/create_positive_variants.sh) in cli aufrufen. Vorher Parameter anpassen

1. Postive Samples erstellen: Dazu `create_samples.sh n` Parameter n durch Anzahl gewünschten Samples pro Variante anpassen. Das Skript legt jeweils n-Bilder an, worauf das Piktogramm in verschiedener Ausrichtung und x/y/z veränderungen positioniert wurde. Pro Bild wird ein TXT mit Positionsangaben zum Piktogramm zum jeweiligen Bild angelegt.
1. Alle TXT in einem Dokument zusammenlegen: `cat FILENAME*.txt > positives.txt``
1. Trainingssamples erstellen und in Vec File speichern: `opencv_createsamples -info positives.txt -bg negatives.txt -vec data.vec -num 3200 -w 48 -h 48`
1. Training starten `opencv_traincascade -data data -vec data.vec -bg negatives.txt -numPos 3200 -numNeg 3000 -numStages 20 -precalcValBufSize 1024 -precalcIdxBufSize 1024 -featureType HAAR -minHitRate 0.995 -maxFalseAlarmRate 0.5 -w 48 -h 48`

1. `chmod a+rx script.sh`
1. `./myscript.sh`


## Learnings/Probleme
* Versionen von openCV > 3.4 unterstützten die Utilities die im Tutotrial (für V4.4.1) https://docs.opencv.org/4.1.0/dc/d88/tutorial_traincascade.html beschrieben sind nicht. Um die benötigten Tools `opencv_createsamples`, `opencv_annotations` und `opencv_traincascade` zu kompilieren musste ich auf Version 3.4 zurück.
* 20 Stages für das erste Training war wohl ein wenig viel :D
