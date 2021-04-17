import logging

import busio
import adafruit_mpu6050


class Accelerometer:
    GPIO_SDA = None
    GPIO_SCL = None
    i2c = None
    AcceleratorModule = None

    def __init__(self):
        logging.info("create new Accelerometer")
        self.GPIO_SDA = 2
        self.GPIO_SCL = 3

        self.i2c = busio.I2C(self.GPIO_SCL, self.GPIO_SDA)
        self.AcceleratorModule = adafruit_mpu6050.MPU6050(self.i2c)

    def get_acceleration_x(self):
        x_axes = 0
        return self.AcceleratorModule.acceleration.__getitem__(x_axes)

    def get_acceleration_y(self):
        y_axes = 1
        return self.AcceleratorModule.acceleration.__getitem__(y_axes)

    def get_acceleration_z(self):
        z_axes = 2
        return self.AcceleratorModule.acceleration.__getitem__(z_axes)

    def get_temperature_in_celsius(self):
        return self.AcceleratorModule.temperature
