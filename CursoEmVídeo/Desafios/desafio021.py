# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# Tentei com o playsound(sla como funciona), mas o guanabra fez com o pygame, massa

import pygame
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("_grenade.mp3")
sound.play()
while pygame.mixer.get_busy():
    pygame.time.delay(100)