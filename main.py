import pygame
from game import game  # On importera la classe Game dans le fichier suivant


pygame.init()

# Dimensions de la fenêtre
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blue Prince - Projet POO")

# Création du jeu 
game = game(screen)

# Lancement de la boucle principale du jeu
game.run()

# Fermeture propre du jeu
pygame.quit()
