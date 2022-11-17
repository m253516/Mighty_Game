import pygame
import sys
import time
from ship import Ship
from island import Island

pygame.init()


water_image = pygame.image.load("images/water_image.png")
water_rect = water_image.get_rect()
tile_size = water_rect.width
screen = pygame.display.set_mode((tile_size*10, tile_size*10))
screen.fill((0, 0, 0))
screen_rect = screen.get_rect()

#print(water_rect)
r = screen_rect.width // water_rect.width
c = screen_rect.height // water_rect.height

#load my Island images
island = Island()
island = Island()
#tile the entire screen with water
for x in range(r):
   for y in range(c):
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
    time.sleep(1)

#new code to catch up

    # #draw the screen
    # draw_background()
    # my_ship.move(coordniate)
    # #ship_rect.center = coordinate
    # screen.blit(my_ship.ikmage, ship_rect)
    # pygame.display.flip()