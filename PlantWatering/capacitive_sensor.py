import time
import serial
import device
import threading
import numpy as np


class MoistureSensor(device.Device):
    def is_alive(self):
        pass

    def __init__(self):
        super(MoistureSensor, self).__init__(__name__)
        self.ser = serial.Serial(self.cfg.serial_port, self.cfg.baud_rate, timeout=1)
        self.samples_worker = threading.Thread(target=self.write_humidity)
        self.samples_worker.start()
        self.lock = threading.Lock()
        self.humidity = []
        self.table = {3: 0, 4: 1, 17: 2}

    def write_humidity(self):
        for i in range(2):
            try:
                serial_data = self.ser.readline().decode('ascii')[0:-2]
            except ValueError:
                serial_data = '0 0 0'

        self.lock.acquire()
        values = serial_data.split(' ')
        self.humidity.append(int(values[0]))
        self.humidity.append(int(values[1]))
        self.humidity.append(int(values[2]))
        self.lock.release()

    def read_humidity(self, pin_number):
        self.lock.acquire()
        humidity = self.humidity
        self.lock.release()
        return humidity[self.table.get(pin_number)]


