import pygame

class Joueur:
    # ... __init__ et afficher sont inchangés ...
    
    def __init__(self, x, y, taille):
        self.x = x
        self.y = y
        self.taille = taille

    def afficher(self, screen):
        rect = pygame.Rect(
            self.x * self.taille + 20 + 10,
            self.y * self.taille + 20 + 10,
            self.taille - 20,
            self.taille - 20
        )
        pygame.draw.rect(screen, (0, 200, 255), rect)

    def deplacer(self, touche, manoir, inventaire): # <--- AJOUT du paramètre 'inventaire'
        
        prochain_x = self.x
        prochain_y = self.y
        deplacement_effectue = False
        
        # Le reste de la logique de calcul de déplacement est inchangé...
        if touche == pygame.K_z and self.y > 0:
            prochain_y -= 1
            deplacement_effectue = True
        elif touche == pygame.K_s and self.y < manoir.rows - 1:
            prochain_y += 1
            deplacement_effectue = True
        elif touche == pygame.K_q and self.x > 0:
            prochain_x -= 1
            deplacement_effectue = True
        elif touche == pygame.K_d and self.x < manoir.cols - 1:
            prochain_x += 1
            deplacement_effectue = True

        if deplacement_effectue:
            # 💡 Ligne clé : le joueur demande à l'inventaire de perdre un pas
            inventaire.perdre_pas(1)
            
            self.x = prochain_x
            self.y = prochain_y