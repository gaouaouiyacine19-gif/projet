# game.py

import pygame
from manoir import Manoir
from joueur import Joueur
from inventere import Inventaire

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.manoir = Manoir()

        # Position de départ du joueur (y=7 pour éviter de cacher le Hall à y=8)
        self.joueur = Joueur(x=2, y=8, taille=self.manoir.cell_size) 
        self.inventaire = Inventaire()

        # --- Variables d'état du jeu ---
        self.game_over = False
        self.win = False

        # --- Chargement des images de fin de jeu ---
        self.img_win = None
        self.img_gameover = None
        try:
            # Charger et potentiellement redimensionner l'image de victoire
            self.img_win = pygame.image.load('win.png').convert_alpha()
            self.img_win = pygame.transform.scale(self.img_win, (self.screen.get_width(), self.screen.get_height()))
            
            # Charger et potentiellement redimensionner l'image de défaite
            self.img_gameover = pygame.image.load('gameover.png').convert_alpha()
            self.img_gameover = pygame.transform.scale(self.img_gameover, (self.screen.get_width(), self.screen.get_height()))
        except pygame.error as e:
            print(f"Erreur de chargement des images de fin de jeu: {e}")

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                # Le joueur ne peut bouger que si le jeu est en cours
                elif event.type == pygame.KEYDOWN and not self.game_over and not self.win:
                    self.joueur.deplacer(event.key, self.manoir, self.inventaire)

            # --- Logique de victoire et défaite ---
            # Vérifier seulement si le jeu est en cours
            if not self.game_over and not self.win:
                
                # Condition de DÉFAITE (si self.pas <= 0)
                if self.inventaire.pas <= 0:
                    self.game_over = True
                    print("PERDU ! Le joueur n'a plus de pas !")
                
                # Condition de VICTOIRE (atteindre la dernière ligne, 3ème colonne, soit x=2, y=8)
                if self.joueur.x == 2 and self.joueur.y == 0:
                    self.win = True
                    print("VICTOIRE ! Le joueur a atteint le Hall d'entrée !")

            # --- PHASE D'AFFICHAGE ---
            
            self.screen.fill((30, 30, 40))
            self.manoir.afficher(self.screen) # Dessine la grille et les images de pièces
            self.joueur.afficher(self.screen) # Dessine le joueur
            self.inventaire.afficher(self.screen) # Affiche l'inventaire
            
            # Affichage des images de fin de jeu au-dessus de tout
            if self.game_over and self.img_gameover:
                self.screen.blit(self.img_gameover, (0, 0)) # Affiche l'image de Game Over
            elif self.win and self.img_win:
                self.screen.blit(self.img_win, (0, 0)) # Affiche l'image de victoire
            
            pygame.display.flip()
            self.clock.tick(60)