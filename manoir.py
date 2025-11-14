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
        
        # Pièce "non découverte" : image_path vide pour utiliser le fond de l'écran
        PIECE_NON_DECOUVERTE = Piece(nom="Inconnu", image_path='') 
        manoir_map = [[PIECE_NON_DECOUVERTE for _ in range(self.cols)] for _ in range(self.rows)]
        
        COL_CIBLE = 2
        
        # 1. Antichambre (ARRIVÉE, y=0, x=2)
        manoir_map[0][COL_CIBLE] = Piece(
            nom="Antichambre",
            image_path='assets/images/base.png', 
            portes={'S': True}, 
            type_piece="antichambre"
        )
        
        # 2. Hall d'Entrée (DÉPART, y=8, x=2)
        hall_entree = Piece(
            nom="Hall d'Entrée",
            image_path='assets/images/hall.png', 
            portes={'N': True, 'E': True, 'O': True}, # Portes N, E, O ouvertes pour le départ
            type_piece="hall_entree"
        )
        manoir_map[self.rows - 1][COL_CIBLE] = hall_entree
        hall_entree.visitee = True # Marquer la pièce de départ comme visitée
        
        return manoir_map
        
    def _charger_toutes_images(self):
        """Charge toutes les images nécessaires (carte + catalogue)."""
        
        # Ignore les chemins vides ('') et récupère les chemins uniques
        chemins_map = set(p.image_path for ligne in self.map for p in ligne if p.image_path)
        chemins_catalogue = set(p.image_path for p in self.catalogue.pieces_disponibles if p.image_path)
        chemins_totaux = chemins_map.union(chemins_catalogue)
        
        for path in chemins_totaux:
            if path not in self.images:
                try:
                    img = pygame.image.load(path).convert_alpha()
                    self.images[path] = pygame.transform.scale(img, (self.cell_size - 2, self.cell_size - 2))
                    # Donner l'image aux pièces qui utilisent ce chemin
                    for ligne in self.map:
                        for piece in ligne:
                           if piece.image_path == path:
                                piece.image = self.images[path]
                    for piece in self.catalogue.pieces_disponibles:
                           if piece.image_path == path:
                                piece.image = self.images[path]


                except pygame.error as e:
                    print(f"Erreur: Image '{path}' introuvable. Assurez-vous que le fichier existe: {e}")
                    self.images[path] = None

    def _get_coords_top_left(self, x, y):
        pixel_x = x * self.cell_size + self.margin
        pixel_y = y * self.cell_size + self.margin
        return (pixel_x, pixel_y)

    def afficher(self, screen):
        # ... (Dessin des contours de la grille) ...
        
        for y in range(self.rows):
            for x in range(self.cols):
                rect = pygame.Rect(
                    x * self.cell_size + self.margin,
                    y * self.cell_size + self.margin,
                    self.cell_size - 2,
                    self.cell_size - 2
                )
                
                piece_courante = self.map[y][x]
                
                # Dessin de l'image de la pièce SEULEMENT si un chemin existe et l'image est chargée
                if piece_courante.image_path and piece_courante.image_path in self.images and self.images[piece_courante.image_path]:
                    image_a_afficher = piece_courante.image
                    coords = self._get_coords_top_left(x, y)
                    screen.blit(image_a_afficher, coords)
                    
                # Dessin du contour
                pygame.draw.rect(screen, (80, 80, 100), rect, 1)