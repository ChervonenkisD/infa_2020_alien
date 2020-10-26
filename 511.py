import pygame
from pygame.draw import *
from math import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 700))
screen.fill([220, 220, 220])

#fon
rect(screen, [0, 255, 255], (0, 0, 600, 400))
rect(screen, [47, 79, 79], (-5, -5, 610, 405), 2)\

#cveta sun
R= 150
G= 255
B= 225
#centr sun
x=400
y=150
Rsun=200
#sun
circle(screen, [R, G, B], (x, y), Rsun, 30)

rect(screen, [R, G, B], (x-Rsun, y-10, x+Rsun, 20))
rect(screen, [R, G, B], (x-10, y-Rsun, 20, y+Rsun+40))

circle(screen, [R+70, G, B-10], (x, y), 25)
circle(screen, [R+70, G, B-10], (x-Rsun+10, y), 15)
circle(screen, [R+70, G, B-10], (x+Rsun-10, y), 15)
circle(screen, [R+70, G, B-10], (x, y-Rsun+10), 15)
circle(screen, [R+70, G, B-10], (x, y+Rsun-10), 15)

#mishka
#cveta tela i fona
r=220
g=220
b=220
#coordinati centra mishki
x=0
y=-0
#razmer mishki
a=1
#telo
ellipse(screen, [r, g, b], ((x+0)*a, (y+300)*a, 200*a, 300*a))
ellipse(screen, [0, 0, 0], ((x+0)*a, (y+300)*a, 200*a, 300*a), 2*a)

#head
ellipse(screen, [r, g, b], ((x+100)*a, (y+250)*a, 100*a, 70*a))
ellipse(screen, [0, 0, 0], ((x+100)*a, (y+250)*a, 100*a, 70*a), 2*a)
#rot
line(screen, [0, 0, 0], ((x+130)*a, (y+300)*a), ((x+130+60)*a, (y+300)*a))
#glas
circle(screen, [0, 0, 0], ((x+150)*a, (y+280)*a), 5*a)
#nos
circle(screen, [0, 0, 0], ((x+200)*a, (y+290)*a), 5*a)
#yxo
circle(screen, [r, g, b], ((x+110)*a, (y+260)*a), 10*a)
circle(screen, [0, 0, 0], ((x+110)*a, (y+260)*a), 10*a, 1*a)

#lunka stenka
ellipse(screen, [90, 80, 70], ((x+370)*a, (y+500)*a, 180*a, 100*a))
ellipse(screen, [0, 0, 0], ((x+370)*a, (y+500)*a, 180*a, 100*a), 1*a)
#lunka center
ellipse(screen, [85/1.5, 107/1.5, 47/1.5], ((x+380)*a, (y+530)*a, 160*a, 70*a))
ellipse(screen, [0, 0, 0], ((x+380)*a, (y+530)*a, 160*a, 70*a), 1*a)

#leska
line(screen, [0, 0, 0], ((x+440)*a, (y+200)*a), (x+440+10*a, y+200+250*a))

#YDOChKA
arc(screen, [0, 0, 0], ((x+190)*a, (y+200)*a, 500*a, 500*a), pi/2, pi, 3*a)

#Lapi verhnia
ellipse(screen, [r, g, b], ((x+170)*a, (y+380)*a, 70*a, 40*a))
ellipse(screen, [0, 0, 0], ((x+170)*a, (y+380)*a, 70*a, 40*a), 2*a)
# Lapi nignia
ellipse(screen, [r, g, b], ((x+100)*a, (y+520)*a, 130*a, 90*a))
ellipse(screen, [0, 0, 0], ((x+100)*a, (y+520)*a, 130*a, 90*a), 2*a)
ellipse(screen, [r, g, b], ((x+190)*a, (y+580)*a, 90*a, 40*a))
ellipse(screen, [0, 0, 0], ((x+190)*a, (y+580)*a, 90*a, 40*a), 2*a)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
