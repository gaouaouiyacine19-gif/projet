import pygame
from game import Game  # On importera la classe Game dans le fichier suivant

# Initialisation de pygame
pygame.init()

# Dimensions de la fenêtre
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blue Prince - Projet POO")

# Création du jeu (on la fera dans game.py juste après)
game = Game(screen)

# Lancement de la boucle principale du jeu
game.run()

# Fermeture propre du jeu
pygame.quit()
