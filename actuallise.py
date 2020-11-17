from numpy import *
import time 
import pygame
from pygame.locals import *
from onfaitduson import *
pygame.mixer.init(44100,-16,2,2048)
pygame.init()
wdw=pygame.display.set_mode((1600,880))
pas = pygame.mixer.Sound("Sound/pas.wav")
bruitpbouton = pygame.mixer.Sound("Sound/buton.wav")
pierredtrou = pygame.mixer.Sound("Sound/pierrequitombe.wav")
bloqué = pygame.mixer.Sound("Sound/bloqué.wav")
dooro = pygame.image.load("sprite/opendoor.png").convert_alpha()
butonv = pygame.image.load("sprite/vertbuton.png").convert_alpha()
doorf = pygame.image.load("sprite/closedoor.png").convert_alpha()
butonr = pygame.image.load("sprite/redbuton.png").convert_alpha()
def refresh(wdw, debug, salle, curX, curY, mur, sol, flag, rock, win, defeat, spike, setr, door, buton, perso1, perso2, perso3, perso4, etat, tour, curXpast, curYpast, npdt, npdtp, porte, porte2):
    print("Voici la salle :", salle,"\n elle est de type :", type(salle))
    if tour == 0:
        curXpast = curX
        curYpast = curY
        npdtp = 0
        bandeson(0)
    bandeson(1)
    npdt = 0
    tour += 1
    print("Salle :",salle, "CurX :",curX,"CurY",curY)
    if salle[curX,curY] == 6 and porte == 1:
        bruitpbouton.play()
    if salle[curX,curY] == 9 and porte2 == 1:
        bruitpbouton.play()
    if salle[curX, curY] == 6:
        if debug == 1:
            print ("porte = {0} et porte2 = {1}".format(porte, porte2))
        if porte == 1:
            porte = 0
##        elif porte == 0:
##            porte = 1
    if porte == 0:
        door = dooro
        buton = butonv
    if porte == 1:
        door = doorf
        buton = butonr
    if salle[curX, curY] == 9:
        if debug == 1:
            print ("porte = {0}".format(porte))
        if porte2 == 1:
            porte2 = 0
    if porte2 == 0:
        door2 = dooro
        buton2 = butonv
    if porte2 == 1:
        door2 = doorf
        buton2 = butonr
    if debug == 1:
        print("\nActuallisation \ncurX={0} \ncurY={1} \ncurXpast={2} \ncurYpast={3} \ntour={4} \nnpdt={5} \nnpdtp={6}".format(curX, curY, curXpast, curYpast, tour, npdt, npdtp))
    for x in range(0 ,11):
        for y in range(0, 20):
            if salle[x,y] == 0:
                wdw.blit(sol,(y*80, x*80))
            if salle[x,y] == 1:
                wdw.blit(sol,(y*80, x*80))
                wdw.blit(mur,(y*80,x*80))
            if salle[x,y] == 2:
                wdw.blit(sol,(y*80, x*80))
                wdw.blit(rock,(y*80,x*80))
            if salle[x,y] == 4:
                wdw.blit(sol,(y*80, x*80))
                wdw.blit(spike,(y*80,x*80))
            if salle[x,y] == 3:
                wdw.blit(sol,(y*80, x*80))
                wdw.blit(flag,(y*80,x*80))
            if salle[x,y] == 5:
                wdw.blit(sol,(y*80, x*80))
                wdw.blit(setr,(y*80,x*80))
                npdt += 1
            if salle[x,y] == 6:
                wdw.blit(sol,(y*80, x*80))
                wdw.blit(buton,(y*80,x*80))
            if salle[x,y] == 7:
                wdw.blit(sol,(y*80, x*80))
                wdw.blit(door,(y*80,x*80))
            if salle[x,y] == 8:
                wdw.blit(sol,(y*80, x*80))
                wdw.blit(setr,(y*80,x*80))
                wdw.blit(rock,(y*80,x*80))
                npdt += 1
            if salle[x,y] == 9:
                wdw.blit(sol,(y*80, x*80))
                wdw.blit(buton2,(y*80,x*80))
            if salle[x,y] == 10:
                wdw.blit(sol,(y*80, x*80))
                wdw.blit(door2,(y*80,x*80))
        if etat == 1:
            wdw.blit(perso1,(curY*80,curX*80))
        if etat == 2:
            wdw.blit(perso2,(curY*80,curX*80))
        if etat == 3:
            wdw.blit(perso3,(curY*80,curX*80))
        if etat == 4:
            wdw.blit(perso4,(curY*80,curX*80))
    if salle[curX, curY] == 3:
        wdw.blit(win, (0,0))
        pygame.display.flip()
        print("Felicitation, vous avez gagné")
    if salle[curX, curY] == 4:
        wdw.blit(sol,(curY*80, curX*80))
        wdw.blit(defeat, (curY*80,curX*80))
        pygame.display.flip()
        print("Vous êtes mort")
#        for event in pygame.event.get():
#            if event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_ESCAPE:
#                    if debug ==1:
#                        print("\nArrêt")
#                    pygame.quit()
#                    quit()
    if curXpast != curX or curYpast != curY:
        pas.play()
    else:
        bloqué.play()
    if tour != 0:
        if npdtp != npdt:
            pierredtrou.play()
    npdtp = npdt
    curXpast, curYpast = curX, curY
    pygame.display.update()
    return tour, curXpast, curYpast, npdt, npdtp, porte, porte2
