import pygame
import main
import time
from onfaitduson import *
from pygame.locals import *
import sayve
import stagecrea
#Voici mon premier projet avec lequel j'ai découvert python et la programation. L'ensemble est donc très sale mais le jeu fonctionne à peut près.
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
white = (255,255,255)
black = (0,0,0)
wdw=pygame.display.set_mode((1600,880))
niveau = int
global lastlevel
lastlevel = int
# Pour savoir si quand il sort du niveau, il est fini
perso2 = pygame.image.load("sprite/persoUp.png").convert_alpha()
perso1 = pygame.image.load("sprite/persoDown.png").convert_alpha()
perso4 = pygame.image.load("sprite/persoRight.png").convert_alpha()
perso3 = pygame.image.load("sprite/persoLeft.png").convert_alpha()
def menuprincipal():
    global lastlevel
    global perso2
    global perso1
    global perso4
    global perso3
    lastlevel = sayve.save(lastlevel)
    toutfini = int
    pygame.init()
    font = pygame.font.Font(None, 24)
    fenetre = 0# Pour savoir sur quelle fenetre on se trouve
    feetre2 = 0# Pour savoir sur quelle fenetre on se trouve
    bandeson(-1)
    
    fond = pygame.image.load("sprite/menu.png").convert_alpha()
    wdw.blit(fond, (0,0))
    pygame.display.set_caption("Find The Way")
    
    player = perso4
    position = player.get_rect()
    position = position.move(460, 685)
    wdw.blit(player, position)
            
    btcloseimg = pygame.image.load("sprite/closebuton.png").convert_alpha()
    btclose = btcloseimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btclose = btclose.move(1137, 640) #Permet de le déplacer
    wdw.blit(btcloseimg, (1137, 640))
    
    btcreditimg = pygame.image.load("sprite/credit.png").convert_alpha()
    btcredit = btcreditimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btcredit = btcredit.move(263, 640) #Permet de le déplacer
    wdw.blit(btcreditimg, (263, 640))
    
    #--------------------------------------------------------------------------------------------
    btpersoimg = pygame.image.load("sprite/btperso.png").convert_alpha()
    btperso = btpersoimg.get_rect() 
    btperso = btperso.move(263, 500) 
    wdw.blit(btpersoimg, (263, 500))
    #--------------------------------------------------------------------------------------------
    btcreerimg = pygame.image.load("sprite/Creer.png").convert_alpha()
    btcreer = btcreerimg.get_rect() 
    btcreer = btcreer.move(1137, 500) 
    wdw.blit(btcreerimg, (1137, 500))
    #--------------------------------------------------------------------------------------------
    btlevelimg = pygame.image.load("sprite/lvl.png").convert_alpha()
    btlevel = btlevelimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlevel = btlevel.move(900, 220) #Permet de le déplacer
    wdw.blit(btlevelimg, (900, 220))
    
    bttutorielimg = pygame.image.load("sprite/Tuto.png").convert_alpha()
    bttutoriel = bttutorielimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    bttutoriel = bttutoriel.move(500, 220) #Permet de le déplacer
    wdw.blit(bttutorielimg, (500, 220))
    
    pygame.display.update()
    continuer = True
    x=0
    position = position.move(2, 0)
    while continuer:
        x += 1
        wdw.blit(fond, position, position)  
        if x < 300 :
            position = position.move(2, 0)#déplacer le joueur
            player = perso4
        elif x < 600 :
            position = position.move(-2, 0)
            player = perso3
        elif x < 900 :
            x=0
        wdw.blit(player, position)                #dessiner un nouveau joueur
        pygame.display.update()                      #afficher le tout
        pygame.time.delay(10)   
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP and fenetre == 0:
                if event.button == 1:
                    if btclose.collidepoint(event.pos):
                        fenetre = 1
                        pygame.quit()
                        quit()
                if event.button == 1:
                    if btlevel.collidepoint(event.pos):
                        fenetre = 1
                        menulevel(fenetre)
                if event.button == 1:
                    if bttutoriel.collidepoint(event.pos):
                        fenetre = 1
                        menututoriel(fenetre)
                if event.button == 1:
                    if btcredit.collidepoint(event.pos):
                        fenetre = 1
                        credits(fenetre)
                if event.button == 1:
                    if btperso.collidepoint(event.pos):
                        fenetre == 1
                        menuperso(fenetre)
                if event.button == 1:
                    if btcreer.collidepoint(event.pos):
                        fenetre == 1
                        stagecrea.creation(perso1, perso2, perso3, perso4)
            if event.type == pygame.QUIT:
                print("\nArrêt")
                pygame.quit()
                quit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_ESCAPE :
            #         print("\nArrêt")
            #         pygame.quit()
            #         quit()
