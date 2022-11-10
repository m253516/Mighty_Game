import pygame
import sys
import time

pygame.init()


water_image = pygame.image.load("water_image.png")
water_rect = water_image.get_rect()
tile_size = water_rect.width
screen_rect = screen.get_rect()
#print(water_rect)
#screen.blit(water_image, screen_rect.center)
screen = pygame.display.set_mode((10*tile_size, 10*tile_size))
screen.fill((0, 0, 0))

rows = screen_rect,height/tile_size
cols = screen_rect.width/tile_size

for x in range(int(rows)):
    for y in range(int(cols)):
        screen.blit(water_image, (x*water_rect.height, y*water_rect.width))

while True:
    #print("----------check for new events____________")
    recent_events = pygame.event.get()
    #print("----------done checking for events--------")
    for event in recent_events:
        if event.type == pygame.QUIT:
            #print("HeeHeeHa I will never Quit")
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen.fill((255, 0, 0))
            elif event.key == pygame.K_g:
                screen.fill((0, 255, 0))
            elif event.key == pygame.K_b:
                screen.fill((0, 0, 255))
pygame.display.flip()
time.sleep()