# piece.py
import pygame 
class Piece:
    def __init__(self, nom, image_path, couleur="Bleue", rareté=0, cout_gemmes=0,
                 portes={'N': False, 'S': False, 'E': False, 'O': False}, 
                 objets=None, type_piece="standard"):
        
        self.nom = nom
        self.image_path = image_path
        self.couleur = couleur       
        self.rareté = rareté         
        self.cout_gemmes = cout_gemmes 
        self.portes = portes         
        self.objets = objets if objets is not None else {}
        self.type_piece = type_piece 
        
        self.visitee = False
        self.image = None

    def rotate(self):
    #Tourne la pièce de 90° à droite + tourne l'image
    # Rotation logique des portes
       self.portes = {
         'N': self.portes.get('O', False),
         'E': self.portes.get('N', False),
         'S': self.portes.get('E', False),
         'O': self.portes.get('S', False)
        }

    # Rotation de l'image pygame
       if self.image is not None:
            self.image = pygame.transform.rotate(self.image, -90)  # -90 = rotation vers la droite


