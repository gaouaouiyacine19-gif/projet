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

    # HAUT (Z)
        if touche == pygame.K_z and self.y > 0:
            direction_porte = 'N'
            prochain_y -= 1
        

    # BAS (S)
        elif touche == pygame.K_s and self.y < manoir.rows - 1:
            direction_porte = 'S'
            prochain_y += 1

    # GAUCHE (Q)
        elif touche == pygame.K_q and self.x > 0:
            direction_porte = 'O'
            prochain_x -= 1

    # DROITE (D)
        elif touche == pygame.K_d and self.x < manoir.cols - 1:
            direction_porte = 'E'
            prochain_x += 1

    # Si aucune direction valide → stop
        if direction_porte is None:
            return None

    # Récupère la pièce ciblée (celle où on veut entrer)
        piece_visee = manoir.map[prochain_y][prochain_x]

    # 2. Vérifier si la pièce est verrouillée (lock_level)
        if piece_visee.lock_level > 0:
             # Pas assez de clés ?
            if inventaire.cles < piece_visee.lock_level:
                 print(f"Porte verrouillée ! Il faut {piece_visee.lock_level} clé(s).")
                 return None
           
           


       
        # Assez de clés → ouvrir la porte
        inventaire.cles -= piece_visee.lock_level
        print(f"Porte ouverte ! {piece_visee.lock_level} clé(s) consommée(s).")
        piece_visee.lock_level = 0  # porte maintenant ouverte définitivement

    # 3. Vérification si la porte existe physiquement
        if not piece_actuelle.portes.get(direction_porte, False):
            print("Mur/Pas de porte dans cette direction.")
        
            return None

    # --- Si validation=False (ZQSD juste pressé, on vise) ---
        if not validation:
            return {'cible_x': prochain_x, 'cible_y': prochain_y}
        

    # --- PHASE DE VALIDATION (validation=True = ESPACE) ---

    # Déduction des pas
        inventaire.perdre_pas(1)

    # Cas 1 : Pièce déjà découverte
        if piece_visee.nom != "Inconnu":
            self.x = prochain_x
            self.y = prochain_y
            return {'nouvelle_piece': False}
        
        
        

    # Cas 2 : Pièce INCONNUE → Choix d'une nouvelle pièce
        return {
        'nouvelle_piece': True,
        'cible_x': prochain_x,
        'cible_y': prochain_y
    }



    
    

    