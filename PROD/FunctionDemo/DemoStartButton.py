from RPi import GPIO
from time import sleep

# Setup GPIO to Input with PullUpResistor
GPIO_PIN_START_BUTTON = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN_START_BUTTON, GPIO.IN, GPIO.PUD_UP)

buttonPressed = False

try:
    print("Demo Start-Button")
    while True:  # this will carry on until you hit CTRL+C
        if GPIO.input(GPIO_PIN_START_BUTTON):
            if not buttonPressed:
                print("Start-Button is pressed")
                buttonPressed = True
        else:
            if buttonPressed:
                print("Start-Button is released")
                buttonPressed = False

        sleep(0.2)  # Entprellen

finally:  # this block will run no matter how the try block exits
    GPIO.cleanup()  # clean up after yourself