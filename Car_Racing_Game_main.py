import pygame
import random
import sys
import time
from pygame.locals import *
from racing_dodge_cars import DodgeCars
#5 import class racing_dodge_cars.py

#1 initialiseren screen
pygame.init()

width = 800
height = 600
FPS = 40  #Frame Rate 40x in 1 sec
white = (255, 255, 255)  #RPG value
l_red = (255, 0, 0)  #red color
red = (150, 0, 0)
l_green = (0, 255, 0)
green = (0, 150, 0)
yellow = (255, 229, 10)
l_yellow = (212, 255, 10)
black = (0, 0, 0)
roadcolor = (47, 47, 47)

#2 display
display = pygame.display.set_mode((width, height))  #display surface objects
pygame.display.set_caption("The Car Racing")  #Caption
clock = pygame.time.Clock()  #Time Object

#3 images
CarImg = pygame.image.load("images/car.png")
RoadImg1 = pygame.image.load("images/road1.jpg")
TreeImg1 = pygame.image.load("images/longtree1.jpg")
TreeImg2 = pygame.image.load("images/longtree2.jpg")
Bugatti = pygame.image.load("images/Bugatti.png")
GameIcon = pygame.image.load("images/GameIcon.png")
pygame.display.set_icon(GameIcon)

#4
life = 2  #Life of the Gamer
Previous_Score = DodgeCars(Display)  #Class to display the screen created
# in py_file'[[racing_dodge_cars.py]]

Previous_Score.Previous_Score()
EndGame = False
GamePause = False

#8instance
Just_In = DodgeCars(Display)


#6 function import class
def Entry_Screen():
    Entry = True
    Display.fill(white)
    #check cross button pressed or not
    while Entry:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        Color_Tuple = (red, yellow, green)
        Color = Color_Tuple[random.randint(0, 2)]

        display_message("Dodge Car", 70, 400, 100, Color)
        display_message("Made By: Alex Markus", 20, 650, 20, black)
        #7
        Just_In.Blit_Image(Bugatti, 175, 200)

        #8 function 3 buttons on initial screen
        Interactive(250, 450, 20, green, l_green, "Start!")
        Interactive(400, 450, 20, yellow, l_yellow, "Ready!")
        Interactive(550, 450, 20, red, l_red, "Quit!")

        pygame.display.update()
        clock.tick(30)

#18
def crash(OCar_startx,Ocar_Starty,count):
    Enter_Current_Score = DodgeCars(Display)
    #pass crash sound
    SoundObj = pygame.mixer.Sound('images/shot.wav')
    SoundObj.play()
    explosion(OCar_startx,Ocar_Starty) #create function later
    Enter_Current_Score.Enter_Current_Score(count)
    life_count() #create function later
    time.sleep(2)
    main() #create function later

#19
def explosion(OCar_startx,Ocar_Starty):
    ExpImg = pygame.image.load('images/explosion.gif')
    Display.blit(ExpImg,(OCar_startx,Ocar_Starty))
    pygame.display.update()

#20
def life_count():
    global life
    life -= 1
    if life == -1:
        GameOver = DodgeCars(Display)
        GameOver.gameover(width,height)

        while True:
            Restart_Page() #func to create later

#22
def Restart_Page():
    Interactive(250,450,20, green,l_green,"Restart!")  #coords button
    Interactive(550,450,20, red,l_red,"Quit!")  #coords button
    pygame.display.update()
    clock.tick(15)

#23
def Pause():
    global GamePaused
    pygame.mixer.music.pause()
    GamePaused = True

    while GamePaused:
        display_message("PAUSED",100,width/2,height/2,black)
        Interactive(250,450,20,green,l_green,"Continue!")
        Interactive(550,450,20,red,l_red,"Quit!")
        pygame.display.update()
        clock.tick(30)




#9 function Interactive
mousex,mousey = 0,0
clickx,clicky = 0,0
MouseClicked = False

def Interactive(centerx,centery,radius,icolor,acolor,message):
    global mousex,mousey
    global clickx,clicky
    global MouseClicked

    for event in pygame.event.get():
        if event.type ==MOUSEMOTION:
            mousex,mousey=event.pos
        elif event.type == MOUSEBUTTONDOWN:
            clickx,clicky= (event.pos)
            MouseClicked = True
        elif event.type == MOUSEBUTTONUP:
            clickx,clicky = event.pos
            MouseClicked = True
    left_x = centerx-radius
    left_y = centery-radius
    width_c = height_c = 2 *radius  #width and height of rect bounding circle

    if mousex>left_x and mousex<(left_x+width_c) and \
            mousey>left_y and mousey<(left_y+height_c):
        Just_In.light(centerx,centery,radius,acolor)
        display_message(message,20,centerx,centery+50,black)

        if clickx>230 and clickx <(230+40) and clicky>430 and clicky<(430+40) and MouseClicked == True:
            MouseClicked = False
            global life
            global GamePaused
            if life == -1:
                Enter_Game()
                main()
            elif GamePaused == True:
                GamePaused=False
                pygame.mixer.music.unpause()
            else:
                Enter_Game()
                main()
        elif clickx>530 and clickx<(530+40) and clicky>430 and clicky<(430+40)\
            and MouseClicked == True:
            pygame.quit()
            sys.exit()
    else:
        Just_In.lights(centerx,centery,radius,color)
        display_message(message,20,centerx,centery+50,black)

#24
def Enter_Game():
   Display.fill(roadcolor)
   Roadx = 200
   Roady = -580
   Treex1 = 0
   Treey1= 0
   Treex2 = 605
   Treey2 = 0

   Start_Number = DodgeCars(Display)
   At_start_time = 3

   while At_start_time >= 0:
       Start_Number.Blit_Image(RoadImg1, Roadx,Roady)  #Calling function to Blit
       Start_Number.Blit_Image(TreeImg1, Treex1,Treey1)  #Calling function to Blit
       Start_Number.Blit_Image(TreeImg2, Treex2,Treey2)  #Calling function to Blit

       if At_start_time == 0:
           display_message("Go", 150,width/2,height/2,black)
       else:
           display_message(str(At_start_time),150,width/2,height/2,black)

       At_start_time -= 1
       pygame.display.update()
       clock.tick(1)



#8 function for [[Car_Racing_Game.display_message line62,63]]
def display_message(text, size, x, y, color):
    TextObje = pygame.font.Font("font.ttf", size)
    TextSurf = TextObje.render(text, True, color)
    RectSurf = TextSurf.get_rect()
    RectSurf.center = (x, y)
    Display.blit(TextSurf, RectSurf)
    pygame.display.update()



