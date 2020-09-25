import os
import datetime
import subprocess
from device import Device


def create_path():
    script_dir = os.path.dirname(__file__)
    currentdate = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
    rel_path = currentdate +".jpg"
    abs_file_path = os.path.join(script_dir, rel_path)
    return abs_file_path


class Camera(Device):
    def __init__(self, path):
        self.path = path

    def is_alive(self):
        return 'Webcam' in os.popen('lsusb').read()

    def capture(self):
        p = subprocess.Popen(self.path)
        p.wait()

