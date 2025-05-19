import pygame
import sys
import os
import time
import random
from pygame.locals import *

# from Car_Racing_Game_main import *


class DodgeCars:        #initialiser function of class
    #constructor function

    def __init__(self,Display):
        self.Display = Display
        self.white = (255,255,255)
        self.red = (255,0,0)
        self.black = (0,0,0)
        self.width = 800
        self.height = 600
        self.GOImg = pygame.image.load("images/gameover.png")
        self.PsScore = []


    #display image function
    def Blit_Image(self,Image,x,y):  #coordinates image
        self.Display.blit(Image,(x,y))
    #10 function opponents
    def Opponent_Cars(self):
        self.Opp_Cars = [pygame.image.load("images/caropp1.png"),pygame.image.load("images/BLUECAR.png"),pygame.image.load("images/caropp3.png")]
        self.Opp_Cars_HW = [(65,104),(64,106),(63,104)]
        self.Random_Number = random.randrange(0,3)
        self.Current_Car = self.Opp_Cars[self.Random_Number]
        self.Current_W,self.Current_H = self.Opp_Cars_HW[self.Random_Number]
        return self.Current_Car,self.Current_W,self.Current_H

    #11 function opponent car coordinates
    def Opponent_Car_Coordinates(self,Road_r):
        self.OCar_Startx = random.randrange(200,Road_r,-64)
        self.OCar_Startylist = [-10,-20,-15,-12,-23]
        self.OCar_Starty = self.OCar_Startylist[random.randrange(0,4)]
        return self.OCar_Startx, self.OCar_Starty

    #12 score count
    def Score(self,count):
        self.ScoreObj  = pygame.font.Font("font.ttf", 30)
        self.ScoreSurf = self.ScoreObj.render("Score: "+str(count), True, self.black)
        self.Display.blit(self.ScoreSurf,(0,0))

    #13 function gameover image
    def gameover(self,width,height):
        self.Display.blit(self.GOImg,(100,200))
        pygame.display.update()
        time.sleep(2)

    #14 current score save to file
    def Enter_Current_Score(self,c_score):
        Write = open("hiscore.txt",'a')
        Write.write('\n')
        Write.write(str(c_score))
        Write.close()

    #15 display current en previous score on screen
    def Previous_Score(self):
        Read = open("hiscore.txt", 'r')
        self.score = Read.readlines()
        Read.close()
        self.score = [x.rstrip() for x in self.score]  # go through all the scores\
        # and store in list and strip all white space right side
        self.score = [int(x) for x in self.score]
        self.score.sort()
        if len(self.score) > 0:
            DodgeCars.Show_Previous_Score(self,self.score[len(self.score)-1])  #get the length of the previous scores\

    #16
    def Show_Previous_Score(self,Pscore):
        self.DScoreObj = pygame.font.Font("font.ttf", 20)
        self.DScoreSurf = self.ScoreObj.render("Previous High Score "+ str(Pscore), True, self.black)
        self.Display.blit(self.DScoreSurf,(0,575))

    #17
    def Display_Life(self,life):
        self.ScoreObj = pygame.font.Font("font.ttf", 30)
        self.ScoreSurf = self.ScoreObj.render("turns left : "+str(life), True,self.black)
        self.Display.blit(self.ScoreSurf,(620,0))


    def lights(self,centerx,centery,radius,color):
        pygame.draw.circle(self.Display,color,(centerx,centery), radius)
    # def Previous_Score(self):
    #     pass
