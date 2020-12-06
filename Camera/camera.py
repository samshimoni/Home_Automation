import os
import datetime
from device import Device
import re
import pygame.camera


class Camera(Device):
    def __init__(self):
        super(Camera, self).__init__(__name__)
        pygame.camera.init()
        pygame.camera.list_cameras()

    def is_alive(self):
        return True

    def capture(self):
        cam = pygame.camera.Camera("/dev/video0", (640, 480))
        cam.start()
        img = cam.get_image()
        pygame.image.save(img, self.cfg.camera_photos_dir + "/" + datetime.datetime.now().strftime("%Y-%m-%d|%H:%M:%S") + ".jpg")
        cam.stop()

    def clean_dir_from_photos(self):
        files = [f for f in os.listdir('Camera') if re.match(r'[0-9]+.*\.jpg', f)]
        for file in files:
            os.remove(self.cfg.camera_photos_dir + "/" + file)
