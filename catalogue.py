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
            image_path='assets/images/magasin.png',
            rareté=0,
            cout_gemmes=0,
            portes={'N': True, 'S': True}, 
            objets={'cles': 1, 'gemmes': 1, 'pieces_or': 1},
            type_piece="magasin" 
        ))

        # 2. GARAGE (Entrée S, Cul-de-sac)
        catalogue.append(Piece(
            nom="Garage",
            image_path='assets/images/garage.png',
            rareté=0,
            cout_gemmes=1,
            portes={'N': True, 'S': True},

            objets={'cles': 2},
            type_piece="standard"
        ))
        # 2.  winne cellar (Entrée S, Cul-de-sac)
        catalogue.append(Piece(
            nom="winne cellar",
            image_path='assets/images/WineCellar.png',
            rareté=0,
            cout_gemmes=1,
            portes={'N': True, 'S': True},
            objets={'pieces_or': 1},
            type_piece="standard"
        ))
        # 2. GARAGE (Entrée S, Cul-de-sac)
        
        catalogue.append(Piece(
            nom="Galerie",
            image_path='assets/images/Galerie.png',
            rareté=0,
            cout_gemmes=1,
            portes={'N': True, 'S': True, 'E': True},
            objets={},
            type_piece="standard"
        ))
         # 2. salle a galsse (Entrée S, Cul-de-sac)
        catalogue.append(Piece(
            nom="glasse",
            image_path='assets/images/glasse.png',
            rareté=0,
            cout_gemmes=1,
            portes={'N': True, 'S': True},
            objets={'cles': 0},
            type_piece="standard"
        ))

        # 3. SALLE MUSIQUE (Entrée S, Sorties O, S)
        catalogue.append(Piece(
            nom="Salle Musique",
            image_path='assets/images/garage.png',
            rareté=0,
            cout_gemmes=2,
            portes={'S': True, 'O': True}, 
            objets={'cles': 3},
            type_piece="standard"
        ))
        
        # 4. VESTIAIRE (Entrée S, Sortie N)
        catalogue.append(Piece(
            nom="Vestiaire",
            image_path='assets/images/vestiaire.png',
            rareté=0,
            cout_gemmes=0,
            portes={'S': True, 'N': True},
            objets={'cles': 1},
            type_piece="vestiaire"
        ))
         # 5. foyet  (entrée S, sortie N)
        catalogue.append(Piece(
            nom="foyer",
            image_path='assets/images/Foyer.png',
            rareté=0,
            cout_gemmes=0,
            portes={'S': True, 'N': True},
            objets={'gemmes': 1},
            type_piece="foyer"
        ))
         # 6. coin(entrée S, cul-de-sac)
        catalogue.append(Piece(
            nom="Chambre d'Amis",
            image_path='assets/images/coin.png',
            rareté=0,
            cout_gemmes=1,
            portes={'S': True},
            objets={'gemmes': 1},
            type_piece="chambre"
        ))

        # 7. Cuisine (entrée S, sorties E et O)
        catalogue.append(Piece(
            nom="Cuisine",
            image_path='assets/images/cuisine.png',
            rareté=0,
            cout_gemmes=0,
            portes={'S': True, 'E': True, 'O': True},
            objets={'pieces_or': 1},
            type_piece="standard"
        ))

        #  PIÈCES VERTES (un peu plus rares : rareté 1) 

        # 8. salon (S et N, donne 2 gemmes)
        catalogue.append(Piece(
            nom="Le salon",
            image_path='assets/images/salon.png',
            rareté=1,
            cout_gemmes=1,
            portes={'S': True, 'N': True},
            objets={'gemmes': 2},
            type_piece="chambre"
        ))
        

        # 9. Salle Den  (S et E, donne une clé)
        catalogue.append(Piece(
            nom="Den",
            image_path='assets/images/Den.png',
            rareté=1,
            cout_gemmes=2,
            portes={'S': True, 'E': True},
            objets={'pieces_or': 1},
            type_piece="standard"
        ))
        
        # 10. Bibliothèque (S et N, donne 2 gemmes)
        catalogue.append(Piece(
            nom="Bibliothèque",
            image_path='assets/images/bibliotheque.png',
            rareté=1,
            cout_gemmes=1,
            portes={'S': True, 'N': True},
            objets={'gemmes': 2},
            type_piece="chambre"
        ))

        # PIÈCES ROUGES (plus rares : rareté 2) 

        # 11. Salle du Trésor
        catalogue.append(Piece(
            nom="Salle des trophées",
            image_path='assets/images/trophees.png',
            rareté=2,
            cout_gemmes=3,
            portes={'S': True},
            objets={'pieces_or': 5, 'gemmes': 2},
            type_piece="tresor"
        ))
        # 11. Salle du toilettes
        catalogue.append(Piece(
            nom="Toilettes",
            image_path='assets/images/bathrome.png',
            rareté=2,
            cout_gemmes=3,
            portes={'S': True},
            objets={'pieces_or': -2, 'gemmes': -5,'cles': -1 },
            type_piece="tresor"
        ))

        # 12. Chambre Maudite (donne des clés mais coûte cher)
        catalogue.append(Piece(
            nom="salle de sport",
            image_path='assets/images/salledesport.png',
            rareté=2,
            cout_gemmes=2,
            portes={'S': True, 'O': True},
            objets={'gemmes': -30},
            type_piece="piege"
        ))

         # 12. Chambre Maudite (tu perd des piece )
        catalogue.append(Piece(
            nom="chapel",
            image_path='assets/images/Chapel.png',
            rareté=1,
            cout_gemmes=2,
            portes={'S': True, 'O': True},
            objets={'cles': -1 ,'pieces_or': -1},
            type_piece="piege"
        ))

        #  PIÈCES VIOLETTES (très rares : rareté 3)

         # . chambre d'inviter (S et N, donne 2 gemmes)
        catalogue.append(Piece(
            nom="chambre d'invité",
            image_path='assets/images/invites.png',
            rareté=1,
            cout_gemmes=1,
            portes={'S': True, 'N': True},
            objets={'gemmes': 10},
            type_piece="chambre"
        ))
        
        
        
        
        
        return catalogue

    def get_pioche_initiale(self):
        return self.pieces_disponibles