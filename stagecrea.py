import pygame
from numpy import *
import Refreshstagecrea
from menu import *
import sayve
from onfaitduson import *
from maincreaction import *
def creation(perso1, perso2, perso3, perso4):
	bandeson(-1)
	pygame.init()
	wdw=pygame.display.set_mode((1600,880))
	mur = pygame.image.load("sprite/pimpmymur.png").convert_alpha()
	sol = pygame.image.load("sprite/pimpmysol.png").convert_alpha()
	flag = pygame.image.load("sprite/pimpmyflag.png").convert_alpha()
	rock = pygame.image.load("sprite/pimpmycaillou.png").convert_alpha()
	spike = pygame.image.load("sprite/pimpmypiques.png").convert_alpha()
	cdtrou = pygame.image.load("sprite/pimpmycailloudanstrou.png").convert_alpha()
	door = pygame.image.load("sprite/pimpmydoor.png").convert_alpha()
	buton = pygame.image.load("sprite/pimpmybouton.png").convert_alpha()
	vide = pygame.image.load("sprite/r.png").convert_alpha()
	petitfond = pygame.image.load("sprite/milieu.png").convert_alpha()
	fond = pygame.image.load("sprite/menu.png").convert_alpha()
	tester = pygame.image.load("sprite/tester.png").convert_alpha()
	menu = pygame.image.load("sprite/menubuton.png").convert_alpha()
	door2 = pygame.image.load("sprite/pimpmydoor.png").convert_alpha()
	buton2 = pygame.image.load("sprite/pimpmybouton.png").convert_alpha()

	toutfini = 0
	bloc = 11

	hitbox1 = door.get_rect().move(260,160)
	hitbox2 = door.get_rect().move(320,160)
	hitbox3 = door.get_rect().move(380,160)
	hitbox4 = door.get_rect().move(440,160)
	hitbox5 = door.get_rect().move(500,160)
	hitbox6 = door.get_rect().move(560,160)
	hitbox7 = door.get_rect().move(620,160)
	hitbox8 = door.get_rect().move(680,160)
	hitbox9 = door.get_rect().move(740,160)
	hitbox10 = door.get_rect().move(800,160)
	hitbox11 = door.get_rect().move(860,160)
	hitbox12 = door.get_rect().move(920,160)
	hitbox13 = door.get_rect().move(980,160)
	hitbox14 = door.get_rect().move(1040,160)
	hitbox15 = door.get_rect().move(1100,160)
	hitbox16 = door.get_rect().move(1160,160)
	hitbox17 = door.get_rect().move(1220,160)
	hitbox18 = door.get_rect().move(1280,160)

	hitbox19 = door.get_rect().move(260,220)
	hitbox20 = door.get_rect().move(320,220)
	hitbox21 = door.get_rect().move(380,220)
	hitbox22 = door.get_rect().move(440,220)
	hitbox23 = door.get_rect().move(500,220)
	hitbox24 = door.get_rect().move(560,220)
	hitbox25 = door.get_rect().move(620,220)
	hitbox26 = door.get_rect().move(680,220)
	hitbox27 = door.get_rect().move(740,220)
	hitbox28 = door.get_rect().move(800,220)
	hitbox29 = door.get_rect().move(860,220)
	hitbox30 = door.get_rect().move(920,220)
	hitbox31 = door.get_rect().move(980,220)
	hitbox32 = door.get_rect().move(1040,220)
	hitbox33 = door.get_rect().move(1100,220)
	hitbox34 = door.get_rect().move(1160,220)
	hitbox35 = door.get_rect().move(1240,220)
	hitbox36 = door.get_rect().move(1280,220)

	hitbox37 = door.get_rect().move(260,280)
	hitbox38 = door.get_rect().move(320,280)
	hitbox39 = door.get_rect().move(380,280)
	hitbox40 = door.get_rect().move(440,280)
	hitbox41 = door.get_rect().move(500,280)
	hitbox42 = door.get_rect().move(560,280)
	hitbox43 = door.get_rect().move(620,280)
	hitbox44 = door.get_rect().move(680,280)
	hitbox45 = door.get_rect().move(740,280)
	hitbox46 = door.get_rect().move(800,280)
	hitbox47 = door.get_rect().move(860,280)
	hitbox48 = door.get_rect().move(920,280)
	hitbox49 = door.get_rect().move(980,280)
	hitbox50 = door.get_rect().move(1040,280)
	hitbox51 = door.get_rect().move(1100,280)
	hitbox52 = door.get_rect().move(1160,280)
	hitbox53 = door.get_rect().move(1220,280)
	hitbox54 = door.get_rect().move(1280,280)

	hitbox55 = door.get_rect().move(260,340)
	hitbox56 = door.get_rect().move(320,340)
	hitbox57 = door.get_rect().move(380,340)
	hitbox58 = door.get_rect().move(440,340)
	hitbox59 = door.get_rect().move(500,340)
	hitbox60 = door.get_rect().move(560,340)
	hitbox61 = door.get_rect().move(620,340)
	hitbox62 = door.get_rect().move(680,340)
	hitbox63 = door.get_rect().move(740,340)
	hitbox64 = door.get_rect().move(800,340)
	hitbox65 = door.get_rect().move(860,340)
	hitbox66 = door.get_rect().move(920,340)
	hitbox67 = door.get_rect().move(980,340)
	hitbox68 = door.get_rect().move(1040,340)
	hitbox69 = door.get_rect().move(1100,340)
	hitbox70 = door.get_rect().move(1160,340)
	hitbox71 = door.get_rect().move(1240,340)
	hitbox72 = door.get_rect().move(1280,340)

	hitbox73 = door.get_rect().move(260,400)
	hitbox74 = door.get_rect().move(320,400)
	hitbox75 = door.get_rect().move(380,400)
	hitbox76 = door.get_rect().move(440,400)
	hitbox77 = door.get_rect().move(500,400)
	hitbox78 = door.get_rect().move(560,400)
	hitbox79 = door.get_rect().move(620,400)
	hitbox80 = door.get_rect().move(680,400)
	hitbox81 = door.get_rect().move(740,400)
	hitbox82 = door.get_rect().move(800,400)
	hitbox83 = door.get_rect().move(860,400)
	hitbox84 = door.get_rect().move(920,400)
	hitbox85 = door.get_rect().move(980,400)
	hitbox86 = door.get_rect().move(1040,400)
	hitbox87 = door.get_rect().move(1100,400)
	hitbox88 = door.get_rect().move(1160,400)
	hitbox89 = door.get_rect().move(1220,400)
	hitbox90 = door.get_rect().move(1280,400)

	hitbox91 = door.get_rect().move(260,460)
	hitbox92 = door.get_rect().move(320,460)
	hitbox93 = door.get_rect().move(380,460)
	hitbox94 = door.get_rect().move(440,460)
	hitbox95 = door.get_rect().move(500,460)
	hitbox96 = door.get_rect().move(560,460)
	hitbox97 = door.get_rect().move(620,460)
	hitbox98 = door.get_rect().move(680,460)
	hitbox99 = door.get_rect().move(740,460)
	hitbox100 = door.get_rect().move(800,460)
	hitbox101 = door.get_rect().move(860,460)
	hitbox102 = door.get_rect().move(920,460)
	hitbox103 = door.get_rect().move(980,460)
	hitbox104 = door.get_rect().move(1040,460)
	hitbox105 = door.get_rect().move(1100,460)
	hitbox106 = door.get_rect().move(1160,460)
	hitbox107 = door.get_rect().move(1220,460)
	hitbox108 = door.get_rect().move(1280,460)

	hitbox109 = door.get_rect().move(260,520)
	hitbox110 = door.get_rect().move(320,520)
	hitbox111 = door.get_rect().move(380,520)
	hitbox112 = door.get_rect().move(440,520)
	hitbox113 = door.get_rect().move(500,520)
	hitbox114 = door.get_rect().move(560,520)
	hitbox115 = door.get_rect().move(620,520)
	hitbox116 = door.get_rect().move(680,520)
	hitbox117 = door.get_rect().move(740,520)
	hitbox118 = door.get_rect().move(800,520)
	hitbox119 = door.get_rect().move(860,520)
	hitbox120 = door.get_rect().move(920,520)
	hitbox121 = door.get_rect().move(980,520)
	hitbox122 = door.get_rect().move(1040,520)
	hitbox123 = door.get_rect().move(1100,520)
	hitbox124 = door.get_rect().move(1160,520)
	hitbox125 = door.get_rect().move(1220,520)
	hitbox126 = door.get_rect().move(1280,520)

	hitbox127 = door.get_rect().move(260,580)
	hitbox128 = door.get_rect().move(320,580)
	hitbox129 = door.get_rect().move(380,580)
	hitbox130 = door.get_rect().move(440,580)
	hitbox131 = door.get_rect().move(500,580)
	hitbox132 = door.get_rect().move(560,580)
	hitbox133 = door.get_rect().move(620,580)
	hitbox134 = door.get_rect().move(680,580)
	hitbox135 = door.get_rect().move(740,580)
	hitbox136 = door.get_rect().move(800,580)
	hitbox137 = door.get_rect().move(860,580)
	hitbox138 = door.get_rect().move(920,580)
	hitbox139 = door.get_rect().move(980,580)
	hitbox140 = door.get_rect().move(1040,580)
	hitbox141 = door.get_rect().move(1100,580)
	hitbox142 = door.get_rect().move(1160,580)
	hitbox143 = door.get_rect().move(1220,580)
	hitbox144 = door.get_rect().move(1280,580)

	hitbox145 = door.get_rect().move(260,640)
	hitbox146 = door.get_rect().move(320,640)
	hitbox147 = door.get_rect().move(380,640)
	hitbox148 = door.get_rect().move(440,640)
	hitbox149 = door.get_rect().move(500,640)
	hitbox150 = door.get_rect().move(560,640)
	hitbox151 = door.get_rect().move(620,640)
	hitbox152 = door.get_rect().move(680,640)
	hitbox153 = door.get_rect().move(740,640)
	hitbox154 = door.get_rect().move(800,640)
	hitbox155 = door.get_rect().move(860,640)
	hitbox156 = door.get_rect().move(920,640)
	hitbox157 = door.get_rect().move(980,640)
	hitbox158 = door.get_rect().move(1040,640)
	hitbox159 = door.get_rect().move(1100,640)
	hitbox160 = door.get_rect().move(1160,640)
	hitbox161 = door.get_rect().move(1220,640)
	hitbox162 = door.get_rect().move(1280,640)

	salle=zeros((11, 20))
	salle[0] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
	salle[1] = [1,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,1]
	salle[2] = [1,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,1]
	salle[3] = [1,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,1]
	salle[4] = [1,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,1]
	salle[5] = [1,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,1]
	salle[6] = [1,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,1]
	salle[7] = [1,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,1]
	salle[8] = [1,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,1]
	salle[9] = [1,0,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,1]
	salle[10]= [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]



	wdw.blit(fond, (0,0))
	wdw.blit(petitfond,(200,100))

	btmenu = menu.get_rect()
	btmenu = btmenu.move(1390,0)
	wdw.blit(menu, (1390,0))

	bttester = tester.get_rect()
	bttester = bttester.move(1390,760)
	wdw.blit(tester, (1390,760))

	btmur = mur.get_rect() #Pour que Rect représente avec précision l'image chargé
	btmur = btmur.move(25, 40) #Permet de le déplacer
	wdw.blit(mur, (25, 40))

	btsol = sol.get_rect() #Pour que Rect représente avec précision l'image chargé
	btsol = btsol.move(25, 160) #Permet de le déplacer
	wdw.blit(sol, (25, 160))

	btflag = flag.get_rect() #Pour que Rect représente avec précision l'image chargé
	btflag = btflag.move(25, 280) #Permet de le déplacer
	wdw.blit(flag, (25, 280))

	btrock = rock.get_rect() #Pour que Rect représente avec précision l'image chargé
	btrock = btrock.move(25, 400) #Permet de le déplacer
	wdw.blit(rock, (25, 400))

	btspike = spike.get_rect() #Pour que Rect représente avec précision l'image chargé
	btspike = btspike.move(25, 520) #Permet de le déplacer
	wdw.blit(spike, (25, 520))

	btcdtrou = cdtrou.get_rect() #Pour que Rect représente avec précision l'image chargé
	btcdtrou = btcdtrou.move(25, 640) #Permet de le déplacer
	wdw.blit(cdtrou, (25, 640))

	btdoor = door.get_rect() #Pour que Rect représente avec précision l'image chargé
	btdoor = btdoor.move(1420, 200) #Permet de le déplacer
	wdw.blit(door, (1420, 200))

	btbuton = buton.get_rect() #Pour que Rect représente avec précision l'image chargé
	btbuton = btbuton.move(1515, 200) #Permet de le déplacer
	wdw.blit(buton, (1515, 200))

	btdoor1 = door.get_rect() #Pour que Rect représente avec précision l'image chargé
	btdoor1 = btdoor1.move(1420, 400) #Permet de le déplacer
	wdw.blit(door, (1420, 400))

	btbuton1 = buton.get_rect() #Pour que Rect représente avec précision l'image chargé
	btbuton1 = btbuton1.move(1515, 400) #Permet de le déplacer
	wdw.blit(buton, (1515, 400))

	pygame.display.update()
	Refreshstagecrea.refresh(salle,sol,mur,rock,spike,flag,cdtrou,buton,door,buton2,door2,vide)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE :
					print("\nSTOP")
					pygame.quit()
					quit()
			if event.type == MOUSEBUTTONUP:
				if event.button == 1:
					if btmenu.collidepoint(event.pos):
						menuprincipal()
					if bttester.collidepoint(event.pos):
						for x in range(0 ,11):
							for y in range(0, 20):
								if salle[x,y] == 11:
									salle[x,y] = 0
						toutfini = 2
						pnl = 1
						while toutfini == 2:
							print("Salle avant sauvegarde :", salle)
							salle = sayve.savve(pnl, salle)
							toutfini = jeu(salle, perso1, perso2, perso3, perso4)
							pnl = 0
						if toutfini == 0 or toutfini == 1:
							menuprincipal()
						if toutfini == 3:
							creation(perso1, perso2, perso3, perso4)
					if btsol.collidepoint(event.pos):
						bloc = 0
					if btmur.collidepoint(event.pos):
						bloc = 1
					if btrock.collidepoint(event.pos):
						bloc = 2
					if btflag.collidepoint(event.pos):
						bloc = 3
					if btspike.collidepoint(event.pos):
						bloc = 4
					if btcdtrou.collidepoint(event.pos):
						bloc = 5
					if btbuton.collidepoint(event.pos):
						bloc = 6
					if btdoor.collidepoint(event.pos):
						bloc = 7
					if btbuton1.collidepoint(event.pos):
						bloc = 9
					if btdoor1.collidepoint(event.pos):
						bloc = 10
					if hitbox1.collidepoint(event.pos):
						salle[1,1] = bloc
					if hitbox2.collidepoint(event.pos):
						salle[1, 2] = bloc
					if hitbox3.collidepoint(event.pos):
						salle[1, 3] = bloc
					if hitbox4.collidepoint(event.pos):
						salle[1, 4] = bloc
					if hitbox5.collidepoint(event.pos):
						salle[1, 5] = bloc
					if hitbox6.collidepoint(event.pos):
						salle[1, 6] = bloc
					if hitbox7.collidepoint(event.pos):
						salle[1, 7] = bloc
					if hitbox8.collidepoint(event.pos):
						salle[1, 8] = bloc
					if hitbox9.collidepoint(event.pos):
						salle[1, 9] = bloc
					if hitbox10.collidepoint(event.pos):
						salle[1, 10] = bloc
					if hitbox11.collidepoint(event.pos):
						salle[1,11] = bloc
					if hitbox12.collidepoint(event.pos):
						salle[1, 12] = bloc
					if hitbox13.collidepoint(event.pos):
						salle[1, 13] = bloc
					if hitbox14.collidepoint(event.pos):
						salle[1, 14] = bloc
					if hitbox15.collidepoint(event.pos):
						salle[1, 15] = bloc
					if hitbox16.collidepoint(event.pos):
						salle[1, 16] = bloc
					if hitbox17.collidepoint(event.pos):
						salle[1, 17] = bloc
					if hitbox18.collidepoint(event.pos):
						salle[1, 18] = bloc
					if hitbox19.collidepoint(event.pos):
						salle[2, 1] = bloc
					if hitbox20.collidepoint(event.pos):
						salle[2, 2] = bloc
					if hitbox21.collidepoint(event.pos):
						salle[2,3] = bloc
					if hitbox22.collidepoint(event.pos):
						salle[2, 4] = bloc
					if hitbox23.collidepoint(event.pos):
						salle[2, 5] = bloc
					if hitbox24.collidepoint(event.pos):
						salle[2, 6] = bloc
					if hitbox25.collidepoint(event.pos):
						salle[2, 7] = bloc
					if hitbox26.collidepoint(event.pos):
						salle[2, 8] = bloc
					if hitbox27.collidepoint(event.pos):
						salle[2, 9] = bloc
					if hitbox28.collidepoint(event.pos):
						salle[2, 10] = bloc
					if hitbox29.collidepoint(event.pos):
						salle[2, 11] = bloc
					if hitbox30.collidepoint(event.pos):
						salle[2, 12] = bloc
					if hitbox31.collidepoint(event.pos):
						salle[2,13] = bloc
					if hitbox32.collidepoint(event.pos):
						salle[2, 14] = bloc
					if hitbox33.collidepoint(event.pos):
						salle[2, 15] = bloc
					if hitbox34.collidepoint(event.pos):
						salle[2, 16] = bloc
					if hitbox35.collidepoint(event.pos):
						salle[2, 17] = bloc
					if hitbox36.collidepoint(event.pos):
						salle[2, 18] = bloc
					if hitbox37.collidepoint(event.pos):
						salle[3, 1] = bloc
					if hitbox38.collidepoint(event.pos):
						salle[3, 2] = bloc
					if hitbox39.collidepoint(event.pos):
						salle[3, 3] = bloc
					if hitbox40.collidepoint(event.pos):
						salle[3,4] = bloc	
					if hitbox41.collidepoint(event.pos):
						salle[3,5] = bloc
					if hitbox42.collidepoint(event.pos):
						salle[3, 6] = bloc
					if hitbox43.collidepoint(event.pos):
						salle[3, 7] = bloc
					if hitbox44.collidepoint(event.pos):
						salle[3, 8] = bloc
					if hitbox45.collidepoint(event.pos):
						salle[3, 9] = bloc
					if hitbox46.collidepoint(event.pos):
						salle[3, 10] = bloc
					if hitbox47.collidepoint(event.pos):
						salle[3, 11] = bloc
					if hitbox48.collidepoint(event.pos):
						salle[3, 12] = bloc
					if hitbox49.collidepoint(event.pos):
						salle[3, 13] = bloc
					if hitbox50.collidepoint(event.pos):
						salle[3, 14] = bloc
					if hitbox51.collidepoint(event.pos):
						salle[3,15] = bloc
					if hitbox52.collidepoint(event.pos):
						salle[3, 16] = bloc
					if hitbox53.collidepoint(event.pos):
						salle[3, 17] = bloc
					if hitbox54.collidepoint(event.pos):
						salle[3, 18] = bloc
					if hitbox55.collidepoint(event.pos):
						salle[4, 1] = bloc
					if hitbox56.collidepoint(event.pos):
						salle[4, 2] = bloc
					if hitbox57.collidepoint(event.pos):
						salle[4, 3] = bloc
					if hitbox58.collidepoint(event.pos):
						salle[4, 4] = bloc
					if hitbox59.collidepoint(event.pos):
						salle[4, 5] = bloc
					if hitbox60.collidepoint(event.pos):
						salle[4, 6] = bloc
					if hitbox61.collidepoint(event.pos):
						salle[4,7] = bloc
					if hitbox62.collidepoint(event.pos):
						salle[4, 8] = bloc
					if hitbox63.collidepoint(event.pos):
						salle[4, 9] = bloc
					if hitbox64.collidepoint(event.pos):
						salle[4, 10] = bloc
					if hitbox65.collidepoint(event.pos):
						salle[4, 11] = bloc
					if hitbox66.collidepoint(event.pos):
						salle[4, 12] = bloc
					if hitbox67.collidepoint(event.pos):
						salle[4, 13] = bloc
					if hitbox68.collidepoint(event.pos):
						salle[4, 14] = bloc
					if hitbox69.collidepoint(event.pos):
						salle[4, 15] = bloc
					if hitbox70.collidepoint(event.pos):
						salle[4, 16] = bloc
					if hitbox71.collidepoint(event.pos):
						salle[4,17] = bloc
					if hitbox72.collidepoint(event.pos):
						salle[4, 18] = bloc
					if hitbox73.collidepoint(event.pos):
						salle[5, 1] = bloc
					if hitbox74.collidepoint(event.pos):
						salle[5, 2] = bloc
					if hitbox75.collidepoint(event.pos):
						salle[5, 3] = bloc
					if hitbox76.collidepoint(event.pos):
						salle[5, 4] = bloc
					if hitbox77.collidepoint(event.pos):
						salle[5, 5] = bloc
					if hitbox78.collidepoint(event.pos):
						salle[5, 6] = bloc
					if hitbox79.collidepoint(event.pos):
						salle[5, 7] = bloc
					if hitbox80.collidepoint(event.pos):
						salle[5, 8] = bloc
					if hitbox81.collidepoint(event.pos):
						salle[5, 9] = bloc
					if hitbox82.collidepoint(event.pos):
						salle[5, 10] = bloc
					if hitbox83.collidepoint(event.pos):
						salle[5, 11] = bloc
					if hitbox84.collidepoint(event.pos):
						salle[5, 12] = bloc
					if hitbox85.collidepoint(event.pos):
						salle[5, 13] = bloc
					if hitbox86.collidepoint(event.pos):
						salle[5, 14] = bloc
					if hitbox87.collidepoint(event.pos):
						salle[5, 15] = bloc
					if hitbox88.collidepoint(event.pos):
						salle[5, 16] = bloc
					if hitbox89.collidepoint(event.pos):
						salle[5, 17] = bloc
					if hitbox90.collidepoint(event.pos):
						salle[5, 18] = bloc
					if hitbox91.collidepoint(event.pos):
						salle[6,1] = bloc
					if hitbox92.collidepoint(event.pos):
						salle[6, 2] = bloc
					if hitbox93.collidepoint(event.pos):
						salle[6, 3] = bloc
					if hitbox94.collidepoint(event.pos):
						salle[6, 4] = bloc
					if hitbox95.collidepoint(event.pos):
						salle[6, 5] = bloc
					if hitbox96.collidepoint(event.pos):
						salle[6, 6] = bloc
					if hitbox97.collidepoint(event.pos):
						salle[6, 7] = bloc
					if hitbox98.collidepoint(event.pos):
						salle[6, 8] = bloc
					if hitbox99.collidepoint(event.pos):
						salle[6, 9] = bloc
					if hitbox100.collidepoint(event.pos):
						salle[6, 10] = bloc
					if hitbox101.collidepoint(event.pos):
						salle[6,11] = bloc
					if hitbox102.collidepoint(event.pos):
						salle[6, 12] = bloc
					if hitbox103.collidepoint(event.pos):
						salle[6, 13] = bloc
					if hitbox104.collidepoint(event.pos):
						salle[6, 14] = bloc
					if hitbox105.collidepoint(event.pos):
						salle[6, 15] = bloc
					if hitbox106.collidepoint(event.pos):
						salle[6, 16] = bloc
					if hitbox107.collidepoint(event.pos):
						salle[6, 17] = bloc
					if hitbox108.collidepoint(event.pos):
						salle[6, 18] = bloc
					if hitbox109.collidepoint(event.pos):
						salle[7, 1] = bloc
					if hitbox110.collidepoint(event.pos):
						salle[7, 2] = bloc
					if hitbox111.collidepoint(event.pos):
						salle[7,3] = bloc
					if hitbox112.collidepoint(event.pos):
						salle[7, 4] = bloc
					if hitbox113.collidepoint(event.pos):
						salle[7, 5] = bloc
					if hitbox114.collidepoint(event.pos):
						salle[7, 6] = bloc
					if hitbox115.collidepoint(event.pos):
						salle[7, 7] = bloc
					if hitbox116.collidepoint(event.pos):
						salle[7, 8] = bloc
					if hitbox117.collidepoint(event.pos):
						salle[7, 9] = bloc
					if hitbox118.collidepoint(event.pos):
						salle[7, 10] = bloc
					if hitbox119.collidepoint(event.pos):
						salle[7, 11] = bloc
					if hitbox120.collidepoint(event.pos):
						salle[7,12] = bloc	
					if hitbox121.collidepoint(event.pos):
						salle[7,13] = bloc
					if hitbox122.collidepoint(event.pos):
						salle[7, 14] = bloc
					if hitbox123.collidepoint(event.pos):
						salle[7, 15] = bloc
					if hitbox124.collidepoint(event.pos):
						salle[7, 16] = bloc
					if hitbox125.collidepoint(event.pos):
						salle[7, 17] = bloc
					if hitbox126.collidepoint(event.pos):
						salle[7, 18] = bloc
					if hitbox127.collidepoint(event.pos):
						salle[8, 1] = bloc
					if hitbox128.collidepoint(event.pos):
						salle[8, 2] = bloc
					if hitbox129.collidepoint(event.pos):
						salle[8, 3] = bloc
					if hitbox130.collidepoint(event.pos):
						salle[8, 4] = bloc
					if hitbox131.collidepoint(event.pos):
						salle[8,5] = bloc
					if hitbox132.collidepoint(event.pos):
						salle[8, 6] = bloc
					if hitbox133.collidepoint(event.pos):
						salle[8, 7] = bloc
					if hitbox134.collidepoint(event.pos):
						salle[8, 8] = bloc
					if hitbox135.collidepoint(event.pos):
						salle[8, 9] = bloc
					if hitbox136.collidepoint(event.pos):
						salle[8, 10] = bloc
					if hitbox137.collidepoint(event.pos):
						salle[8, 11] = bloc
					if hitbox138.collidepoint(event.pos):
						salle[8, 12] = bloc
					if hitbox139.collidepoint(event.pos):
						salle[8, 13] = bloc
					if hitbox140.collidepoint(event.pos):
						salle[8, 14] = bloc
					if hitbox141.collidepoint(event.pos):
						salle[8,15] = bloc
					if hitbox142.collidepoint(event.pos):
						salle[8, 16] = bloc
					if hitbox143.collidepoint(event.pos):
						salle[8, 17] = bloc
					if hitbox144.collidepoint(event.pos):
						salle[8, 18] = bloc
	#				if hitbox145.collidepoint(event.pos):
	#					salle[9, 1] = bloc
					if hitbox146.collidepoint(event.pos):
						salle[9, 2] = bloc
					if hitbox147.collidepoint(event.pos):
						salle[9, 3] = bloc
					if hitbox148.collidepoint(event.pos):
						salle[9, 4] = bloc
					if hitbox149.collidepoint(event.pos):
						salle[9, 5] = bloc
					if hitbox150.collidepoint(event.pos):
						salle[9, 6] = bloc
					if hitbox151.collidepoint(event.pos):
						salle[9,7] = bloc
					if hitbox152.collidepoint(event.pos):
						salle[9, 8] = bloc
					if hitbox153.collidepoint(event.pos):
						salle[9, 9] = bloc
					if hitbox154.collidepoint(event.pos):
						salle[9, 10] = bloc
					if hitbox155.collidepoint(event.pos):
						salle[9, 11] = bloc
					if hitbox156.collidepoint(event.pos):
						salle[9, 12] = bloc
					if hitbox157.collidepoint(event.pos):
						salle[9, 13] = bloc
					if hitbox158.collidepoint(event.pos):
						salle[9, 14] = bloc
					if hitbox159.collidepoint(event.pos):
						salle[9, 15] = bloc
					if hitbox160.collidepoint(event.pos):
						salle[9, 16] = bloc
					if hitbox161.collidepoint(event.pos):
						salle[9, 17] = bloc
					if hitbox162.collidepoint(event.pos):
						salle[9, 18] = bloc
					print("\nBloc =",bloc,"\nSalle =",salle)
					Refreshstagecrea.refresh(salle,sol,mur,rock,spike,flag,cdtrou,buton,door,buton2,door2,vide)
	#0 = sol, 1 = mur, 2 = pierre, 3 = drapeau, 4 = trou, 5 = pierre dans trou, 6 = bouton, 7 = porte, 8 = pierre dans le trou + pierre par dessus, 9 = bouton 2, 10 = porte 2