def menulevel(fenetre):
    global lastlevel
    suivant = 0
    pygame.init()
    pygame.display.flip()
    # pour savoir de quel niveau il sort
    niveau = int
    # Pour savoir si quand il sort du niveau, il est fini
    toutfini = 0
    continuer = True
    fond = pygame.image.load("sprite/menu.png").convert_alpha()
    wdw.blit(fond, (0,0))
    font=pygame.font.Font(None, 24)
    
    btsuiteimg = pygame.image.load("sprite/next.png").convert_alpha()
    btsuite = btsuiteimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btsuite = btsuite.move(100, 640) #Permet de le déplacer
    wdw.blit(btsuiteimg, (100, 640))
    
    btbackimg = pygame.image.load("sprite/menubuton.png").convert_alpha()
    btback = btbackimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btback = btback.move(1300, 640) #Permet de le déplacer
    wdw.blit(btbackimg, (1300, 640))
    

    if lastlevel == 0:
        btlvl1nimg = pygame.image.load("sprite/lvl1n.png").convert_alpha()
    elif lastlevel >= 1:
        btlvl1nimg = pygame.image.load("sprite/lvl1d.png").convert_alpha()
    btlvl1n = btlvl1nimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlvl1n = btlvl1n.move(100, 120) #Permet de le déplacer
    wdw.blit(btlvl1nimg, (100, 120))
        
    if lastlevel == 0:
        btlvl2vimg = pygame.image.load("sprite/lvl2v.png").convert_alpha()
    elif lastlevel == 1:
        btlvl2vimg = pygame.image.load("sprite/lvl2n.png").convert_alpha()
    elif lastlevel > 1:
        btlvl2vimg = pygame.image.load("sprite/lvl2d.png").convert_alpha()
    btlvl2v = btlvl2vimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlvl2v = btlvl2v.move(400, 120) #Permet de le déplacer
    wdw.blit(btlvl2vimg, (400, 120))
    
    if lastlevel <=1:
        btlvl3vimg = pygame.image.load("sprite/lvl3v.png").convert_alpha()
    elif lastlevel == 2:
        btlvl3vimg = pygame.image.load("sprite/lvl3n.png").convert_alpha()
    elif lastlevel > 2:
        btlvl3vimg = pygame.image.load("sprite/lvl3d.png").convert_alpha()
    btlvl3v = btlvl3vimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlvl3v = btlvl3v.move(700, 120) #Permet de le déplacer
    wdw.blit(btlvl3vimg, (700, 120))
    
    if lastlevel <= 2:
        btlvl4vimg = pygame.image.load("sprite/lvl4v.png").convert_alpha()
    elif lastlevel == 3:
        btlvl4vimg = pygame.image.load("sprite/lvl4n.png").convert_alpha()
    elif lastlevel > 3:
        btlvl4vimg = pygame.image.load("sprite/lvl4d.png").convert_alpha()
    btlvl4v = btlvl4vimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlvl4v = btlvl4v.move(1000, 120) #Permet de le déplacer
    wdw.blit(btlvl4vimg, (1000, 120))
    
    if lastlevel <= 3:
        btlvl5vimg = pygame.image.load("sprite/lvl5v.png").convert_alpha()
    elif lastlevel == 4:
        btlvl5vimg = pygame.image.load("sprite/lvl5n.png").convert_alpha()
    elif lastlevel > 4:
        btlvl5vimg = pygame.image.load("sprite/lvl5d.png").convert_alpha()
    btlvl5v = btlvl5vimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlvl5v = btlvl5v.move(1300, 120) #Permet de le déplacer
    wdw.blit(btlvl5vimg, (1300, 120))
    
    if lastlevel <= 4:
        btlvl6vimg = pygame.image.load("sprite/lvl6v.png").convert_alpha()
    elif lastlevel == 5:
        btlvl6vimg = pygame.image.load("sprite/lvl6n.png").convert_alpha()
    elif lastlevel > 5:
        btlvl6vimg = pygame.image.load("sprite/lvl6d.png").convert_alpha()
    btlvl6v = btlvl6vimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlvl6v = btlvl6v.move(100, 300) #Permet de le déplacer
    wdw.blit(btlvl6vimg, (100, 300))
    
    if lastlevel <= 5:
        btlvl7vimg = pygame.image.load("sprite/lvl7v.png").convert_alpha()
    elif lastlevel == 6:
        btlvl7vimg = pygame.image.load("sprite/lvl7n.png").convert_alpha()
    elif lastlevel > 6:
        btlvl7vimg = pygame.image.load("sprite/lvl7d.png").convert_alpha()
    btlvl7v = btlvl7vimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlvl7v = btlvl7v.move(400, 300) #Permet de le déplacer
    wdw.blit(btlvl7vimg, (400, 300))
    
    if lastlevel <= 6:
        btlvl8vimg = pygame.image.load("sprite/lvl8v.png").convert_alpha()
    elif lastlevel == 7:
        btlvl8vimg = pygame.image.load("sprite/lvl8n.png").convert_alpha()
    elif lastlevel > 7:
        btlvl8vimg = pygame.image.load("sprite/lvl8d.png").convert_alpha()
    btlvl8v = btlvl8vimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlvl8v = btlvl8v.move(700, 300) #Permet de le déplacer
    wdw.blit(btlvl8vimg, (700, 300))
    
    if lastlevel <= 7:
        btlvl9vimg = pygame.image.load("sprite/lvl9v.png").convert_alpha()
    elif lastlevel == 8:
        btlvl9vimg = pygame.image.load("sprite/lvl9n.png").convert_alpha()
    elif lastlevel > 8:
        btlvl9vimg = pygame.image.load("sprite/lvl9d.png").convert_alpha()
    btlvl9v = btlvl9vimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlvl9v = btlvl9v.move(1000, 300) #Permet de le déplacer
    wdw.blit(btlvl9vimg, (1000, 300))
    
    if lastlevel <= 8:
        btlvl10vimg = pygame.image.load("sprite/lvl10v.png").convert_alpha()
    elif lastlevel == 9:
        btlvl10vimg = pygame.image.load("sprite/lvl10n.png").convert_alpha()
    elif lastlevel > 9:
        btlvl10vimg = pygame.image.load("sprite/lvl10d.png").convert_alpha()
    btlvl10v = btlvl10vimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlvl10v = btlvl10v.move(1300, 300) #Permet de le déplacer
    wdw.blit(btlvl10vimg, (1300, 300))
    
    if lastlevel <= 9:
        btlvl11vimg = pygame.image.load("sprite/lvl11v.png").convert_alpha()
    elif lastlevel == 10:
        btlvl11vimg = pygame.image.load("sprite/lvl11n.png").convert_alpha()
    elif lastlevel > 10:
        btlvl11vimg = pygame.image.load("sprite/lvl11d.png").convert_alpha()
    btlvl11v = btlvl11vimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlvl11v = btlvl11v.move(100, 480) #Permet de le déplacer
    wdw.blit(btlvl11vimg, (100, 480))
    
    if lastlevel <= 10:
        btlvl12vimg = pygame.image.load("sprite/lvl12v.png").convert_alpha()
    elif lastlevel == 11:
        btlvl12vimg = pygame.image.load("sprite/lvl12n.png").convert_alpha()
    elif lastlevel > 11:
        btlvl12vimg = pygame.image.load("sprite/lvl12d.png").convert_alpha()
    btlvl12v = btlvl12vimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlvl12v = btlvl12v.move(400, 480) #Permet de le déplacer
    wdw.blit(btlvl12vimg, (400, 480))
    
    if lastlevel <= 11:
        btlvl13vimg = pygame.image.load("sprite/lvl13v.png").convert_alpha()
    elif lastlevel == 12:
        btlvl13vimg = pygame.image.load("sprite/lvl13n.png").convert_alpha()
    elif lastlevel > 12:
        btlvl13vimg = pygame.image.load("sprite/lvl13d.png").convert_alpha()
    btlvl13v = btlvl13vimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlvl13v = btlvl13v.move(700, 480) #Permet de le déplacer
    wdw.blit(btlvl13vimg, (700, 480))
    
    if lastlevel <= 12:
        btlvl14vimg = pygame.image.load("sprite/lvl14v.png").convert_alpha()
    elif lastlevel == 13:
        btlvl14vimg = pygame.image.load("sprite/lvl14n.png").convert_alpha()
    elif lastlevel > 13:
        btlvl14vimg = pygame.image.load("sprite/lvl14d.png").convert_alpha()
    btlvl14v = btlvl14vimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlvl14v = btlvl14v.move(1000, 480) #Permet de le déplacer
    wdw.blit(btlvl14vimg, (1000, 480))
    
    if lastlevel <= 13:
        btlvl15vimg = pygame.image.load("sprite/lvl15v.png").convert_alpha()
    elif lastlevel == 14:
        btlvl15vimg = pygame.image.load("sprite/lvl15n.png").convert_alpha()
    elif lastlevel > 14:
        btlvl15vimg = pygame.image.load("sprite/lvl15d.png").convert_alpha()
    btlvl15v = btlvl15vimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlvl15v = btlvl15v.move(1300, 480) #Permet de le déplacer
    wdw.blit(btlvl15vimg, (1300, 480))
    pygame.display.update()
    while continuer == True:
        for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        if btlvl1n.collidepoint(event.pos) and fenetre == 1 and lastlevel >=0 :
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(1, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(1)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlvl2v.collidepoint(event.pos) and fenetre == 1 and lastlevel >=1 or suivant == 1  and niveau == 2:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(2, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(2)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlvl3v.collidepoint(event.pos) and fenetre == 1 and lastlevel >=2 or suivant == 1  and niveau == 3:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(3, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(3)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlvl4v.collidepoint(event.pos) and fenetre == 1 and lastlevel >=3 or suivant == 1  and niveau == 4:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(4, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(4)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlvl5v.collidepoint(event.pos) and fenetre == 1 and lastlevel >=4 or suivant == 1  and niveau == 5:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(5, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(5)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlvl6v.collidepoint(event.pos) and fenetre == 1 and lastlevel >=5 or suivant == 1 and niveau == 6:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(6, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(6)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlvl7v.collidepoint(event.pos) and fenetre == 1 and lastlevel >=6 or suivant == 1 and niveau == 7:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(7, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(7)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlvl8v.collidepoint(event.pos) and fenetre == 1 and lastlevel >=7 or suivant == 1 and niveau == 8:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(8, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(8)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlvl9v.collidepoint(event.pos) and fenetre == 1 and lastlevel >=8 or suivant == 1 and niveau == 9:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(9, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(9)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlvl10v.collidepoint(event.pos) and fenetre == 1 and lastlevel >=9 or suivant == 1 and niveau == 10:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(10, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(10)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlvl11v.collidepoint(event.pos) and fenetre == 1 and lastlevel >=10 or suivant == 1 and niveau == 11:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(11, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(11)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlvl12v.collidepoint(event.pos) and fenetre == 1 and lastlevel >=11 or suivant == 1 and niveau == 12:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(12, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(12)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlvl13v.collidepoint(event.pos) and fenetre == 1 and lastlevel >=12 or suivant == 1 and niveau == 13:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(13, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(13)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlvl14v.collidepoint(event.pos) and fenetre == 1 and lastlevel >=13 or suivant == 1 and niveau == 14:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(14, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(14)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlvl15v.collidepoint(event.pos) and fenetre == 1 and lastlevel >=14 or suivant == 1 and niveau == 15:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(15, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(15)
                            if toutfini == 3:
                                menuprincipal()
                        if btback.collidepoint(event.pos) and fenetre == 1 or suivant == 1  and fenetre == 1:
                            fenetre = 0
                            menuprincipal()
                        if btsuite.collidepoint(event.pos) and fenetre == 1 or suivant == 1  and fenetre == 1:
                            fenetre = 1
                            menulevel2(fenetre)
                        #toutfini : Si = 1 : il a fini le niveau, si = 0 il ne l'a pas fini, si = 2 : il est mort
                        if toutfini == 1 and fenetre == 0:
                            time.sleep(1)
                            menuprincipal()
                        elif toutfini == 0 and fenetre == 0:
                            time.sleep(0.5)
                            menuprincipal()
                        elif toutfini == 2 and fenetre == 0:
                            time.sleep(0.5)
                            menuprincipal()
def menulevel2(fenetre):
    global lastlevel
    suivant = 0
    pygame.init()
    pygame.display.flip()
    # pour savoir de quel niveau il sort
    niveau = int
    # Pour savoir si quand il sort du niveau, il est fini
    toutfini = 0
    continuer = True
    fond = pygame.image.load("sprite/menu.png").convert_alpha()
    wdw.blit(fond, (0,0))
    font=pygame.font.Font(None, 24)

    btavantimg = pygame.image.load("sprite/return.png").convert_alpha()
    btavant = btavantimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btavant = btavant.move(100, 640) #Permet de le déplacer
    wdw.blit(btavantimg, (100, 640))
        
    btbackimg = pygame.image.load("sprite/menubuton.png").convert_alpha()
    btback = btbackimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btback = btback.move(1300, 640) #Permet de le déplacer
    wdw.blit(btbackimg, (1300, 640))
    
    if lastlevel <= 14:
        btlevel16img = pygame.image.load("sprite/lvl16v.png").convert_alpha()
    elif lastlevel == 15:
        btlevel16img = pygame.image.load("sprite/lvl16n.png").convert_alpha()
    elif lastlevel > 15:
        btlevel16img = pygame.image.load("sprite/lvl16d.png").convert_alpha()
    btlevel16 = btlevel16img.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlevel16 = btlevel16.move(100, 120) #Permet de le déplacer
    wdw.blit(btlevel16img, (100, 120))
    
    if lastlevel <= 15:
        btlevel17img = pygame.image.load("sprite/lvl17v.png").convert_alpha()
    elif lastlevel == 16:
        btlevel17img = pygame.image.load("sprite/lvl17n.png").convert_alpha()
    elif lastlevel > 16:
        btlevel17img = pygame.image.load("sprite/lvl17d.png").convert_alpha()
    btlevel17 = btlevel17img.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlevel17 = btlevel17.move(400, 120) #Permet de le déplacer
    wdw.blit(btlevel17img, (400, 120))
    
    if lastlevel <= 16:
        btlevel18img = pygame.image.load("sprite/lvl18v.png").convert_alpha()
    elif lastlevel == 17:
        btlevel18img = pygame.image.load("sprite/lvl18n.png").convert_alpha()
    elif lastlevel > 17:
        btlevel18img = pygame.image.load("sprite/lvl18d.png").convert_alpha()
    btlevel18 = btlevel18img.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlevel18 = btlevel18.move(700, 120) #Permet de le déplacer
    wdw.blit(btlevel18img, (700, 120))
    
    if lastlevel <= 17:
        btlevel19img = pygame.image.load("sprite/lvl19v.png").convert_alpha()
    elif lastlevel == 18:
        btlevel19img = pygame.image.load("sprite/lvl19n.png").convert_alpha()
    elif lastlevel > 18:
        btlevel19img = pygame.image.load("sprite/lvl19d.png").convert_alpha()
    btlevel19 = btlevel19img.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlevel19 = btlevel19.move(1000, 120) #Permet de le déplacer
    wdw.blit(btlevel19img, (1000, 120))
    
    if lastlevel <= 18:
        btlevel20img = pygame.image.load("sprite/lvl20v.png").convert_alpha()
    elif lastlevel == 19:
        btlevel20img = pygame.image.load("sprite/lvl20n.png").convert_alpha()
    elif lastlevel > 19:
        btlevel20img = pygame.image.load("sprite/lvl20d.png").convert_alpha()
    btlevel20 = btlevel20img.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlevel20 = btlevel20.move(1300, 120) #Permet de le déplacer
    wdw.blit(btlevel20img, (1300, 120))
    
    if lastlevel <= 19:
        btlevel21img = pygame.image.load("sprite/lvl21v.png").convert_alpha()
    elif lastlevel == 20:
        btlevel21img = pygame.image.load("sprite/lvl21n.png").convert_alpha()
    elif lastlevel > 20:
        btlevel21img = pygame.image.load("sprite/lvl21d.png").convert_alpha()
    btlevel21 = btlevel21img.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlevel21 = btlevel21.move(100, 300) #Permet de le déplacer
    wdw.blit(btlevel21img, (100, 300))
    
    if lastlevel <= 20:
        btlevel22img = pygame.image.load("sprite/lvl22v.png").convert_alpha()
    elif lastlevel == 21:
        btlevel22img = pygame.image.load("sprite/lvl22n.png").convert_alpha()
    elif lastlevel > 21:
        btlevel22img = pygame.image.load("sprite/lvl22d.png").convert_alpha()
    btlevel22 = btlevel22img.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlevel22 = btlevel22.move(400, 300) #Permet de le déplacer
    wdw.blit(btlevel22img, (400, 300))
    
    if lastlevel <= 21:
        btlevel23img = pygame.image.load("sprite/lvl23v.png").convert_alpha()
    elif lastlevel == 22:
        btlevel23img = pygame.image.load("sprite/lvl23n.png").convert_alpha()
    elif lastlevel > 22:
        btlevel23img = pygame.image.load("sprite/lvl23d.png").convert_alpha()
    btlevel23 = btlevel23img.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlevel23 = btlevel23.move(700, 300) #Permet de le déplacer
    wdw.blit(btlevel23img, (700, 300))
    
    if lastlevel <= 22:
        btlevel24img = pygame.image.load("sprite/lvl24v.png").convert_alpha()
    elif lastlevel == 23:
        btlevel24img = pygame.image.load("sprite/lvl24n.png").convert_alpha()
    elif lastlevel > 23:
        btlevel24img = pygame.image.load("sprite/lvl24d.png").convert_alpha()
    btlevel24 = btlevel24img.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlevel24 = btlevel24.move(1300, 300) #Permet de le déplacer
    wdw.blit(btlevel24img, (1000, 300))
    
    if lastlevel <= 23:
        btlevel25img = pygame.image.load("sprite/lvl25v.png").convert_alpha()
    elif lastlevel == 24:
        btlevel25img = pygame.image.load("sprite/lvl25n.png").convert_alpha()
    elif lastlevel > 24:
        btlevel25img = pygame.image.load("sprite/lvl25d.png").convert_alpha()
    btlevel25 = btlevel25img.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlevel25 = btlevel25.move(1300, 300) #Permet de le déplacer
    wdw.blit(btlevel25img, (1300, 300))
    
    if lastlevel <= 24:
        btlevel26img = pygame.image.load("sprite/lvl26v.png").convert_alpha()
    elif lastlevel == 25:
        btlevel26img = pygame.image.load("sprite/lvl26n.png").convert_alpha()
    elif lastlevel > 25:
        btlevel26img = pygame.image.load("sprite/lvl26d.png").convert_alpha()
    btlevel26 = btlevel26img.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlevel26 = btlevel26.move(100, 480) #Permet de le déplacer
    wdw.blit(btlevel26img, (100, 480))
    
    if lastlevel <= 25:
        btlevel27img = pygame.image.load("sprite/lvl27v.png").convert_alpha()
    elif lastlevel == 26:
        btlevel27img = pygame.image.load("sprite/lvl27n.png").convert_alpha()
    elif lastlevel > 26:
        btlevel27img = pygame.image.load("sprite/lvl27d.png").convert_alpha()
    btlevel27 = btlevel27img.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlevel27 = btlevel27.move(400, 480) #Permet de le déplacer
    wdw.blit(btlevel27img, (400, 480))
    
    if lastlevel <= 26:
        btlevel28img = pygame.image.load("sprite/lvl28v.png").convert_alpha()
    elif lastlevel == 27:
        btlevel28img = pygame.image.load("sprite/lvl28n.png").convert_alpha()
    elif lastlevel > 27:
        btlevel28img = pygame.image.load("sprite/lvl28d.png").convert_alpha()
    btlevel28 = btlevel28img.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlevel28 = btlevel28.move(700, 480) #Permet de le déplacer
    wdw.blit(btlevel28img, (700, 480))
    
    if lastlevel <= 27:
        btlevel29img = pygame.image.load("sprite/lvl29v.png").convert_alpha()
    elif lastlevel == 28:
        btlevel29img = pygame.image.load("sprite/lvl29n.png").convert_alpha()
    elif lastlevel > 28:
        btlevel29img = pygame.image.load("sprite/lvl29d.png").convert_alpha()
    btlevel29 = btlevel29img.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlevel29 = btlevel29.move(1000, 480) #Permet de le déplacer
    wdw.blit(btlevel29img, (1000, 480))
    
    if lastlevel <= 28:
        btlevel30img = pygame.image.load("sprite/lvl30v.png").convert_alpha()
    elif lastlevel == 29:
        btlevel30img = pygame.image.load("sprite/lvl30n.png").convert_alpha()
    elif lastlevel > 29:
        btlevel30img = pygame.image.load("sprite/lvl30d.png").convert_alpha()
    btlevel30 = btlevel30img.get_rect() #Pour que Rect représente avec précision l'image chargé
    btlevel30 = btlevel30.move(1300, 480) #Permet de le déplacer
    wdw.blit(btlevel30img, (1300, 480))
    
    pygame.display.update()
    while continuer == True:
        for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        if btlevel16.collidepoint(event.pos) and fenetre == 1 and lastlevel >=15 or suivant == 1 and niveau == 16:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(16, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(16)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlevel17.collidepoint(event.pos) and fenetre == 1 and lastlevel >=16 or suivant == 1 and niveau == 17:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(17, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(17)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlevel18.collidepoint(event.pos) and fenetre == 1 and lastlevel >=17 or suivant == 1 and niveau == 18:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(18, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(18)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlevel19.collidepoint(event.pos) and fenetre == 1 and lastlevel >=18 or suivant == 1 and niveau == 19:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(19, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(19)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlevel20.collidepoint(event.pos) and fenetre == 1 and lastlevel >=19 or suivant == 1 and niveau == 20:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(20, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(20)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlevel21.collidepoint(event.pos) and fenetre == 1 and lastlevel >=20 or suivant == 1 and niveau == 21:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(21, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(21)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlevel22.collidepoint(event.pos) and fenetre == 1 and lastlevel >=21 or suivant == 1 and niveau == 22:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(22, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(22)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlevel23.collidepoint(event.pos) and fenetre == 1 and lastlevel >=22 or suivant == 1 and niveau == 23:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(23, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(23)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlevel24.collidepoint(event.pos) and fenetre == 1 and lastlevel >=23 or suivant == 1 and niveau == 24:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(24, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(24)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlevel25.collidepoint(event.pos) and fenetre == 1 and lastlevel >=24 or suivant == 1 and niveau == 25:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(25, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(25)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlevel26.collidepoint(event.pos) and fenetre == 1 and lastlevel >=25 or suivant == 1 and niveau == 26:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(26, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(26)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlevel27.collidepoint(event.pos) and fenetre == 1 and lastlevel >=26 or suivant == 1 and niveau == 27:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(27, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(27)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlevel28.collidepoint(event.pos) and fenetre == 1 and lastlevel >=27 or suivant == 1 and niveau == 28:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(28, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(28)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlevel29.collidepoint(event.pos) and fenetre == 1 and lastlevel >=28 or suivant == 1 and niveau == 29:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(29, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(29)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if btlevel30.collidepoint(event.pos) and fenetre == 1 and lastlevel >=29 or suivant == 1 and niveau == 30:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(30, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini != 2 and toutfini != 0:
                                lastlevel = sayve.save(30)
                            if toutfini == 3:
                                menuprincipal()
                        if btback.collidepoint(event.pos) and fenetre == 1 or suivant == 1  and fenetre == 1:
                            fenetre = 0
                            menuprincipal()
                        if btavant.collidepoint(event.pos) and fenetre == 1 or suivant == 1  and fenetre == 1:
                            fenetre = 1
                            menulevel(fenetre)
                        #toutfini : Si = 1 : il a fini le niveau, si = 0 il ne l'a pas fini, si = 2 : il est mort
                        if toutfini == 1 and fenetre == 0:
                            time.sleep(1)
                            menuprincipal()
                        elif toutfini == 0 and fenetre == 0:
                            time.sleep(0.5)
                            menuprincipal()
                        elif toutfini == 2 and fenetre == 0:
                            time.sleep(0.5)
                            menuprincipal()

def menututoriel(fenetre):
    suivant = 0
    pygame.init()
    pygame.display.flip()
    # pour savoir de quel niveau il sort
    niveau = int
    # Pour savoir si quand il sort du niveau, il est fini
    toutfini = 0
    continuer = True
    fond = pygame.image.load("sprite/menu.png").convert_alpha()
    wdw.blit(fond, (0,0))
    font=pygame.font.Font(None, 24)
    
    aideimg = pygame.image.load("sprite/aide.png").convert_alpha()
    aide = aideimg.get_rect()
    aide = aide.move(500, 100)
    wdw.blit(aideimg, (500,100))
    texteclic = font.render("cliquez ici",1,(0,255,255))
    wdw.blit(texteclic, (550,90))
    
    btbackimg = pygame.image.load("sprite/menubuton.png").convert_alpha()
    btback = btbackimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    btback = btback.move(1300, 640) #Permet de le déplacer
    wdw.blit(btbackimg, (1300, 640))
    
    
    bttutoriel1nimg = pygame.image.load("sprite/lvl1n.png").convert_alpha()
    bttutoriel1n = bttutoriel1nimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    bttutoriel1n = bttutoriel1n.move(300, 390) #Permet de le déplacer
    wdw.blit(bttutoriel1nimg, (300, 390))
    
    bttutoriel2nimg = pygame.image.load("sprite/lvl2n.png").convert_alpha()
    bttutoriel2n = bttutoriel2nimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    bttutoriel2n = bttutoriel2n.move(700, 390) #Permet de le déplacer
    wdw.blit(bttutoriel2nimg, (700, 390))
    
    bttutoriel3nimg = pygame.image.load("sprite/lvl3n.png").convert_alpha()
    bttutoriel3n = bttutoriel3nimg.get_rect() #Pour que Rect représente avec précision l'image chargé
    bttutoriel3n = bttutoriel3n.move(1100, 390) #Permet de le déplacer
    wdw.blit(bttutoriel3nimg, (1100, 390))
    
    pygame.display.update()
    while continuer == True:
        for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        if bttutoriel1n.collidepoint(event.pos) and fenetre == 1 :
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(31, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if bttutoriel2n.collidepoint(event.pos) and fenetre == 1 or suivant == 1 and niveau == 32:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(32, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini == 3:
                                niveau += 1
                                suivant = 1
                        if bttutoriel3n.collidepoint(event.pos) and fenetre == 1 or suivant == 1 and niveau == 33:
                            fenetre = 0
                            suivant = 0
                            print("Dans menu level, avant niveau = {0}.".format(niveau))
                            niveau, toutfini = main.jeu(33, perso1, perso2, perso3, perso4)
                            print("Dans menu level, après niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                            while toutfini == 2:
                                niveau, toutfini = main.jeu(niveau, perso1, perso2, perso3, perso4)
                            if toutfini == 3:
                                menuprincipal()
                        if aide.collidepoint(event.pos):
                            print("test")
                            texteaide = font.render("Bienvenu sur \"Find The Way\" ! L'objectif de ce jeu est simple :",1,(0,0,0))
                            texteaide2 = font.render("Il faut déplacer un personnage afin d'atteindre un drapeau! ",1,(0,0,0))
                            texteaide3 = font.render("pour cela, appuyez sur vos touches directionnelles afin de vous déplacer. ",1,(0,0,0))
                            texteaide4 = font.render("Cependant, pour atteindre le drapeau il faut résoudre quelques casse-têtes... ",1,(0,0,0))
                            texteaide5 = font.render("De plus sur certains niveaux il y'a plusieurs façon de gagner et de perdre. Conseil : Evitez d'aller dans les trous... ",1,(0,0,0))
                            wdw.blit(texteaide, (700,150))
                            wdw.blit(texteaide2, (700,175))
                            wdw.blit(texteaide3, (700,190))
                            wdw.blit(texteaide4, (700,205))
                            wdw.blit(texteaide5, (700,220))
                            textetuto1 = font.render("Tutoriel 1 : Dans ce niveau vous devez atteindre le drapeau dans un labyrinthe. ",1,(0,0,0))
                            wdw.blit(textetuto1, (300,490))
                            textetuto2 = font.render("Tutoriel 2 : Dans ce niveau vous allez devoir pousser des pierres dans des trous afin de vous donner accès au drapeau. ",1,(0,0,0))
                            wdw.blit(textetuto2, (300,515))
                            textetuto22 = font.render("N'oubliez pas que vous pouvez déplacer plusieurs pierres en même temps et que les pierres peuvent passer sur les trous bouchés.",1,(0,0,0))
                            wdw.blit(textetuto22, (300,530))
                            textetuto3 = font.render("Tutoriel 3 : Dans ce dernier niveau, vous allez combiner déplacement, pierres et trous ainsi que des boutons! ",1,(0,0,0))
                            wdw.blit(textetuto3, (300,555))
                            textetuto33 = font.render("Les boutons vont vous permettre de casser des barvricades et de vous libérer le chemin. ",1,(0,0,0))
                            wdw.blit(textetuto33, (300,570))
                            pygame.display.update()
                            
                        if btback.collidepoint(event.pos) and fenetre == 1 or suivant == 1  and fenetre == 1:
                            fenetre = 0
                            menuprincipal()
                        #toutfini : Si = 1 : il a fini le niveau, si = 0 il ne l'a pas fini, si = 2 : il est mort
                        if toutfini == 1 and fenetre == 0:
                            time.sleep(1)
                            menuprincipal()
                        elif toutfini == 0 and fenetre == 0:
                            time.sleep(0.5)
                            menuprincipal()
                        elif toutfini == 2 and fenetre == 0:
                            time.sleep(0.5)
                            menuprincipal()
def credits(fenetre):
    fond = pygame.image.load("sprite/credits.png").convert_alpha()
    wdw.blit(fond, (0,0))
    pygame.display.set_caption("Find The Way")
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE :
                    fenetre = 0
                    menuprincipal()
#pour que menuprincipal() ne ce lance pas quand on importe le fichier

def menuperso(fenetre):
    global perso2
    global perso1
    global perso4
    global perso3
    pygame.init()
    pygame.display.flip()
    fond = pygame.image.load("sprite/menu.png")
    
    wdw.blit(fond, (0,0))
    
    Pwhite = pygame.image.load("sprite/persoDown.png").convert_alpha()
    btPwhite = Pwhite.get_rect() 
    btPwhite = btPwhite.move(320, 500) 
    wdw.blit(Pwhite, (320, 500))
    
    Pred = pygame.image.load("sprite/persoDownBlue.png").convert_alpha()
    btPred = Pred.get_rect() 
    btPred = btPred.move(640, 500) 
    wdw.blit(Pred, (640, 500))
    
    Pblue = pygame.image.load("sprite/persoDownRed.png").convert_alpha()
    btPblue = Pblue.get_rect() 
    btPblue = btPblue.move(960, 500) 
    wdw.blit(Pblue, (960, 500))
    
    Pgreen = pygame.image.load("sprite/persoDownGreen.png").convert_alpha()
    btPgreen = Pgreen.get_rect() 
    btPgreen = btPgreen.move(1280, 500) 
    wdw.blit(Pgreen, (1280, 500))
    
    Phat = pygame.image.load("sprite/persoDownHat.png").convert_alpha()
    btPhat = Phat.get_rect() 
    btPhat = btPhat.move(640, 300) 
    wdw.blit(Phat, (640, 300))
    
    Pme = pygame.image.load("sprite/persoDownMe.png").convert_alpha()
    btPme = Pme.get_rect() 
    btPme = btPme.move(960, 300) 
    wdw.blit(Pme, (960, 300))
    
    Phappy = pygame.image.load("sprite/persoDownHappy.png").convert_alpha()
    btPhappy = Phappy.get_rect() 
    btPhappy = btPhappy.move(1280, 300) 
    wdw.blit(Phappy, (1280, 300))
    
    Pshirt = pygame.image.load("sprite/persoDownShirt.png").convert_alpha()
    btPshirt = Pshirt.get_rect() 
    btPshirt = btPshirt.move(320, 300) 
    wdw.blit(Pshirt, (320, 300))

    btbackimg = pygame.image.load("sprite/menubuton.png").convert_alpha()
    btback = btbackimg.get_rect()
    btback = btback.move(1300, 640)
    wdw.blit(btbackimg, (1300, 640))
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE :
                    fenetre = 0
                    menuprincipal()
            if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if btPwhite.collidepoint(event.pos):
                            perso2 = pygame.image.load("sprite/persoUp.png").convert_alpha()
                            perso1 = pygame.image.load("sprite/persoDown.png").convert_alpha()
                            perso4 = pygame.image.load("sprite/persoRight.png").convert_alpha()
                            perso3 = pygame.image.load("sprite/persoLeft.png").convert_alpha()
                            menuprincipal()
                        if btPred.collidepoint(event.pos):
                            perso2 = pygame.image.load("sprite/persoUpBlue.png").convert_alpha()
                            perso1 = pygame.image.load("sprite/persoDownBlue.png").convert_alpha()
                            perso4 = pygame.image.load("sprite/persoRightBlue.png").convert_alpha()
                            perso3 = pygame.image.load("sprite/persoLeftBlue.png").convert_alpha()
                            menuprincipal()
                        if btPblue.collidepoint(event.pos):
                            perso2 = pygame.image.load("sprite/persoUpRed.png").convert_alpha()
                            perso1 = pygame.image.load("sprite/persoDownRed.png").convert_alpha()
                            perso4 = pygame.image.load("sprite/persoRightRed.png").convert_alpha()
                            perso3 = pygame.image.load("sprite/persoLeftRed.png").convert_alpha()
                            menuprincipal()
                        if btPgreen.collidepoint(event.pos):
                            perso2 = pygame.image.load("sprite/persoUpGreen.png").convert_alpha()
                            perso1 = pygame.image.load("sprite/persoDownGreen.png").convert_alpha()
                            perso4 = pygame.image.load("sprite/persoRightGreen.png").convert_alpha()
                            perso3 = pygame.image.load("sprite/persoLeftGreen.png").convert_alpha()
                            menuprincipal()                            
                        if btPhat.collidepoint(event.pos):
                            perso2 = pygame.image.load("sprite/persoUpHat.png").convert_alpha()
                            perso1 = pygame.image.load("sprite/persoDownHat.png").convert_alpha()
                            perso4 = pygame.image.load("sprite/persoRightHat.png").convert_alpha()
                            perso3 = pygame.image.load("sprite/persoLeftHat.png").convert_alpha()
                            menuprincipal()
                        if btPme.collidepoint(event.pos):
                            perso2 = pygame.image.load("sprite/persoUpMe.png").convert_alpha()
                            perso1 = pygame.image.load("sprite/persoDownMe.png").convert_alpha()
                            perso4 = pygame.image.load("sprite/persoRightMe.png").convert_alpha()
                            perso3 = pygame.image.load("sprite/persoLeftMe.png").convert_alpha()
                            menuprincipal()
                        if btPhappy.collidepoint(event.pos):
                            perso2 = pygame.image.load("sprite/persoUpHappy.png").convert_alpha()
                            perso1 = pygame.image.load("sprite/persoDownHappy.png").convert_alpha()
                            perso4 = pygame.image.load("sprite/persoRightHappy.png").convert_alpha()
                            perso3 = pygame.image.load("sprite/persoLeftHappy.png").convert_alpha()
                            menuprincipal()
                        if btPshirt.collidepoint(event.pos):
                            perso2 = pygame.image.load("sprite/persoUpShirt.png").convert_alpha()
                            perso1 = pygame.image.load("sprite/persoDownShirt.png").convert_alpha()
                            perso4 = pygame.image.load("sprite/persoRightShirt.png").convert_alpha()
                            perso3 = pygame.image.load("sprite/persoLeftShirt.png").convert_alpha()
                            menuprincipal()

                            
                        if btback.collidepoint(event.pos):
                            menuprincipal()
                            
                            
    
    
    
    


if __name__ == '__main__':
    menuprincipal()
