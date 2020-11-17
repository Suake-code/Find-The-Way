import pygame
from pygame.locals import *
def bandeson(debut):
    pygame.mixer.init(44100,-16,2,2048)
    if debut == 0:
        musiquejeu = pygame.mixer.Sound("Sound/bandeson.wav")
        pygame.mixer.music.load('Sound/bandeson.wav')
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.2)
    if debut == -1:
        musiquetest = pygame.mixer.Sound("Sound/musiquemenu.wav")
        musiquejeu = pygame.mixer.Sound("Sound/musiquemenu.wav")
        pygame.mixer.music.load('Sound/musiquemenu.wav')
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.2)