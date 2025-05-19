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
Display = pygame.display.set_mode((width, height))  #display surface objects
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
        Just_In.lights(centerx,centery,radius,acolor)
        display_message(message,20,centerx,centery+50,black)

        if clickx>230 and clickx <(230+40) and clicky>430 and clicky<(430+40) and MouseClicked == True:
            MouseClicked = False
            global life
            global GamePaused
            if life == -1:
                Enter_Game()
                main()
            elif GamePause == True:
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
        Just_In.lights(centerx,centery,radius,icolor)
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

def main():
    Obj1 = DodgeCars(Display)
    Obj2 = DodgeCars(Display)
    Objects = (Obj1,Obj2)  #Tuple of Objects
    Life = DodgeCars(Display)  #Objects to display life

    Carx = width*0.4  #X coord of my car
    Cary = height*0.8  #Y-Coord of my Car
    Car_width = 64
    Car_height = 104

    Previous_Score = DodgeCars(Display) #Object to display prev score
    Road_Count = 1

    x_change = 0
    y_change = 0

    Road_r = 600  #Right end of the road
    Current_Car1, OCar_w1, OCar_h1 = Objects[0].Opponent_Cars()
    OCar_Startx1,OCar_Starty1 = Objects[0].Opponent_Car_Coordinates()
    OCar_Speed1 = 7
    OCar_Speed2 = 7
    OCar_Speed3 = 9

    #when the score increases, the speed increases also
    OCARSSPEEDS = [OCar_Speed1, OCar_Speed2, OCar_Speed3]   #Initialising speed cars
    Add_Speed1 = OCARSSPEEDS[0]
    Add_Speed2 = OCARSSPEEDS[1]
    Add_Speed3 = OCARSSPEEDS[2]

    OCARSSPEED_UP = 15 #Speed increased when pressed upper arrow key
    Second_Car_First_time = 1

    ##Coords for setting the image of road and side trees
    Roadx = 200
    Roady = 580
    Treex1 = 0
    Treey1 = -580
    Treex2 = 605
    Treey2 = -580
    MoveRoad = 5
    MoveTree1 = 5
    MoveTree2 = 5

    TempTreeSpeed1 = 5
    TempTreeSpeed2 = 5
    TempRoadSpeed = 5
    count = 0
    Up_Press_Count = 1

    global GamePaused
    if GamePaused ==False:
        while not EndGame:
            Display.fill(roadcolor)
            Roady += MoveRoad
            Treey1 += MoveTree1
            Treey2 += MoveTree2

            if Roady > 10:
                Roady = -580
            if Treey1 > 10:
                Treey1 = -580
                Treey2 = -580
            Objects[0].Blit_Image(RoadImg1, Roadx, Roady)
            Objects[0].Blit_Image(TreeImg1, Treex1, Treey1)
            Objects[0].Blit_Image(TreeImg2, Treex2, Treey2)

            for event in pygame.event.get():  #Returning the list of the Occured Events

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYUP:  #What to do when the Key is Released
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == K_p: #if pressed and released 'p-button'
                        Pause()   #prev. function pres CTRL + left click
                if event.type == pygame.KEYDOWN:  #what to do when the key is actually pressed
                    if event.key == pygame.K_LEFT:
                        x_change = -6
                    elif event.key == pygame.K_RIGHT:
                        x_change = 6
                    elif event.key == pygame.K_UP:
                        if Up_Press_Count == 1:
                            Cary += -15
                        Up_Press_Count += 1
                        MoveRoad = 10
                        MoveTree1 = 10
                        MoveTree2 = 10
                        Add_Speed1 = 14

                        if count >= 10:
                            Add_Speed2 = 17
                    elif event.key == pygame.K_DOWN:
                        y_change = 5
                elif event.type == pygame.KEYUP:  #When the key is released
                    if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT \
                            or event.key ==pygame.K_DOWN:

                        x_change = 0
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        if Up_Press_Count>1:
                            Cary+=15
                        Add_Speed1 = OCARSSPEEDS[0]
                        MoveRoad = TempRoadSpeed
                        MoveTree1 = TempTreeSpeed1
                        MoveTree2 = TempTreeSpeed2

                        if count >= 10:
                            Add_Speed2 = OCARSSPEEDS[1]

            Carx += x_change #Changing the coord of the car
            OCar_Starty1 += Add_Speed1  # Moving the opening car along y-axis
            Objects[0].Blit_Image(CarImg, Carx, Cary)  #Displaying image of car to changed coord
            Objects[0].Blit_Image(Current_Car1, OCar_Startx1,OCar_Starty1)  #Displaying the image of Opponent car to new coord

            if count >= 10:
                OCar_Starty2 += Add_Speed2
                Objects[0].Blit_Image\
                    (Current_Car2, OCar_Startx2,OCar_Starty2)  #de variabelen 'Current_Car2, OCar_Startx2,OCar_Starty2'
                # worden later gecreeërd

            Objects[0].Score(count) # displaying the current score
            Previous_Score.Previous_Score()  #Displaying the prev score
            Life.Display_Life(life)  #Displaying the Life of the Player

            if Carx<200 or Carx > (width-Car_width) or (Cary+Car_height)>height or Cary<0: #Testing if the Car touched the sides of the road
                crash(Carx,Cary,count)
            if OCar_Starty1>height: #if opponent Car crosses the bottom of the screen








Entry_Screen()



