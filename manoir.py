import pygame

class Manoir:
    def __init__(self):
        # dimensions de la grille
        self.cols = 5
        self.rows = 9
        self.cell_size = 80
        self.margin = 20

    def afficher(self, screen):
        # boucle pour dessiner chaque case
        for y in range(self.rows):
            for x in range(self.cols):
                rect = pygame.Rect(
                    x * self.cell_size + self.margin,
                    y * self.cell_size + self.margin,
                    self.cell_size - 2,
                    self.cell_size - 2
                )
                pygame.draw.rect(screen, (80, 80, 100), rect, 1)  # juste le contour
