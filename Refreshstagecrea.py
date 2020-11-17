from numpy import *
import time 
import pygame
from pygame.locals import *
pygame.init()
wdw=pygame.display.set_mode((1600,860))
def refresh(salle,sol,mur,rock,spike,flag,cdtrou,buton,door,buton2,door2,vide):
    for x in range(0 ,11):
        for y in range(0, 20):
            if salle[x,y] == 0:
                wdw.blit(sol,(y*60+200, x*60+100))
            if salle[x,y] == 1:
                wdw.blit(sol,(y*60+200, x*60+100))
                wdw.blit(mur,(y*60+200,x*60+100))
            if salle[x,y] == 2:
                wdw.blit(sol,(y*60+200, x*60+100))
                wdw.blit(rock,(y*60+200,x*60+100))
            if salle[x,y] == 4:
                wdw.blit(sol,(y*60+200, x*60+100))
                wdw.blit(spike,(y*60+200,x*60+100))
            if salle[x,y] == 3:
                wdw.blit(sol,(y*60+200, x*60+100))
                wdw.blit(flag,(y*60+200,x*60+100))
            if salle[x,y] == 5:
                wdw.blit(sol,(y*60+200, x*60+100))
                wdw.blit(cdtrou,(y*60+200,x*60+100))
            if salle[x,y] == 6:
                wdw.blit(sol,(y*60+200, x*60+100))
                wdw.blit(buton,(y*60+200,x*60+100))
            if salle[x,y] == 7:
                wdw.blit(sol,(y*60+200, x*60+100))
                wdw.blit(door,(y*60+200,x*60+100))
            if salle[x,y] == 8:
                wdw.blit(sol,(y*60+200, x*60+100))
                wdw.blit(cdtrou,(y*60+200,x*60+100))
                wdw.blit(rock,(y*60+200,x*60+100))
            if salle[x,y] == 9:
                wdw.blit(sol,(y*60+200, x*60+100))
                wdw.blit(buton2,(y*60+200,x*60+100))
            if salle[x,y] == 10:
                wdw.blit(sol,(y*60+200, x*60+100))
                wdw.blit(door2,(y*60+200,x*60+100))
            if salle[x,y] == 11:
                wdw.blit(vide,(y*60+200, x*60+100))
    pygame.display.update()