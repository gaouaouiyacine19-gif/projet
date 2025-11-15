import pygame

class Joueur:
    def __init__(self, x, y, taille):
        self.x = x  # position colonne
        self.y = y  # position ligne
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

        # 1. Déterminer la direction visée (ZQSD)
        if touche == pygame.K_z and self.y > 0:
            direction_porte = 'N'
            prochain_y -= 1
        elif touche == pygame.K_s and self.y < manoir.rows - 1:
            direction_porte = 'S'
            prochain_y += 1
        elif touche == pygame.K_q and self.x > 0:
            direction_porte = 'O'
            prochain_x -= 1
        elif touche == pygame.K_d and self.x < manoir.cols - 1:
            direction_porte = 'E'
            prochain_x += 1

        if direction_porte is None:
            return None

        # 2. Vérifier si une porte existe dans cette direction
        if not piece_actuelle.portes.get(direction_porte, False):
            print("Mur/Pas de porte dans cette direction.")
            return None

        # --- Mode “visée seulement” (ZQSD = viser, pas encore bouger) ---
        if not validation:
            return {'cible_x': prochain_x, 'cible_y': prochain_y}

        # --- Mode validation (ESPACE) ---
        inventaire.perdre_pas(1)

        piece_visee = manoir.map[prochain_y][prochain_x]

        # Cas 1 : Pièce déjà révélée → mouvement simple
        if piece_visee.nom != "Inconnu":
            self.x = prochain_x
            self.y = prochain_y
            return {'nouvelle_piece': False}

        # Cas 2 : Pièce inconnue → déclenche le tirage
        return {
            'nouvelle_piece': True,
            'cible_x': prochain_x,
            'cible_y': prochain_y
        }
