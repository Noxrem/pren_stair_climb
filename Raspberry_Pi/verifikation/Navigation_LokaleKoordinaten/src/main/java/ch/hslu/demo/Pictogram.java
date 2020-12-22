package ch.hslu.demo;

public enum Pictogram {
    PICTOGRAM0("Hammer", 125 ), PICTOGRAM1("Sandwich", 100),
    PICTOGRAM2("Lineal", 75), PICTOGRAM3("Farbeimer", 50),
    PICTOGRAM4("Bleistift",25);

    String name;
    int targetXPosition;

    Pictogram(String name, int targetXPosition){
        this.name = name;
        this.targetXPosition = targetXPosition;
    }
}
