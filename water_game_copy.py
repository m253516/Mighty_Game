import pygame
import time
import sys

pygame.init()

pygame.display.set_caption("This is my game!")
screen = pygame.display.set_mode((tile_size*10, tile_size*10))

screen.fill((0, 0, 255))

water_image = pygame.image.load('images/water_image.png')
screen_rect = screen.get_rect()
screen.blit(water_image, screen_rect.center)

r = screen_rect.width // water_rect.width
c = screen_rect.height // water_rect.height
tile_size = water_rect.width

#tile the entire screen with water
for x in range(r):
   for y in range(c):
       screen.blit(water_image, (x*water_rect.height, y*water_rect.width))





while True:
   #step 1 - check for user input (key press, mouse clicks)
   recent_events = pygame.event.get()
   print("-----------Checking for new events ------------")
   for event in recent_events:
       #print(event.type)
       if event.type == pygame.QUIT:
           print("Ha Ha I will never quit!")
           pygame.quit()
           sys.exit()
       elif event.type == pygame.KEYDOWN:
           screen.fill((255, 0, 0))
       elif event.type == pygame.KEYUP:
           screen.fill((255, 0, 0))
       elif event.type == pygame.MOUSEMOTION:
           screen.fill((0, 255, 0))
   print("----------Done Checking -----------------")
   pygame.display.flip()
   time.sleep(1)