import RPi.GPIO as GPIO
import datetime
import time
import device
import mail_sender


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
        self.mail = mail_sender.MailSender()

    def is_alive(self):
        pass

    def get_status(self):
        GPIO.setup(self.water_sensor_pin, GPIO.IN)
        return GPIO.input(self.water_sensor_pin)

    def auto_water(self):
        consecutive_water_count = 0
        init_output(self.pump_pin)
        try:
            wet = self.get_status() == 0
            while wet is False and consecutive_water_count < 10:
                time.sleep(self.delay)
                self.pump_on()
                consecutive_water_count += 1
                wet = self.get_status() == 0

            GPIO.cleanup()
            response = 'Plant is no Longer dry... satisfied after {} times'.format(consecutive_water_count)
            self.logger.info(response)
            self.mail.send_mail()
            return response

        except KeyboardInterrupt:
            GPIO.cleanup()

    def pump_on(self):
        init_output(self.pump_pin)
        f = open("last_watered.txt", "w")
        f.write("Last watered {}".format(datetime.datetime.now()))
        f.close()
        GPIO.output(self.pump_pin, GPIO.LOW)
        time.sleep(1)
        GPIO.output(self.pump_pin, GPIO.HIGH)


PlantWatering().auto_water()
