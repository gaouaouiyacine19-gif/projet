# game.py
import pygame
from manoir import Manoir
from joueur import Joueur
from inventere import Inventaire # S'assurer que le nom est bon

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.manoir = Manoir()

        # Position de départ : 3ème colonne (index 2), 8ème ligne (index 7).
        # Nous mettons y=7 pour que le joueur NE CACHE PAS le Hall d'entrée (y=8).
        self.joueur = Joueur(x=2, y=7, taille=self.manoir.cell_size)
        self.inventaire = Inventaire() 

    def run(self):
        while self.running:
            
            # Vérification de défaite (optionnel, mais bon à garder)
            if self.inventaire.pas <= 0:
                print("PERDU ! Le joueur n'a plus de pas !")
                self.running = False 
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    # Passage de l'inventaire pour le décompte des pas
                    self.joueur.deplacer(event.key, self.manoir, self.inventaire) 

            # --- PHASE D'AFFICHAGE ---
            
            self.screen.fill((30, 30, 40))
            self.manoir.afficher(self.screen) # Dessine la grille et les images de pièces
            self.joueur.afficher(self.screen) # Dessine le joueur (devrait être visible à y=7)
            self.inventaire.afficher(self.screen) 
            
            pygame.display.flip()
            self.clock.tick(60)