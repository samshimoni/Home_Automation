import serial
import device


class MoistureSensor(device.Device):
    def is_alive(self):
        pass

    def __init__(self):
        super(MoistureSensor, self).__init__(__name__)
        self.ser = serial.Serial(self.cfg.serial_port, self.cfg.baud_rate, timeout=1)

    def get_humidity(self):
        samples = []
        for i in range(10):
            try:
                serial_data = self.ser.readline().decode('ascii')[0:3]
            except:
                serial_data = 0

            value = int(serial_data)
            samples.append(value)

        return sum(samples) / len(samples)
