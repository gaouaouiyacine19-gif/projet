import pygame
from manoir import Manoir
from joueur import Joueur
from inventere import Inventaire # <--- NOUVEAU : Import de la classe Inventaire

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.manoir = Manoir()

        self.joueur = Joueur(x=2, y=8, taille=self.manoir.cell_size)
        self.inventaire = Inventaire() # <--- NOUVEAU : Initialisation de l'Inventaire

    def run(self):
        while self.running:
            # NOTE : J'ai laissé la vérification de défaite en commentaire 
            # pour que le jeu ne se ferme pas, mais elle est là si besoin.
            # if self.inventaire.pas <= 0:
            #     print("PERDU ! Plus de pas !")
            #     self.running = False 
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    # <--- Ligne clé : on passe l'inventaire pour déduire un pas
                    self.joueur.deplacer(event.key, self.manoir, self.inventaire) 

            # --- PHASE D'AFFICHAGE ---
            
            self.screen.fill((30, 30, 40))
            self.manoir.afficher(self.screen)
            self.joueur.afficher(self.screen)
            self.inventaire.afficher(self.screen) # Affiche la nouvelle valeur
            
            pygame.display.flip()
            self.clock.tick(60)