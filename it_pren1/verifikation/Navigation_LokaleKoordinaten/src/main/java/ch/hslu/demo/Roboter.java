package ch.hslu.demo;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Roboter {

    public static final Logger LOGGER = LogManager.getLogger(Roboter.class);

    private int positionX;
    private int positionY;
    private int direction; //0=Entgegen Treppe, 1 = nach Links, 2 = zur Treppe, 3 = nach Rechts

    public Roboter(int positionX, int positionY) {
        this.positionX = positionX;
        this.positionY = positionY;
        this.direction = 0;

    }

    public void rotate90CounterClockWise() {
        this.direction = (direction + 1) % 4;
    }

    public void rotate180CounterClockWise() {
        this.direction = (direction + 2) % 4;
    }

    public void rotate90ClockWise() {
        this.direction = (direction + 3) % 4;
    }

    public void goForwards(int distance) {
        switch (this.direction) {
            case 0:
                this.positionY += distance;
                break;
            case 1:
                this.positionX -= distance;
                break;
            case 2:
                this.positionY -= distance;
                break;
            case 3:
                this.positionX += distance;
                break;
            default:
                LOGGER.error("Fehler in goForwards(). Die direction ist " + this.direction);
        }
    }

    public void goBackwards(int distance) {
        switch (this.direction) {
            case 0:
                this.positionY -= distance;
                break;
            case 1:
                this.positionX += distance;
                break;
            case 2:
                this.positionY += distance;
                break;
            case 3:
                this.positionX -= distance;
                break;
            default:
                LOGGER.error("Fehler in goBackwards(). Die direction ist " + this.direction);

        }
    }

    public int getPositionX() {
        return positionX;
    }

    public int getPositionY() {
        return positionY;
    }

    public void setPositionX(int positionX) {
        this.positionX = positionX;
    }

    public void setPositionY(int positionY) {
        this.positionY = positionY;
    }
}
