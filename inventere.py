import pygame

class Inventaire:
    def __init__(self):
        # Objets consommables (section 2.1)
        self.pas = 70       # Démarre à 70 [cite: 47]
        self.pieces_or = 0  # Démarre à 0 [cite: 48]
        self.gemmes = 2     # Démarre à 2 [cite: 49]
        self.cles = 0       # Démarre à 0 [cite: 50]
        self.des = 0        # Démarre à 0 [cite: 51]
        
    def perdre_pas(self, quantite=1):
        """Décrémente le nombre de pas. Appelée à chaque déplacement."""
        self.pas -= quantite # Perdre 1 pas à chaque déplacement [cite: 47]

    def afficher(self, screen):
        """Affiche les principaux artefacts de l'inventaire à droite de l'écran."""
        
        # Initialisation de la police Pygame
        font = pygame.font.Font(None, 30) 
        start_x = 500
        start_y = 50
        line_height = 30
        
        artefacts = [
            (f"PAS: {self.pas}", (255, 255, 0)),
            (f"GEMMES: {self.gemmes}", (0, 255, 255)),
            (f"CLÉS: {self.cles}", (255, 100, 100)),
            (f"DÉS: {self.des}", (255, 165, 0)),
            (f"PIÈCES D'OR: {self.pieces_or}", (255, 223, 0))
        ]
        
        for index, (text_content, color) in enumerate(artefacts):
            text_surface = font.render(text_content, True, color)
            # Correction de l'erreur TypeError : seulement (X, Y)
            screen.blit(text_surface, (start_x, start_y + index * line_height))