# catalogue.py

from piece import Piece

class CataloguePiece:
    """Contient toutes les définitions de pièces possibles pour le jeu."""

    def __init__(self):
        self.pieces_disponibles = self._creer_catalogue_initial()
        
    def _creer_catalogue_initial(self):
        """Définit et retourne la liste complète des pièces basiques du jeu."""
        
        catalogue = []
        
        # --- PIÈCES BLEUES (Rareté 0) ---
        
        # 1. MAGASIN (Entrée S, Cul-de-sac)
        catalogue.append(Piece(
            nom="Magasin",
            image_path='magasin.png',
            rareté=0,
            cout_gemmes=0,
            portes={'S': True}, 
            objets={'cles': 1, 'gemmes': 1, 'pieces_or': 1},
            type_piece="magasin" 
        ))

        # 2. GARAGE (Entrée S, Cul-de-sac)
        catalogue.append(Piece(
            nom="Garage",
            image_path='garage.png',
            rareté=0,
            cout_gemmes=1,
            portes={'S': True},
            objets={'cles': 3},
            type_piece="standard"
        ))

        # 3. SALLE MUSIQUE (Entrée S, Sorties O, S)
        catalogue.append(Piece(
            nom="Salle Musique",
            image_path='musique.png',
            rareté=0,
            cout_gemmes=2,
            portes={'S': True, 'O': True}, 
            objets={'cles': 3},
            type_piece="standard"
        ))
        
        # 4. VESTIAIRE (Entrée S, Sortie N)
        catalogue.append(Piece(
            nom="Vestiaire",
            image_path='vestiaire.png',
            rareté=0,
            cout_gemmes=0,
            portes={'S': True, 'N': True},
            objets={'cles': 1},
            type_piece="vestiaire"
        ))
        
        return catalogue

    def get_pioche_initiale(self):
        return self.pieces_disponibles