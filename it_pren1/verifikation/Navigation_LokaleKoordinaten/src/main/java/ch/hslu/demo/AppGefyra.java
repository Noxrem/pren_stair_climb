package ch.hslu.demo;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.Scanner;

public class AppGefyra {

    public static final Logger LOGGER = LogManager.getLogger(AppGefyra.class);
    public static final int OFFSET_LINE = 30;
    public static final int OFFSET_STAIR = 20;
    public static final int BACKWARDS_DISTANCE = OFFSET_LINE + 10;

    private static final Roboter roboter = new Roboter(-1, -1);
    private static final Playground playground = new Playground(200, 150, roboter);
    private static boolean isAligned = false;
    private static Pictogram foundPictogram = Pictogram.PICTOGRAM0;
    private static int pictogramNumber = 0;

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        boolean isSetCorrectlyX = false;
        boolean isSetCorrectlyY = false;
        boolean isSetCorrectlyPictogram = false;
        do {
            LOGGER.info("Gib die X-Koordinate der Startposition des Roboters ein:");
            int inputPositionX = scanner.nextInt();
            if (inputPositionX <= playground.getWidth()) {
                isSetCorrectlyX = true;
                roboter.setPositionX(inputPositionX);
            } else {
                LOGGER.info("Die X-Koordinate darf nicht grösser sein als die Spielfeldbreite");
            }
        } while (!isSetCorrectlyX);
        do {
            LOGGER.info("Gib die Y-Koordinate der Startposition des Roboters ein:");
            int inputPositionY = scanner.nextInt();
            if (inputPositionY <= playground.getLength()) {
                isSetCorrectlyY = true;
                roboter.setPositionY(inputPositionY);
            } else {
                LOGGER.info("Die Y-Koordinate darf nicht grösser sein als die Spielfeldlänge");
            }
        } while (!isSetCorrectlyY);
        LOGGER.info("Gib die Art des Anfahrens an. Falls auf der Höhe des Piktogramms angefahren werden soll, gib 'true' ein, für mittiges Anfahren 'false'.");
        isAligned = scanner.nextBoolean();
        do {
            LOGGER.info("Gib die Nummer des Piktogramms ein, das erkannt wurde: ");
            pictogramNumber = scanner.nextInt();
            if (pictogramNumber <= 4) {
                isSetCorrectlyPictogram = true;
            } else {
                LOGGER.info("Es existieren nur die Piktogramme 0 - 4");
            }
        } while (!isSetCorrectlyPictogram);


        LOGGER.info("#########################################START LOKALISATION#############################################");
        //Start der Variante 1: Lokalisation mithilfe des Spielfeldrandes
        LOGGER.info("Startposition des Roboters: " + "(" + roboter.getPositionX() + "," + roboter.getPositionY() + ") mit Ausrichtung in Richtung Endlinie");
        if (roboter.getPositionY() + OFFSET_LINE >= playground.getLength()) {
            LOGGER.info("Roboter ist zu nahe an Endlinie und fährt zurück um " + BACKWARDS_DISTANCE);
            roboter.goBackwards(BACKWARDS_DISTANCE);
            LOGGER.info("Neue Position: " + "(" + roboter.getPositionX() + "," + roboter.getPositionY() + ")");
        }

        while (roboter.getPositionY() + OFFSET_LINE < playground.getLength()) { //Simuliert das Heranfahren an die Linie, bis erkannte Linie ganz unten im Blickfeld ist. Dann Stopp
            roboter.goForwards(1);
        }
        LOGGER.info("Roboter fährt vorwärts in Richtung Endlinie");
        LOGGER.info("Roboter hat die Endline erreicht mit Abstand " + OFFSET_LINE + ". Position: " + "(" + roboter.getPositionX() + "," + roboter.getPositionY() + ")");

        roboter.rotate90CounterClockWise();
        LOGGER.info("Roboter dreht um 90 Grad gegen den Uhrzeigersinn");

        if (roboter.getPositionX() < OFFSET_LINE) {//falls true; befindet sich Roboter unbestimmbar nahe am linken Rand
            roboter.goBackwards(BACKWARDS_DISTANCE);
            LOGGER.info("Roboter ist zu nahe an linker Linie und fährt zurück um " + BACKWARDS_DISTANCE + ". Position: " + "(" + roboter.getPositionX() + "," + roboter.getPositionY() + ")");
        }
        LOGGER.info("Roboter fährt vorwärts in Richtung linker Linie");

        while (roboter.getPositionX() > OFFSET_LINE) {
            roboter.goForwards(1);
        }
        LOGGER.info("Roboter hat die linke Linie erreicht mit Abstand " + OFFSET_LINE + ". Position: " + "(" + roboter.getPositionX() + "," + roboter.getPositionY() + ")");

        roboter.goBackwards(playground.getWidth() / 2 - OFFSET_LINE);
        LOGGER.info("Roboter fährt rückwärts");
        LOGGER.info("Roboter ist in der Mitte der Endlinie mit Abstand " + OFFSET_LINE + " zur Endlinie. Position: (" + roboter.getPositionX() + "," + roboter.getPositionY() + ")");

