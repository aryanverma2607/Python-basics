'''import pygame
pygame.init()

pygame.display.set_mode()

screen = pygame.display.set_mode((800, 600))  #(width,height)
display=pygame.display.set_mode((200,600))

pygame.display.set_caption("My game")
pygame.event.get()

pygame.QUIT

pygame.KEYDOWN
pygame.KEYUP

#screen.fill(255,0,0)       #(R,G,B)

import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My Game")

running = True

while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
pygame.quit()

pygame.KEYDOWN
pygame.KEYUP
#screen.fill(255,0,0)       #(R,G,B)

#display_update
pygame.display.flip("Aryan")
pygame.display.update()

#drawing shapes
pygame.draw.circle()
pygame.draw.rect()



pygame.time.Clock()
clock.tick(60)

pygame.mixer
'''
'''
pygame.mixer.load()
play()
pause()
stop()

pygame.init()
pygame.display.set_mode()
pygame.display.set_caption()
pygame.event.get()
pygame.display.flip()
pygame.draw.rect()
pygame.draw.circle()
pygame.image.load()
screen.blit()
pygame.time.Clock()
pygame.quit()
'''

import pygame

pygame.init()

screen = pygame.display.set_mode((600, 700))
pygame.display.set_caption("My First Game")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.display.update()

pygame.quit()
