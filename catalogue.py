# catalogue.py

from piece import Piece

class CataloguePiece:
    """Contient toutes les définitions de pièces possibles pour le jeu."""

    def __init__(self):
        self.pieces_disponibles = self._creer_catalogue_initial()
        
    def _creer_catalogue_initial(self):
        """Définit et retourne la liste complète des pièces basiques du jeu."""
        
        catalogue = []
        
        # les chambre blue 
        # 1. MAGASIN 
        catalogue.append(Piece(
            nom="Magasin",
            image_path='assets/images/bleumagasin.png',
            rareté=0,
            cout_gemmes=0,
            portes={'S': True }, 
            objets={'cles': 1, 'gemmes': 1, 'pieces_or': 1, 'pelle': 1 },
            type_piece="magasin" 
        ))

        # 2. GARAGE 
        catalogue.append(Piece(
            nom="Garage",
            image_path='assets/images/bleugarage.png',
            rareté=0,
            cout_gemmes=1,
            portes={'S': True },
            objets={'cles': 3,'pelle': 1},
            type_piece="standard"
        
        ))
        
        # 3.  winne cellar 
        catalogue.append(Piece(
            nom="winne cellar",
            image_path='assets/images/bleuWineCellar.png',
            rareté=0,
            cout_gemmes=1,
            portes={'S': True},
            objets={'pieces_or': 3},
            type_piece="standard"
        ))
        # 4. galerie 
        
        catalogue.append(Piece(
            nom="Galerie",
            image_path='assets/images/bleuGalerie.png',
            rareté=0,
            cout_gemmes=1,
            portes={'N': True,'S': True},
            objets={'pas':5,'pelle': 1},
            type_piece="standard"
        ))
         # 5 salle a glasse 
        catalogue.append(Piece(
            nom="glasse",
            image_path='assets/images/bleuglasse.png',
            rareté=0,
            cout_gemmes=1,
            portes={ 'S': True },
            objets={'cles': 0,'marteau': 1,'pelle': 1},
            type_piece="standard"
        ))

        # 6 SALLE MUSIQUE 
        catalogue.append(Piece(
            nom="Salle Musique",
            image_path='assets/images/bleumusique.png',
            rareté=0,
            cout_gemmes=2,
            portes={'S': True , 'O': True  }, 
            objets={'cles': 1, 'pelle': 1,'pelle': 1},
            
            type_piece="standard"
            

        ))
        
        # 7. VESTIAIRE 
        catalogue.append(Piece(
            nom="Vestiaire",
            image_path='assets/images/vestiaire.png',
            rareté=0,
            cout_gemmes=0,
            portes={'S': True, 'N': True},
            objets={'pas': 2,'patte_lapin': 1,'pelle': 1},
            type_piece="vestiaire"
            

        ))
         
        
         # 8. coin
        catalogue.append(Piece(
            nom="Chambre d'Amis",
            image_path='assets/images/bleucoin.png',
            rareté=0,
            cout_gemmes=1,
            portes={'S': True,'O': True},
            objets={'cles': 1,'detecteur_metal': 1},
            type_piece="chambre"
           

        ))

        # 9. Cuisine 
        catalogue.append(Piece(
            nom="Cuisine",
            image_path='assets/images/bleucuisine.png',
            rareté=0,
            cout_gemmes=0,
            portes={'S': True, 'O': True},
            objets={'pieces_or': 4,'marteau': 1},
            type_piece="standard"
           

        ))
         # 10. Salle Den  
        catalogue.append(Piece(
            nom="Den",
            image_path='assets/images/bleuDen.png',
            rareté=1,
            cout_gemmes=2,
            portes={'S': True, 'E': True, 'O': True},
            objets={'des': 1,'pelle': 1},
            type_piece="standard"
            

        ))
        # 11 salon
        catalogue.append(Piece(
            nom="Le salon",
            image_path='assets/images/bleusalon.png',
            rareté=1,
            cout_gemmes=1,
            portes={'S': True, 'O': True},
            objets={'gemmes': 5,'kit_crochetage': 1,'cles': 1,'pelle': 1},
            type_piece="chambre"
        ))

            # 12Salle du Trésor
        catalogue.append(Piece(
            nom="Salle des trophées",
            image_path='assets/images/bleutrophees.png',
            rareté=2,
            cout_gemmes=3,
            portes={'S': True},
            objets={'pieces_or': 5, 'gemmes': 2,'cles': 1},
            type_piece="tresor"
        ))

         # 13. Bibliothèque 
        catalogue.append(Piece(
            nom="Bibliothèque",
            image_path='assets/images/bleubibliotheque.png',
            rareté=1,
            cout_gemmes=1,
            portes={'S': True, 'O': True},
            objets={'gemmes': 2,'pelle': 1},
            type_piece="chambre"
        ))
        #14
         
        catalogue.append(Piece(
            nom="Work shop",
            image_path='assets/images/bleuWorkshop.png',
            rareté=0,
            cout_gemmes=0,
            portes={'S': True,'N':True}, 
            objets={'cles': 1, 'gemmes': 1, 'pieces_or': 1},
            type_piece="magasin" 
        ))

        #15
        catalogue.append(Piece(
            nom="Study",
            image_path='assets/images/bleuStudy.png',
            rareté=0,
            cout_gemmes=0,
            portes={'S': True}, 
            objets={'cles': 1, 'gemmes': 1, 'pieces_or': 1,'pelle': 1},
            type_piece="study" 
        ))
        #16
        catalogue.append(Piece(
            nom="Spare Room",
            image_path='assets/images/bleuSpareRoom.png',
            rareté=0,
            cout_gemmes=0,
            portes={'S': True,'N':True}, 
            objets={'cles': 1, 'gemmes': 1, 'pieces_or': 1,'detecteur_metal': 1},
            type_piece="magasin" 
            #jdjdj
          
        ))

        #17
        catalogue.append(Piece(
            nom="Security",
            image_path='assets/images/bleuSecurity.png',
            rareté=0,
            cout_gemmes=1,
            portes={'S': True,'E':True,'O':True}, 
            objets={'cles': 1, 'gemmes': 1, 'pieces_or': 1,'marteau': 1},
            
            type_piece="magasin" 
            

        ))


        #18
        catalogue.append(Piece(
            nom="Obser vatory",
            image_path='assets/images/bleuObservatory.png',
            rareté=0,
            cout_gemmes=0,
            portes={'S': True,'O':True}, 
            objets={'cles': 0, 'gemmes': 2, 'pieces_or': 0},
            type_piece="magasin" 
        ))

        #19
        catalogue.append(Piece(
            nom="Laboratory ",
            image_path='assets/images/bleuLaboratory.png',
            rareté=0,
            cout_gemmes=1,
            portes={'S': True,'O':True}, 
            objets={'cles': 1, 'gemmes': 1, 'pieces_or': 1},
            type_piece="magasin" 
        ))
        #20
        catalogue.append(Piece(
            nom="Dining Room ",
            image_path='assets/images/bleuDiningRoom.png',
            rareté=0,
            cout_gemmes=1,
            portes={'S': True,'O':True,'E':True}, 
            objets={'cles': 0, 'gemmes': 2, 'pieces_or': 0,'pelle': 1},
            type_piece="magasin" 
        ))
        
        #21
        catalogue.append(Piece(
            nom="Drawing Room",
            image_path='assets/images/bleuDrawingRoom.png',
            rareté=0,
            cout_gemmes=0,
            portes={'S': True,'O':True,'E':True}, 
            objets={'cles': -1, 'gemmes': 0, 'pieces_or': 1,'marteau': 1},
            type_piece="magasin" 
            

        ))


        #  PIÈCES VERTES ET jaune  
          # 1 foyer 

        catalogue.append(Piece(
            nom="foyer",
            image_path='assets/images/Foyer.png',
            rareté=0,
            cout_gemmes=0,
            portes={'S': True, 'N': True},
            objets={'gemmes': 0},
            type_piece="foyer"
        
        ))
          # 2 chambre cours 
        catalogue.append(Piece(
            nom="cour",
            image_path='assets/images/vertcour.png',
            rareté=1,
            cout_gemmes=1,
            portes={'S': True, 'E': True, 'O': True},
            objets={'gemmes': 1},
            type_piece="chambre"
        ))

        # 3 patio (verrouillée)
        catalogue.append(Piece(
            nom="patio",
            image_path='assets/images/vertpatio.png',
            rareté=1,
            cout_gemmes=1,
            portes={'S': True, 'O': True},
            lock_level=1,      # nécessite 1 clé
            objets={'cles': -1, 'pas': 5, 'marteau': 1},
            type_piece="Patio"
    
        ))

            
        # 4 chambre jardin

        catalogue.append(Piece(
            nom=" Jardin",
            image_path='assets/images/vertjardin.png',
            rareté=1,
            cout_gemmes=1,
            portes={ 'S': True, 'E': True, 'O': True},
            lock_level=1,
            objets={'pieces_or': 2 , 'gemmes': 2,'marteau': 1,'pas': -5},

            type_piece="vert"
        ))
          

          # 5 chambre solarium
        catalogue.append(Piece(
            nom="Solarium.png",
            image_path='assets/images/vertsolarium.png',
            rareté=1,
            cout_gemmes=1,
            portes={'S': True},
            lock_level=1, 
            objets={'gemmes': 2},
            type_piece="vert"
            ))
        

        # 6 chambre Tarrace 

        catalogue.append(Piece(
            nom="Terrace",
            image_path='assets/images/vertTerrace.png',
            rareté=1,
            cout_gemmes=1,
            portes={ 'S': True},
            lock_level=1, 
            objets={'pieces_or':-2,'detecteur_metal': 1,'gemmes': 2},
            type_piece="vert"
        ))

        # 7 chambre  cloister

        catalogue.append(Piece(
            nom="Cloister",
            image_path='assets/images/vertvCloister.png',
            rareté=1,
            cout_gemmes=1,
            portes={'N': True, 'S': True, 'E': True, 'O': True},
            objets={'cles': 1, 'gemmes': 1,'kit_crochetage': 1},
        

            type_piece="vert"
        ))


         # 8 chambre veranda 
        catalogue.append(Piece(
            nom="Veranda",
            image_path='assets/images/vertVeranda.png',
            rareté=1,
            cout_gemmes=1,
            portes={'N': True, 'S': True},
            lock_level=1, 
            objets={'pieces_or': 2, 'gemmes': 3,'pelle': 2,'cles': 1},

            type_piece="vert"
        ))

        
         # les chambre jaune 
          #1 chambre casino
        catalogue.append(Piece(
            nom="Casino",
            image_path='assets/images/jauneCasino.png',
            rareté=1,
            cout_gemmes=1,
            portes={'O': True, 'S': True,},
            lock_level=1, 
            objets={'pieces_or': 1, 'gemmes': 1},
            type_piece="jaune"
        ))
          # 2 chambre corridor 
        catalogue.append(Piece(
            nom="Corridor", 
            image_path='assets/images/jauneCorridor.png',
            rareté=1,
            cout_gemmes=0,
            portes={'N': True, 'S': True },
            lock_level=1,
            objets={'pas': -2},
            type_piece="jaune"
        ))
         #3
        catalogue.append(Piece(
            nom="Esst wing hall",
            image_path='assets/images/jauneEast.png',
            rareté=1,
            cout_gemmes=1,
            portes={'S': True, 'E': True, 'O': True},
            objets={'pieces_or': 1, 'gemmes': 2},
            

            type_piece="jaune"
        ))
        #4
        catalogue.append(Piece(
            nom="Hallway Icon",
            image_path='assets/images/jauneHallwayIcon.png',
            rareté=1,
            cout_gemmes=1,
            portes={ 'S': True, 'E': True, 'O': True},
            lock_level=1,
            objets={'pieces_or': 1, 'gemmes': 1},
            type_piece="jaune"
        ))
        #5 
        catalogue.append(Piece(
            nom="Locksmith",
            image_path='assets/images/jauneLocksmith.png',
            rareté=1,
            cout_gemmes=1,
            portes={ 'S': True},
            lock_level=1, 
            objets={'pieces_or': 0, 'gemmes': 1,'kit_crochetage': 1},

            type_piece="jaune"
        ))
        # 6
        catalogue.append(Piece(
            nom="Locksmith",
            image_path='assets/images/jauneLocksmith.png',
            rareté=1,
            cout_gemmes=1,
            portes={'N': True, 'S': True, 'E': True, 'O': True},
            lock_level=1, 
            objets={'marteau': 1},

            type_piece="jaune"
        ))
        # 7
        catalogue.append(Piece(
            nom="Passageway",
            image_path='assets/images/jaunePassageway.png',
            rareté=1,
            cout_gemmes=1,
            portes={ 'S': True},
            lock_level=1, 
            objets={'pieces_or': 1, 'gemmes': 1},
            type_piece="jaune"
        ))
        # 8
        catalogue.append(Piece(
            nom="Secret Passage",
            image_path='assets/images/jauneSecretPassage.png',
            rareté=1,
            cout_gemmes=1,
            portes={ 'S': True,'O':True},
            lock_level=1, 
            objets={'pieces_or': 1, 'gemmes': 1},
            type_piece="jaune"
        ))
       

        #9
        catalogue.append(Piece(
            nom=" The Armory",
            image_path='assets/images/jauneTheArmory.png',
            rareté=1,
            cout_gemmes=1,
            portes={'O': True, 'S': True},
            lock_level=2, 
            objets={'pieces_or': 1, 'gemmes': 1},
            type_piece="jaune"
            

        ))

        #10
        catalogue.append(Piece(
            nom=" Tunnel",
            image_path='assets/images/jauneTunnel.png',
            rareté=1,
            cout_gemmes=1,
            portes={'N': True, 'S': True},
            lock_level=1, 
            objets={'pelle': 1},
            type_piece="jaune"
        ))
        #11
        catalogue.append(Piece(
            nom=" West Wing Hall",
            image_path='assets/images/jauneWestWingHall.png',
            rareté=1,
            cout_gemmes=1,
            portes={ 'S': True, 'E': True, 'O': True},
            lock_level=2,
            objets={'des': 1, 'gemmes': 1,'detecteur_metal': 1},
            type_piece="jaune"
            

        ))
        






        # PIÈCES ROUGES 

       
        # 1 Salle du toilettes
        catalogue.append(Piece(
            nom="Toilettes",
            image_path='assets/images/bathrome.png',
            rareté=2,
            cout_gemmes=3,
            portes={'S': True},
            lock_level=1, 
            objets={'pieces_or': -2, 'gemmes': -5,'cles': -1 },
            type_piece="Toilettes"
        ))

        # 2 Chambre salle de sporte(
        catalogue.append(Piece(
            nom="salle de sport",
            image_path='assets/images/rougesalledesport.png',
            rareté=2,
            cout_gemmes=2,
            portes={'S': True, 'O': True,'E': True, 'N': True},
            lock_level=1, 
            objets={'gemmes': -6},
            type_piece="piege"
        ))

         # 3 Chambre chapel 
        catalogue.append(Piece(
            nom="chapel",
            image_path='assets/images/Chapel.png',
            rareté=1,
            cout_gemmes=2,
            portes={'S': True, 'O': True,'E': True },
            lock_level=1, 
            objets={'cles': -1 ,'pieces_or': -1,'pas' : 5},
            type_piece="piege"
            

        ))



         # 4 Salle du Weight
        catalogue.append(Piece(
            nom="Weight",
            image_path='assets/images/rougeWeight.png',
            rareté=2,
            cout_gemmes=3,
            portes={'N': True, 'S': True, 'E': True, 'O': True},
            lock_level=2, 
            objets={'pieces_or':-1 , 'gemmes': 2,'cles': 1 },
            type_piece="tresor"
        ))

         # 5 Salle du Gymnasium
        catalogue.append(Piece(
            nom="Gymnasium",
            image_path='assets/images/rougeGymnasium.png',
            rareté=2,
            cout_gemmes=3,
            portes={'S': True, 'E': True, 'O': True},
            lock_level=1, 
            objets={ 'gemmes': -1,'cles': -1 },
            type_piece="tresor"
        ))

         # 6 Salle du Furnace
        catalogue.append(Piece(
            nom="Furnace",
            image_path='assets/images/rougeFurnace.png',
            rareté=2,
            cout_gemmes=0,
            portes={ 'S': True},
            lock_level=2, 
            objets={'pieces_or': -2,'cles': -1 },
            type_piece="Furnace"
        ))

         # 7 Salle du Darkroom
        catalogue.append(Piece(
            nom="Darkroom",
            image_path='assets/images/rougeDarkroom.png',
            rareté=2,
            cout_gemmes=3,
            portes={'S': True, 'E': True, 'O': True},
            lock_level=2, 
            objets={'pieces_or': 0, 'gemmes': -5,'cles': -1 },
            type_piece="tresor"
        ))
         # 8 Salle Closed
        catalogue.append(Piece(
            nom="Closed",
            image_path='assets/images/rougeClosed.png',
            rareté=2,
            cout_gemmes=3,
            portes={'S': True, 'E': True, 'O': True},
            lock_level=1, 
            objets={'pieces_or': -1, 'gemmes': 5,'cles': -2 },
            type_piece="tresor"
        ))


         # 9 Salle des Archives
        catalogue.append(Piece(
            nom="Archives",
            image_path='assets/images/rougeArchives.png',
            rareté=2,
            cout_gemmes=3,
            portes={'N': True, 'S': True, 'E': True, 'O': True},
            lock_level=3, 
            objets={'pieces_or': -2, 'gemmes': -5,'cles': +3 },
            type_piece="tresor"
        ))





        #  PIÈCES VIOLETTES 
        

         # 1 chambre d'inviter
        catalogue.append(Piece(
            nom="chambre d'invité",
            image_path='assets/images/vioinvites.png',
            rareté=1,
            cout_gemmes=1,
            portes={'S': True},
            lock_level=1, 
            objets={'gemmes': 10},
            type_piece="chambre"
        ))
        
        #2
        catalogue.append(Piece(
            nom="Boudoir",
            image_path='assets/images/vioboudoir.png',
            rareté=3,
            cout_gemmes=3,
            portes={'O': True, 'S': True,},
            lock_level=2, 
            objets={'gemmes': 5, 'pieces_or': 2,'marteau': 1},
            

            type_piece="violet"
        ))
         #3
        catalogue.append(Piece(
            nom="chambre",
            image_path='assets/images/viochambre.png',
            rareté=3,
            cout_gemmes=4,
            portes={'O': True, 'S': True},
            lock_level=2, 
            objets={'cles': 2, 'gemmes': 3,'pas':5},
            type_piece="violet"
        ))
        #4

        catalogue.append(Piece(
            nom="Quartier du serviteur",
            image_path='assets/images/vioServant.png',
            rareté=3,
            cout_gemmes=3,
            portes={ 'S': True},
            lock_level=1, 
            objets={'cles': 2,'patte_lapin': 1},

            type_piece="violet"
        ))
        #5

        catalogue.append(Piece(
            nom="Chevillere",
            image_path='assets/images/viochevillere.png',
            rareté=3,
            cout_gemmes=4,
            portes={'O': True, 'S': True},
            lock_level=2, 
            objets={'gemmes': 10, 'cles': 1},
            type_piece="violet"
        ))
        #6

        catalogue.append(Piece(
            nom="Chambreparentale",
            image_path='assets/images/viochambreparentale.png',
            rareté=3,
            cout_gemmes=3,
            portes={'S': True},
            lock_level=2, 
            objets={ 'gemmes': 5,'pas': -5},

            type_piece="violet"
        ))
        #7

        catalogue.append(Piece(
            nom="couchettes",
            image_path='assets/images/viocouchettes.png',
            rareté=3,
            cout_gemmes=2,
            portes={'S': True},
            lock_level=1, 
            objets={'pas':5,'marteau': 1},

            type_piece="violet"
        ))


        
           # PIÈCE MULTICOLORE SPÉCIALE 

        catalogue.append(Piece(
           nom="",
           image_path='assets/images/aquaruim.png',
           rareté=1,
           cout_gemmes=4,
           portes={'S': True, 'E': True, 'O': True},
           lock_level=3, 
           objets={'cles': 2, 'gemmes': 3, 'pieces_or': 5, 'pas': 10},
           type_piece="multicolor"
))



        
        
        return catalogue

    def get_pioche_initiale(self):
        return self.pieces_disponibles