        roboter.rotate90CounterClockWise();
        LOGGER.info("Roboter dreht um 90 Grad gegen den Uhrzeigersinn. Nun schaut der Roboter in Richtung der Treppe");
        if (isAligned) {
            foundPictogram = choosePictogram(pictogramNumber);
            LOGGER.info("'Variante B: Treppe auf Höhe des Piktogrammes anfahren' wird ausgeführt.");
            goToPointsClimbAligned(foundPictogram);
        } else {
            LOGGER.info("'Variante A: Treppe mittig anfahren' wird ausgeführt.");
            goToPointClimbInTheMiddle();

        }
    }

    //Variante A: Treppe mittig anfahren:
    private static void goToPointClimbInTheMiddle() {
        roboter.goForwards(playground.getLength() - OFFSET_LINE - OFFSET_STAIR);
        LOGGER.info("Roboter fährt zur Position, wo Brücke abgelegt werden soll");
        LOGGER.info("Roboter hat die Ablageposition erreicht.");
        LOGGER.info("********************************************************************************************");
        LOGGER.info("Die SOLL-Position ist: (" + playground.getWidth() / 2 + "," + OFFSET_STAIR + ") / die IST-Position ist: (" + roboter.getPositionX() + "," + roboter.getPositionY() + ")");
        LOGGER.info("********************************************************************************************");
    }

    //Variante B: Treppe auf Höhe des Piktogrammes anfahren
    private static void goToPointsClimbAligned(Pictogram pictogram) {
        int wayY = playground.getLength() - OFFSET_STAIR - OFFSET_LINE;
        roboter.goForwards(wayY);
        LOGGER.info("Roboter fährt vorwärts zur Position " + roboter.getPositionX() + "," + roboter.getPositionY() + ")");
        int wayX;
        boolean isTurnClockwise;
        if (pictogram.targetXPosition >= playground.getWidth() / 2) {
            wayX = pictogram.targetXPosition - playground.getWidth() / 2;
            isTurnClockwise = false;
        } else {
            wayX = playground.getWidth() / 2 - pictogram.targetXPosition;
            isTurnClockwise = true;
        }
        if (isTurnClockwise) {
            roboter.rotate90ClockWise();
            LOGGER.info("Roboter dreht 90 Grad im Uhrzeigersinn");
            roboter.goForwards(wayX);
            LOGGER.info("Roboter fährt vorwärts zur Position " + roboter.getPositionX() + "," + roboter.getPositionY() + ")");
            roboter.rotate90CounterClockWise();
            LOGGER.info("Roboter dreht 90 Grad im Gegenuhrzeigersinn");
            LOGGER.info("********************************************************************************************");
            LOGGER.info("Die SOLL-Position ist: (" + pictogram.targetXPosition + "," + OFFSET_STAIR + ") / die IST-Position ist: (" + roboter.getPositionX() + "," + roboter.getPositionY() + ")");
            LOGGER.info("********************************************************************************************");

        } else {
            roboter.rotate90CounterClockWise();
            LOGGER.info("Roboter dreht 90 Grad im Gegenuhrzeigersinn");
            roboter.goForwards(wayX);
            LOGGER.info("Roboter fährt vorwärts zur Position " + roboter.getPositionX() + "," + roboter.getPositionY() + ")");
            roboter.rotate90ClockWise();
            LOGGER.info("Roboter dreht 90 Grad im Uhrzeigersinn");
            LOGGER.info("********************************************************************************************");
            LOGGER.info("Die SOLL-Position ist: (" + pictogram.targetXPosition + "," + OFFSET_STAIR + ") / die IST-Position ist: (" + roboter.getPositionX() + "," + roboter.getPositionY() + ")");
            LOGGER.info("********************************************************************************************");
        }
    }

    private static Pictogram choosePictogram(int number) {
        Pictogram chosenPictogram = null;

        switch (number) {
            case 0:
                chosenPictogram = Pictogram.PICTOGRAM0;
                LOGGER.info("Piktogramm 0 soll angefahren werden: " + chosenPictogram.name);
                break;
            case 1:
                chosenPictogram = Pictogram.PICTOGRAM1;
                LOGGER.info("Piktogramm 1 soll angefahren werden: " + chosenPictogram.name);
                break;
            case 2:
                chosenPictogram = Pictogram.PICTOGRAM2;
                LOGGER.info("Piktogramm 2 soll angefahren werden: " + chosenPictogram.name);
                break;
            case 3:
                chosenPictogram = Pictogram.PICTOGRAM3;
                LOGGER.info("Piktogramm 3 soll angefahren werden: " + chosenPictogram.name);
                break;
            case 4:
                chosenPictogram = Pictogram.PICTOGRAM4;
                LOGGER.info("Piktogramm 4 soll angefahren werden: " + chosenPictogram.name);
                break;
            default:
                chosenPictogram = Pictogram.PICTOGRAM0;
                LOGGER.error("Fehler in Piktogrammwahl. Gültig sind nur Zahlen von 0 - 4. Es wurde automatisch Piktogramm 0 gewählt.");
        }
        return chosenPictogram;
    }
}
