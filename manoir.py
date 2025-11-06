import pygame

class Manoir:
    def __init__(self):
        self.cols = 5
        self.rows = 9
        self.cell_size = 80
        self.margin = 20
        
        self.image_antichambre = None # base.png (en haut)
        self.image_hall_entree = None # hall.jpg (en bas)

        try:
            # Chargement de l'Antichambre (base.png)
            self.image_antichambre = pygame.image.load('base.png').convert_alpha()
            self.image_antichambre = pygame.transform.scale(self.image_antichambre, 
                                                            (self.cell_size - 2, self.cell_size - 2))

            # Chargement du Hall d'entrée (hall.jpg)
            # Vérifiez l'extension : hall.jpg ou hall.png ?
            self.image_hall_entree = pygame.image.load('hall.png').convert_alpha() 
            self.image_hall_entree = pygame.transform.scale(self.image_hall_entree, 
                                                            (self.cell_size - 2, self.cell_size - 2))
        except pygame.error as e:
            print(f"Erreur de chargement d'image: {e}")
            
    def _get_coords_top_left(self, x, y):
        """Calcule les coordonnées en pixels du coin supérieur gauche d'une case."""
        pixel_x = x * self.cell_size + self.margin
        pixel_y = y * self.cell_size + self.margin
        return (pixel_x, pixel_y)

    def afficher(self, screen):
        # 1. Dessin des contours de la grille
        for y in range(self.rows):
            for x in range(self.cols):
                rect = pygame.Rect(
                    x * self.cell_size + self.margin,
                    y * self.cell_size + self.margin,
                    self.cell_size - 2,
                    self.cell_size - 2
                )
                pygame.draw.rect(screen, (80, 80, 100), rect, 1)  
        
        # 2. Dessin des images spécifiques (3ème carreau = index 2)
        COL_CIBLE = 2
        
        # Antichambre (en haut, y=0, col=2)
        if self.image_antichambre:
            antichambre_x, antichambre_y = self._get_coords_top_left(x=COL_CIBLE, y=0)
            screen.blit(self.image_antichambre, (antichambre_x, antichambre_y))
            
        # Hall d'entrée (en bas, y=rows-1, col=2)
        if self.image_hall_entree:
            hall_x, hall_y = self._get_coords_top_left(x=COL_CIBLE, y=self.rows - 1)
            screen.blit(self.image_hall_entree, (hall_x, hall_y))