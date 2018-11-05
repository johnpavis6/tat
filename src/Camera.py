from datetime import date,datetime
import pygame
import pygame.camera
import os

pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
dir=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
dir='/var/www/html/photos/'+dir
dir='photos'
#os.mkdir(dir)
def take_photo():
    img = cam.get_image()
    t=date.today()
    name=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    url=dir+'/'+name+'.jpg'
    pygame.image.save(img,url)
