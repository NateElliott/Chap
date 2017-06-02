import os
import cv2
from django.conf import settings

class CamCapture:

    def __init__(self, file, ramp=30, camera=1):


        self.name = file
        self.file = os.path.join(settings.CAP_DIR,file)

        self.ramp = ramp
        self.camera = cv2.VideoCapture(camera)


        for i in range(ramp):
            temp = self.get_image()

        self.capture = self.get_image()
        cv2.imwrite(self.file, self.capture)


    def filename(self):
        return self.name


    def get_image(self):
        r,i = self.camera.read()
        return i


    def __str__(self):
        return self.file