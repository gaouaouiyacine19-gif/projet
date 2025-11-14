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
            image_path='assets/images/bleumagasin.png',
            rareté=0,
            cout_gemmes=0,
            portes={'S': True}, 
            objets={'cles': 1, 'gemmes': 1, 'pieces_or': 1},
            type_piece="magasin" 
        ))

        # 2. GARAGE (Entrée S, Cul-de-sac)
        catalogue.append(Piece(
            nom="Garage",
            image_path='assets/images/bleugarage.png',
            rareté=0,
            cout_gemmes=1,
            portes={'S': True},

            objets={'cles': 3},
            type_piece="standard"
        
        ))
        
        # 3.  winne cellar (Entrée S, Cul-de-sac)
        catalogue.append(Piece(
            nom="winne cellar",
            image_path='assets/images/bleuWineCellar.png',
            rareté=0,
            cout_gemmes=1,
            portes={'S': True},
            objets={'pieces_or': 1},
            type_piece="standard"
        ))
        # 4. galerie  (Entrée S, Cul-de-sac)
        
        catalogue.append(Piece(
            nom="Galerie",
            image_path='assets/images/bleuGalerie.png',
            rareté=0,
            cout_gemmes=1,
            portes={'N': True,'S': True},
            objets={},
            type_piece="standard"
        ))
         # 5 salle a glasse (Entrée S, Cul-de-sac)
        catalogue.append(Piece(
            nom="glasse",
            image_path='assets/images/bleuglasse.png',
            rareté=0,
            cout_gemmes=1,
            portes={ 'S': True},
            objets={'cles': 0},
            type_piece="standard"
        ))

        # 6 SALLE MUSIQUE (Entrée S, Sorties O, S)
        catalogue.append(Piece(
            nom="Salle Musique",
            image_path='assets/images/bleumusique.png',
            rareté=0,
            cout_gemmes=2,
            portes={'S': True}, 
            objets={'cles': 3},
            type_piece="standard"
        ))
        
        # 7. VESTIAIRE (Entrée S, Sortie N)
        catalogue.append(Piece(
            nom="Vestiaire",
            image_path='assets/images/vestiaire.png',
            rareté=0,
            cout_gemmes=0,
            portes={'S': True, 'N': True},
            objets={'cles': 1},
            type_piece="vestiaire"
        ))
         
        
         # 8. coin(entrée S, cul-de-sac)
        catalogue.append(Piece(
            nom="Chambre d'Amis",
            image_path='assets/images/bleucoin.png',
            rareté=0,
            cout_gemmes=1,
            portes={'S': True,'O': True},
            objets={'cles': 1},
            type_piece="chambre"
        ))

        # 9. Cuisine (entrée S, sorties E et O)
        catalogue.append(Piece(
            nom="Cuisine",
            image_path='assets/images/bleucuisine.png',
            rareté=0,
            cout_gemmes=0,
            portes={'S': True, 'O': True, 'O': True},
            objets={'pieces_or': 4},
            type_piece="standard"
        ))
         # 10. Salle Den  (S et E, donne une clé)
        catalogue.append(Piece(
            nom="Den",
            image_path='assets/images/bleuDen.png',
            rareté=1,
            cout_gemmes=2,
            portes={'S': True, 'E': True, 'O': True},
            objets={'pieces_or': 1},
            type_piece="standard"
        ))
        # 11 salon (S et N, donne 2 gemmes)
        catalogue.append(Piece(
            nom="Le salon",
            image_path='assets/images/bleusalon.png',
            rareté=1,
            cout_gemmes=1,
            portes={'S': True, 'O': True},
            objets={'gemmes': 2},
            type_piece="chambre"
        ))

            # 12Salle du Trésor
        catalogue.append(Piece(
            nom="Salle des trophées",
            image_path='assets/images/bleutrophees.png',
            rareté=2,
            cout_gemmes=3,
            portes={'S': True},
            objets={'pieces_or': 5, 'gemmes': 2},
            type_piece="tresor"
        ))

         # 13. Bibliothèque (S et N, donne 2 gemmes)
        catalogue.append(Piece(
            nom="Bibliothèque",
            image_path='assets/images/bleubibliotheque.png',
            rareté=1,
            cout_gemmes=1,
            portes={'S': True, 'O': True},
            objets={'gemmes': 2},
            type_piece="chambre"
        ))

        #  PIÈCES VERTES ET jaune  (un peu plus rares : rareté 1) 
          # 1 foyer (entrée S, sortie N)

        catalogue.append(Piece(
            nom="foyer",
            image_path='assets/images/Foyer.png',
            rareté=0,
            cout_gemmes=0,
            portes={'S': True, 'N': True},
            objets={'gemmes': 1},
            type_piece="foyer"
        
        ))
        
       

        # PIÈCES ROUGES (plus rares : rareté 2) 

       
        # 1 Salle du toilettes
        catalogue.append(Piece(
            nom="Toilettes",
            image_path='assets/images/bathrome.png',
            rareté=2,
            cout_gemmes=3,
            portes={'S': True},
            objets={'pieces_or': -2, 'gemmes': -5,'cles': -1 },
            type_piece="tresor"
        ))

        # 2 Chambre salle de sporte(donne des clés mais coûte cher)
        catalogue.append(Piece(
            nom="salle de sport",
            image_path='assets/images/salledesport.png',
            rareté=2,
            cout_gemmes=2,
            portes={'S': True, 'O': True,'E': True, 'N': True},
            objets={'gemmes': -30},
            type_piece="piege"
        ))

         # 1 Chambre chapel (tu perd des piece )
        catalogue.append(Piece(
            nom="chapel",
            image_path='assets/images/Chapel.png',
            rareté=1,
            cout_gemmes=2,
            portes={'S': True, 'O': True,'E': True },
            objets={'cles': -1 ,'pieces_or': -1},
            type_piece="piege"
        ))

        #  PIÈCES VIOLETTES (très rares : rareté 3)
        

         # . chambre d'inviter (S et N, donne 2 gemmes)
        catalogue.append(Piece(
            nom="chambre d'invité",
            image_path='assets/images/vioinvites.png',
            rareté=1,
            cout_gemmes=1,
            portes={'S': True},
            objets={'gemmes': 10},
            type_piece="chambre"
        ))
        

        catalogue.append(Piece(
            nom="Boudoir",
            image_path='assets/images/vioboudoir.png',
            rareté=3,
            cout_gemmes=3,
            portes={'O': True, 'S': True,},
            objets={'gemmes': 5, 'pieces_or': 2},
            type_piece="violet"
        ))

        catalogue.append(Piece(
            nom="chambre",
            image_path='assets/images/viochambre.png',
            rareté=3,
            cout_gemmes=4,
            portes={'O': True, 'S': True},
            objets={'cles': 2, 'gemmes': 3,'pas':5},
            type_piece="violet"
        ))

        catalogue.append(Piece(
            nom="Quartier du serviteur",
            image_path='assets/images/vioServant.png',
            rareté=3,
            cout_gemmes=3,
            portes={ 'S': True},
            objets={'cles': 2},
            type_piece="violet"
        ))

        catalogue.append(Piece(
            nom="Chevillere",
            image_path='assets/images/viochevillere.png',
            rareté=3,
            cout_gemmes=4,
            portes={'O': True, 'S': True},
            objets={'gemmes': 10, 'cles': 1},
            type_piece="violet"
        ))

        catalogue.append(Piece(
            nom="Chambreparentale",
            image_path='assets/images/viochambreparentale.png',
            rareté=3,
            cout_gemmes=3,
            portes={'s': True},
            objets={ 'gemmes': 5},
            type_piece="violet"
        ))

        catalogue.append(Piece(
            nom="couchettes",
            image_path='assets/images/viocouchettes.png',
            rareté=3,
            cout_gemmes=2,
            portes={'S': True},
            objets={'pas':5},
            type_piece="violet"
        ))

        
        
        return catalogue

    def get_pioche_initiale(self):
        return self.pieces_disponibles