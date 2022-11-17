import pygame

class Ship:
    def __init__(self):
        self.image = pygame.load("images/my_ship.png")
        self.rect = self.image.get_rect()

    def move(self, coordinate):
        self.rect.center = coordinate

    def draw(self,):