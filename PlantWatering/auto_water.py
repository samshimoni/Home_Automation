#! /usr/bin/env python3
from abc import ABC

import RPi.GPIO as GPIO
import time
import device
import mail_sender


class PlantWatering(device.Device, ABC):
    def is_alive(self):
        pass

    def __init__(self):
        super(PlantWatering, self).__init__(__name__)
        GPIO.setmode(GPIO.BCM)
        self.pinList = [self.cfg.pump_1_pin, self.cfg.pump_2_pin, self.cfg.pump_3_pin, self.cfg.pump_4_pin]
        self.water_sensor_pin = self.cfg.waterSensorPin
        self.delay = self.cfg.waterDelay
        self.mail = mail_sender.MailSender()

    def init_output(self):
        for i in self.pinList:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.HIGH)

    def auto_water(self, pin_number):
        consecutive_water_count = 0
        self.init_output()
        try:
            while consecutive_water_count < 3:
                time.sleep(self.delay)
                self.pump_on(pin_number)
                consecutive_water_count += 1

            GPIO.cleanup()
            response = 'Plant is no Longer dry... satisfied after {} times'.format(consecutive_water_count)

            self.logger.info(response)
            self.mail.send_mail(response)
            return response

        except KeyboardInterrupt:
            GPIO.cleanup()

    def pump_on(self, pin_number):
        self.init_output()
        GPIO.output(pin_number, GPIO.LOW)
        time.sleep(1)
        GPIO.output(pin_number, GPIO.HIGH)
