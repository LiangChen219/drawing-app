import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("line drawer")
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
screen.fill(white)

brush_size = 5
brush_color = black

drawing = False
last_pos = None

#continuesly draws a line between last pos and current pos when drawing is true
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                last_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                last_pos = None
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                screen.fill(white)
                
    if drawing:
        current_pos = pygame.mouse.get_pos()
        if last_pos:
            pygame.draw.line(screen, brush_color, last_pos, current_pos, brush_size)
        last_pos = current_pos
        
    clock.tick(60)
    pygame.display.update()
        
            
        
