# HaarCascade Training
Bis ich mit dem Training effektiv beginnen konnte, musste ich ersten einige Anleitungen lesen, Bilder sammeln und brauchte dazu viele Nerven.

## Prerequisits
* openCV: https://docs.opencv.org/master/d0/db2/tutorial_macos_install.html
* imagemagick: brew install imagemagick
* ghostscript: brew install ghostscript
* Shell-Skripts `create_positive_variants.sh` und `create_samples.sh`
* Brechtigungen zum Ausführen der Skripts anpassen `chmod a+rx scripts.sh`

## Negative Samples
Negative Samples sind beliebige Bilder, welche das Objekt **nicht** enthalten dürfen.
1. Download Negative Bilder https://github.com/sonots/tutorial-haartraining/tree/master/data/negatives
2. in Arbeitsverzeichnis ablegen
3. TXT-Dokument mit Pfad zu allen negativen Bilder erstellen: `find negatives -type f > negatives.txt`

## Positive Samples
1. Piktogramm mit verschiedenen Kontrast- und Helligkeitsstufen anlegen. Für das Training habe ich 31 verschiedene Bilder vom gleichen Piktogramm erzeugt.
1. versch. Ansichten erstellen
    1. `create_positive_variants.sh` Skript in cli aufrufen. Vorher Variablen `ITERATIONS`, `IMG_IN_PATH`, `IMG_OUT_PATH` anpassen

1. Postive Samples erstellen: Dazu `create_samples.sh n` Parameter *n* durch Anzahl gewünschten Samples pro Variante anpassen. Das Skript legt jeweils *n*-Bilder an, worauf das Piktogramm in verschiedener Ausrichtung und x/y/z veränderungen positioniert wurde. Pro Bild wird ein TXT mit Positionsangaben zum Piktogramm zum jeweiligen Bild angelegt.
1. Alle TXT in einem Dokument zusammenlegen: `cat FILENAME*.txt > positives.txt`
1. Trainingssamples erstellen und in Vec File speichern: `opencv_createsamples -info positives.txt -bg negatives.txt -vec data.vec -num 3200 -w 48 -h 48`
1. Training starten `opencv_traincascade -data data -vec data.vec -bg negatives.txt -numPos 3200 -numNeg 3000 -numStages 20 -precalcValBufSize 1024 -precalcIdxBufSize 1024 -featureType HAAR -minHitRate 0.995 -maxFalseAlarmRate 0.5 -w 48 -h 48`


## Learnings/Probleme
* Versionen von openCV > 3.4 unterstützten die Utilities die im Tutotrial (für V4.4.1) https://docs.opencv.org/4.1.0/dc/d88/tutorial_traincascade.html beschrieben sind nicht. Um die benötigten Tools `opencv_createsamples`, `opencv_annotations` und `opencv_traincascade` zu kompilieren musste ich auf Version 3.4 zurück.
* 20 Stages für das erste Training war wohl ein wenig viel :D
* Objekte nicht rotieren da sie fix ausgerichtet stehen werden und so Fehlerkennung minimiert werden kann
* Winkel der X/Y-Achsen nur marginal verändern
* Fehler von immer gleichen Hintergrundbilder, beim generieren der Background-Images -> evtl. auf manuelles Starten des Befehls ausweichen oder separate TXT-Files führen
* Training auf Server machen nicht Laptop -> mittlerweile Linux Server beim EnterpriseLab dafür im Einsatz
* Anzahl der Erkennung merken und Signal für Erkennung erst ausgeben, wenn Threshold überschritten
* Strategy Pattern könnte evtl. für anschliessende Ausgabe, weiterer Prozess angewendet werden
* Im Training einzelner Piktogramme die anderen als Fehler einbauen
* Nicht zu helle Positives verwenden, da Licht sonst als solches erkannt wird
