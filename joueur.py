import pygame

class Joueur:
    def __init__(self, x, y, taille):
        self.x = x  # position colonne
        self.y = y  # position ligne
        self.taille = taille

    def afficher(self, screen):
        # Le carré bleu du joueur
        rect = pygame.Rect(
            self.x * self.taille + 20 + 10,
            self.y * self.taille + 20 + 10,
            self.taille - 20,
            self.taille - 20
        )
        pygame.draw.rect(screen, (0, 200, 255), rect)  

    def deplacer(self, touche, manoir, inventaire): 
        
        prochain_x = self.x
        prochain_y = self.y
        deplacement_possible = False
        
        # 1. Vérification des limites de la grille (bloque aux bords)
        
        # HAUT (Z): self.y doit être > 0
        if touche == pygame.K_z and self.y > 0:
            prochain_y -= 1
            deplacement_possible = True
            
        # BAS (S): self.y doit être < manoir.rows - 1 (dernière ligne)
        elif touche == pygame.K_s and self.y < manoir.rows - 1:
            prochain_y += 1
            deplacement_possible = True
            
        # GAUCHE (Q): self.x doit être > 0
        elif touche == pygame.K_q and self.x > 0:
            prochain_x -= 1
            deplacement_possible = True
            
        # DROITE (D): self.x doit être < manoir.cols - 1
        elif touche == pygame.K_d and self.x < manoir.cols - 1:
            prochain_x += 1
            deplacement_possible = True

        # 2. Appliquer le mouvement et déduire un pas
        if deplacement_possible:
            # [cite_start]Décompte des pas [cite: 47]
            inventaire.perdre_pas(1)
            
            self.x = prochain_x
            self.y = prochain_y