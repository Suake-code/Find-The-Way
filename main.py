from numpy import *
import time 
import pygame
from pygame.locals import *
from deplacements import *
from gammeplay import *
from actuallise import *
from level import *
niveauu = int
def menufinniveau(wdw, toutfini):
#toutfini en sortie : 0 => Le niveau n'est pas fini retour au menu. 1 => Le niveau est fini retours au menu. 2 => Le niveau n'est pas fini, on recommence. 3 => Le niveau est fini on vas au suivant.
    green = (0,200,0)
    font=pygame.font.Font(None, 24)
##    grandmenu = pygame.draw.rect(wdw, green,(500,290,600,300))

#Le niveau est fini
    if toutfini == 1:
        bsuivantimg = pygame.image.load("sprite/nextlvl.png").convert_alpha()
        bsuivant = bsuivantimg.get_rect() #Pour que Rect représente avec précision l'image chargé
        bsuivant = bsuivant.move(600, 340)
        wdw.blit(bsuivantimg, (600, 340))
        bretmenuimg = pygame.image.load("sprite/backtomenu.png").convert_alpha()
        bretmenu = bretmenuimg.get_rect() #Pour que Rect représente avec précision l'image chargé
        bretmenu = bretmenu.move(600, 440)
        wdw.blit(bretmenuimg, (600, 440))
        pygame.display.update()
        continuer = True
        while continuer:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    if bretmenu.collidepoint(event.pos):
                        return 1, False
                    if bsuivant.collidepoint(event.pos):
                        return 3, False
#Le niveau n'est pas fini
    if toutfini == 0 or toutfini == 2:
        bretryimg = pygame.image.load("sprite/retry.png").convert_alpha()
        bretry = bretryimg.get_rect() #Pour que Rect représente avec précision l'image chargé
        bretry = bretry.move(600, 340)
        wdw.blit(bretryimg, (600, 340))
        bretmenuimg = pygame.image.load("sprite/backtomenu.png").convert_alpha()
        bretmenu = bretmenuimg.get_rect() #Pour que Rect représente avec précision l'image chargé
        bretmenu = bretmenu.move(600, 440)
        wdw.blit(bretmenuimg, (600, 440))
        pygame.display.update()
        continuer = True
        while continuer:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    if bretmenu.collidepoint(event.pos):
                        return 0, False
                    if bretry.collidepoint(event.pos):
                        return 2, False
                if event.type == pygame.KEYDOWN and toutfini == 0:
                    if event.key == pygame.K_ESCAPE:
                        return 2, True
def jeu(niveau, perso1, perso2, perso3, perso4):
    continuer = True
    debug = 1
    wdw=pygame.display.set_mode((1600,880))
    #Dans le tableau: 0 = sol; 1 = mur; 2 = caillou; 3 = drapeau; 4 = piques, 5 = caillou dans le trou, 6 = bouton, 7 = porte
    #on importe toute les images
    mur = pygame.image.load("sprite/Mur.png").convert_alpha()
    sol = pygame.image.load("sprite/Sol.png").convert_alpha()
    flag = pygame.image.load("sprite/flag.png").convert_alpha()
    rock = pygame.image.load("sprite/rock.png").convert_alpha()
    win = pygame.image.load("sprite/win2.png").convert_alpha()
    defeat = pygame.image.load("sprite/death.png").convert_alpha()
    spike = pygame.image.load("sprite/piques.png").convert_alpha()
    setr = pygame.image.load("sprite/p+c.png").convert_alpha()
    door = pygame.image.load("sprite/closedoor.png").convert_alpha()
    buton = pygame.image.load("sprite/redbuton.png").convert_alpha()
    etat=int
    curX,curY = [9, 1]
    curXpast = int
    curYpast = int
    npdt = int
    npdtp = int
    porte = 1
    porte2 = 1
    etat = 1
    tour = 0
    salle = niveaux(niveau)
#    tour, curXpast, curYpast, npdt, npdtp, porte, porte2= refresh(wdw, debug, salle, curX, curY, mur, sol, flag, rock, win, defeat, spike, setr, door, buton, perso1, perso2, perso3, perso4, etat, tour, curXpast, curYpast, npdt, npdtp, porte, porte2)
    while continuer:
        if niveau == 9 :
            curX,curY = [8, 3]
        elif niveau == 10 :
            curX,curY = [9, 7]
        elif niveau == 3 :
            curX,curY = [7, 3]
        else :
            curX,curY = [9, 1]
        tour, curXpast, curYpast, npdt, npdtp, porte, porte2= refresh(wdw, debug, salle, curX, curY, mur, sol, flag, rock, win, defeat, spike, setr, door, buton, perso1, perso2, perso3, perso4, etat, tour, curXpast, curYpast, npdt, npdtp, porte, porte2)
        wdw, toutfini, curX, curY, wdw, salle, porte, etat, debug, tour, curXpast, curYpast, npdt, npdtp, porte2 = gameplay(curX, curY, wdw, salle, porte, etat, debug, tour, curXpast, curYpast, npdt, npdtp, porte2, perso1, perso2, perso3, perso4)
        print("Niveau = {0}, Toutfini = {1}, Wdw = {2}".format(niveau, toutfini, wdw))
        toutfini, continuer = menufinniveau(wdw, toutfini)
    return niveau, toutfini