import pygame

class Joueur:
    def __init__(self, x, y, taille):
        self.x = x  # position colonne
        self.y = y  # position ligne
        self.taille = taille

    def afficher(self, screen):
        rect = pygame.Rect(
            self.x * self.taille + 20 + 10,
            self.y * self.taille + 20 + 10,
            self.taille - 20,
            self.taille - 20
        )
        pygame.draw.rect(screen, (0, 200, 255), rect)  # carré bleu

    def deplacer(self, touche, manoir):
        # Z = haut, S = bas, Q = gauche, D = droite
        if touche == pygame.K_z and self.y > 0:
            self.y -= 1
        elif touche == pygame.K_s and self.y < manoir.rows - 1:
            self.y += 1
        elif touche == pygame.K_q and self.x > 0:
            self.x -= 1
        elif touche == pygame.K_d and self.x < manoir.cols - 1:
            self.x += 1
