import pygame
from piece import Piece 
from catalogue import CataloguePiece 

class Manoir:
    def __init__(self):
        self.cols = 5
        self.rows = 9
        self.cell_size = 80
        self.margin = 20
        
        self.catalogue = CataloguePiece() 
        self.images = {}

        self.map = self._initialiser_map()
        self._charger_toutes_images()
        
    def _initialiser_map(self):
        """Définit la grille 9x5 des pièces, y compris le départ et l'arrivée."""
        

        PIECE_NON_DECOUVERTE = Piece(
            nom="Inconnu",
            image_path='',
            portes={'N': False, 'S': False, 'E': False, 'O': False},
            lock_level=0
        )

        manoir_map = [[PIECE_NON_DECOUVERTE for _ in range(self.cols)] for _ in range(self.rows)]
        
        COL_CIBLE = 2
        
        # 1. Antichambre (ARRIVÉE)
        manoir_map[0][COL_CIBLE] = Piece(
            nom="Antichambre",
            image_path='assets/images/base.png', 
            portes={'S': True},
            lock_level=0,
            type_piece="antichambre"
        )
        
        # 2. Hall d'Entrée (DÉPART)
        hall_entree = Piece(
            nom="Hall d'Entrée",
            image_path='assets/images/hall.png', 
            portes={'N': True, 'E': True, 'O': True},
            lock_level=0,
            type_piece="hall_entree"
        )
        manoir_map[self.rows - 1][COL_CIBLE] = hall_entree
        hall_entree.visitee = True
        
        return manoir_map
        
    def _charger_toutes_images(self):
        """Charge toutes les images nécessaires (carte + catalogue)."""

        chemins_map = set(
            p.image_path for ligne in self.map for p in ligne if p.image_path
        )
        chemins_catalogue = set(
            p.image_path for p in self.catalogue.pieces_disponibles if p.image_path
        )
        chemins_totaux = chemins_map.union(chemins_catalogue)
        
        for path in chemins_totaux:
            if path not in self.images:
                try:
                    img = pygame.image.load(path).convert_alpha()
                    img = pygame.transform.scale(img, (self.cell_size - 2, self.cell_size - 2))
                    self.images[path] = img

                    # Donner l'image aux pièces du manoir
                    for ligne in self.map:
                        for piece in ligne:
                            if piece.image_path == path:
                                piece.image = img.copy()

                    # Donner l'image aux pièces du catalogue
                    for piece in self.catalogue.pieces_disponibles:
                        if piece.image_path == path:
                            piece.image = img.copy()

                except pygame.error as e:
                    print(f"Erreur: Image '{path}' introuvable : {e}")
                    self.images[path] = None

    def _get_coords_top_left(self, x, y):
        pixel_x = x * self.cell_size + self.margin
        pixel_y = y * self.cell_size + self.margin
        return (pixel_x, pixel_y)

    def afficher(self, screen):
        for y in range(self.rows):
            for x in range(self.cols):
                rect = pygame.Rect(
                    x * self.cell_size + self.margin,
                    y * self.cell_size + self.margin,
                    self.cell_size - 2,
                    self.cell_size - 2
                )
                
                piece = self.map[y][x]

                # Afficher l'image
                if piece.image:
                    coords = self._get_coords_top_left(x, y)
                    screen.blit(piece.image, coords)
                    
                # Contour
                pygame.draw.rect(screen, (0, 0, 0), rect, 2)
