import pygame

class Joueur:
    def __init__(self, x, y, taille):
        self.x = x      # colonne
        self.y = y      # ligne
        self.taille = taille

    def afficher(self, screen):
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

        # -----------------------------
        # 1. DÉTERMINER LA DIRECTION
        # -----------------------------
        if touche == pygame.K_z:  # Nord
            direction_porte = 'N'
            prochain_y -= 1
        elif touche == pygame.K_s:  # Sud
            direction_porte = 'S'
            prochain_y += 1
        elif touche == pygame.K_q:  # Ouest
            direction_porte = 'O'
            prochain_x -= 1
        elif touche == pygame.K_d:  # Est
            direction_porte = 'E'
            prochain_x += 1

        if direction_porte is None:
            return None

        # Dépasser les limites = mur
        if not (0 <= prochain_x < manoir.cols and 0 <= prochain_y < manoir.rows):
            return {'mur': True}

        # -----------------------------
        # 2. Vérifier si une porte existe
        # -----------------------------
        if not piece_actuelle.portes.get(direction_porte, False):
            print("Mur / Porte fermée.")
            return {
                  'popup_porte': True,
                  'cible_x': prochain_x,
                  'cible_y': prochain_y,
                  'lock_level': 3    
            }
        
    
  


        # -----------------------------
        # MODE VISÉE (ZQSD seulement)
        # -----------------------------
        if not validation:
            return {'cible_x': prochain_x, 'cible_y': prochain_y}

        # -----------------------------
        # MODE DÉPLACEMENT VALIDÉ
        # -----------------------------
        inventaire.perdre_pas(1)

        piece_visee = manoir.map[prochain_y][prochain_x]

        # -----------------------------
        # 3. PORTE VERROUILLÉE ?
        # -----------------------------
        lock = getattr(piece_visee, "lock_level", 0)

        if lock > 0:
            return {
                'popup_porte': True,
                'cible_x': prochain_x,
                'cible_y': prochain_y,
                'lock_level': lock
            }

        # -----------------------------
        # 4. Pièce déjà révélée → mouvement simple
        # -----------------------------
        if piece_visee.nom != "Inconnu":
            self.x = prochain_x
            self.y = prochain_y
            return {'nouvelle_piece': False}

        # -----------------------------
        # 5. Nouvelle pièce inconnue → catalogue
        # -----------------------------
        return {
            'nouvelle_piece': True,
            'cible_x': prochain_x,
            'cible_y': prochain_y
        }


    