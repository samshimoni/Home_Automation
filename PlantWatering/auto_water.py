import RPi.GPIO as GPIO
import datetime
import time
import device


def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)


class PlantWatering(device.Device):

    def __init__(self):
        super(PlantWatering, self).__init__(__name__)
        GPIO.setmode(GPIO.BOARD)
        self.pump_pin = self.cfg.pumpPin
        self.water_sensor_pin = self.cfg.waterSensorPin
        self.delay = self.cfg.waterDelay

    def is_alive(self):
        pass

    def get_status(self):
        GPIO.setup(self.water_sensor_pin, GPIO.IN)
        return GPIO.input(self.water_sensor_pin)

    def auto_water(self):
        consecutive_water_count = 0
        init_output(self.pump_pin)
        print("Here we go! Press CTRL+C to exit")
        try:
            wet = self.is_alive() == 0
            while wet is False and consecutive_water_count < 10:
                time.sleep(self.delay)
                self.pump_on()
                consecutive_water_count += 1
                wet = self.get_status() == 0

            GPIO.cleanup()
            print('Plant is no Longer dry... satisfied after {} times'.format(consecutive_water_count))

        except KeyboardInterrupt:  # If CTRL+C is pressed, exit cleanly:
            GPIO.cleanup()  # cleanup all GPI

    def pump_on(self):
        init_output(self.pump_pin)
        f = open("last_watered.txt", "w")
        f.write("Last watered {}".format(datetime.datetime.now()))
        f.close()
        GPIO.output(self.pump_pin, GPIO.LOW)
        time.sleep(1)
        GPIO.output(self.pump_pin, GPIO.HIGH)


gardener = PlantWatering()
gardener.auto_water()