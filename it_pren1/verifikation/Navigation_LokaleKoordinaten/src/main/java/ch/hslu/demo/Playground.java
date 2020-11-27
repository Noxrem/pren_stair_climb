package ch.hslu.demo;

public class Playground {

    private final int length;
    private final int width;
    private final Roboter roboter;

    Playground(int length, int width, Roboter roboter){
        this.length = length;
        this.width = width;
        this.roboter = roboter;
    }

    public int getLength() {
        return length;
    }

    public int getWidth() {
        return width;
    }

    public Roboter getRoboter() {
        return roboter;
    }
}
