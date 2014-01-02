#
# Send Photo tweets from you Raspberry Pi
#


#!/usr/bin/env python
import sys
import pygame
import pygame.camera
from pygame.locals import *
from twython import Twython

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(1280,800)) #Configure your video path and your resolution
cam.start()
image = cam.get_image()
pygame.image.save(image,'webcam.jpg') # The filename of your capture.

#
#Configure your Twitter credentials.
#

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

photo = open('webcam.jpg','rb')
#You should write here your status.
api.update_status_with_media(media=photo, status='Timelapse')

