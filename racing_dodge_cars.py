import pygame,sys,os,time,random
from pygame.locals import *

class DodgeCars:        #initialiser function of class
    #constructor function
    def __init__(self,Display):
        self.Display = Display
        self.white = (255,255,255)
        self.red = (255,0,0)
        self.black = (0,0,0)
        self.widh = 800
        self.height = 600
        self.GOIMG = pygame.image.load("gameover.png")

    #display image function
    def Blit_Image(self,Image,x,y):  #coordinates image
        self.Display.blit(Image,(x,y))

    def lights(self,centerx,centery,radius,color):
        pygame.draw.circle(self.Display,color,(centerx,centery), radius)

    # def Previous_Score(self):
    #     pass
