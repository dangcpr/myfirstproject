import pygame
pygame.init()
screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("Rắn săn mồi")
running=True
RED = (255,0,0)
GREEN = (0,255,0)
while running:
    pygame.draw.rect(screen,GREEN,(0,0,15,15))
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
    pygame.display.flip()
pygame.quit()