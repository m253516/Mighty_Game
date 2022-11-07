import pygame
import time
pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("This is my really cool game")
screen.fill((0,0,255))

while True:
    print("_______________check for new events________________")
    recent_events = pygame.event.get()
    print("_______________check for new events________________")

    for event in recent_events:
        print(event)
    pygame.display.flip()
    time.sleep(2)
