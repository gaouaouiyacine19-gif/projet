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

    def deplacer(self, touche, manoir, inventaire, validation=False): 
        
        prochain_x = self.x
        prochain_y = self.y
        direction_porte = None 
        
        piece_actuelle = manoir.map[self.y][self.x]
        
        # 1. Déterminer la direction visée (ZQSD)
        
        # HAUT (Z): y > 0
        if touche == pygame.K_z and self.y > 0:
            direction_porte = 'N' 
            prochain_y -= 1
        # BAS (S) : Désactivé au départ car on est sur la dernière ligne (y=8)
        elif touche == pygame.K_s and self.y < manoir.rows - 1:
            direction_porte = 'S' 
            prochain_y += 1
        # GAUCHE (Q): x > 0
        elif touche == pygame.K_q and self.x > 0:
            direction_porte = 'O' 
            prochain_x -= 1
        # DROITE (D): x < manoir.cols - 1
        elif touche == pygame.K_d and self.x < manoir.cols - 1:
            direction_porte = 'E' 
            prochain_x += 1
            
        if direction_porte is None:
            return None 

        # Vérification si la porte existe (Mur/Porte Fermée)
        if not piece_actuelle.portes.get(direction_porte, False):
            print("Mur/Pas de porte dans cette direction.")
            return None
        
        # --- Si validation=False (ZQSD vient d'être pressé, on ne fait que viser) ---
        if not validation:
            return {'cible_x': prochain_x, 'cible_y': prochain_y}

        # --- PHASE DE VALIDATION (validation=True, i.e. Espace est pressé) ---
        
        # Déduction des pas
        inventaire.perdre_pas(1)
        
        piece_visee = manoir.map[prochain_y][prochain_x]
        
        # Cas 1 : Pièce déjà découverte (mouvement simple)
        if piece_visee.nom != "Inconnu":
            self.x = prochain_x
            self.y = prochain_y
            return {'nouvelle_piece': False}
        
        # Cas 2 : Pièce INCONNUE (Ouverture de porte, déclenche le tirage)
        else:
            # Le joueur ne bouge PAS avant d'avoir choisi la pièce
            return {'nouvelle_piece': True, 'cible_x': prochain_x, 'cible_y': prochain_y}