#gitignore.io
import pygame
pygame.init()
print('Setup Start')
window = pygame.display.set_mode(size=(600, 500))
print('Setup End')

#https://www.pygame.org/docs/ref/event.html EVENTOS PYGAME

print('Loop Start')
while True:
    #Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Close window
            quit() #End pygame





