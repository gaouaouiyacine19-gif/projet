# game.py (Code de la classe Game)

import pygame
import random
from manoir import Manoir
from joueur import Joueur
from inventere import Inventaire
from catalogue import CataloguePiece 

STATE_DEPLACEMENT = 0
STATE_CHOIX_PIECE = 1

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.manoir = Manoir()
        self.catalogue = self.manoir.catalogue

        # DÉPART: x=2, y=8 (Hall d'Entrée)
        self.joueur = Joueur(x=2, y=8, taille=self.manoir.cell_size) 
        self.inventaire = Inventaire()

        self.game_over = False
        self.win = False

        self.etat_jeu = STATE_DEPLACEMENT      
        self.direction_visee = None           
        self.cible_x = -1                     
        self.cible_y = -1                     
        self.pieces_proposees = []            
        self.index_choix = 0  
        self.direction_entree = None # par ou on rentrer 
                

        # Chargement des images de fin de jeu
        self.img_win = None
        self.img_gameover = None
        try:
            self.img_win = pygame.image.load('assets/images/win.png').convert_alpha()
            self.img_win = pygame.transform.scale(self.img_win, (self.screen.get_width(), self.screen.get_height()))
            self.img_gameover = pygame.image.load('assets/images/gameover.png').convert_alpha()
            self.img_gameover = pygame.transform.scale(self.img_gameover, (self.screen.get_width(), self.screen.get_height()))
        except:
            print("Avertissement: Images de fin de jeu (win.png/gameover.png) non trouvées.")



    def _tirer_pieces(self):
        """Tire trois pièces de la pioche en respectant les probabilités."""
        pioche = self.catalogue.get_pioche_initiale()
        poids = [3 ** (3 - piece.rareté) for piece in pioche]
            
        if len(pioche) < 3: 
            return []

        # Tirage avec poids
        pieces_tirees = random.choices(pioche, weights=poids, k=3)
        return pieces_tirees

    def _valider_choix_piece(self):
        """Place la pièce choisie, déduit le coût, déplace le joueur et exécute les effets."""
        piece_choisie = self.pieces_proposees[self.index_choix]

        # 🔄 1) Déterminer la face d'entrée (N/S/E/O) selon la direction d'entrée
        entree = None
        if self.direction_entree == pygame.K_z:   # tu montes
            entree = 'S'   # tu entres par le bas de la nouvelle pièce
        elif self.direction_entree == pygame.K_s: # tu descends
            entree = 'N'   # tu entres par le haut
        elif self.direction_entree == pygame.K_q: # tu vas à gauche
            entree = 'E'   # tu entres par la droite
        elif self.direction_entree == pygame.K_d: # tu vas à droite
            entree = 'O'   # tu entres par la gauche

        # 🔄 2) Faire tourner la pièce pour que la case d'entrée ait une porte ouverte
        if entree is not None:
            for _ in range(4):  # max 4 rotations
                if piece_choisie.portes.get(entree, False):
                    break
                piece_choisie.rotate()

        if self.inventaire.gemmes >= piece_choisie.cout_gemmes:
            self.inventaire.gemmes -= piece_choisie.cout_gemmes
            
            # Placement de la pièce et mouvement du joueur
            self.manoir.map[self.cible_y][self.cible_x] = piece_choisie
            self.joueur.x = self.cible_x
            self.joueur.y = self.cible_y
            
            # Exécuter les effets (collecte des objets)
            if piece_choisie.objets:
                self.inventaire.cles += piece_choisie.objets.get('cles', 0)
                self.inventaire.gemmes += piece_choisie.objets.get('gemmes', 0)
                self.inventaire.pieces_or += piece_choisie.objets.get('pieces_or', 0)
                # Si tu utilises des 'pas' dans objets :
                self.inventaire.pas += piece_choisie.objets.get('pas', 0)
            
            print(f"Pièce {piece_choisie.nom} placée. Nouveau total de clés: {self.inventaire.cles}")

            # Nettoyage et retour au mode déplacement
            self.etat_jeu = STATE_DEPLACEMENT
            self.pieces_proposees = []
            self.direction_entree = None
        else:
            print("Pas assez de gemmes pour cette pièce.")


    def _afficher_choix_piece(self):
        # ... (La méthode d'affichage du menu de choix est inchangée) ...
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        s = pygame.Surface((screen_width, screen_height))
        s.set_alpha(180)
        s.fill((0, 0, 0))
        self.screen.blit(s, (0, 0))

        font = pygame.font.Font(None, 30)
        menu_y_start = 50
        dessiner_texte = lambda txt, x, y, color: self.screen.blit(font.render(txt, True, color), (x, y))

        dessiner_texte("Choisissez une pièce (Q/D et ENTREE pour valider):", screen_width // 2 - 200, menu_y_start, (255, 255, 255))
        
        for i, piece in enumerate(self.pieces_proposees):
            
            x_pos = 100 + i * 250
            y_pos = menu_y_start + 50
            
            if i == self.index_choix:
                pygame.draw.rect(self.screen, (0, 255, 0), (x_pos - 5, y_pos - 5, 200, 200), 3) 
            
            if piece.image_path and piece.image_path in self.manoir.images and self.manoir.images[piece.image_path]:
                self.screen.blit(self.manoir.images[piece.image_path], (x_pos, y_pos))
            else:
                pygame.draw.rect(self.screen, (100, 100, 100), (x_pos, y_pos, 190, 190))

            dessiner_texte(piece.nom, x_pos, y_pos + 200, (255, 255, 255))
            dessiner_texte(f"Coût: {piece.cout_gemmes} Gemmes", x_pos, y_pos + 225, (0, 255, 255))
            dessiner_texte(f"Clés: {piece.objets.get('cles', 0)}", x_pos, y_pos + 250, (255, 255, 100))


    def run(self):
        while self.running: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.KEYDOWN and not self.game_over and not self.win:
                    
                    if self.etat_jeu == STATE_DEPLACEMENT:
                        
                        # 1. VISER une direction (ZQSD)
                        if event.key in [pygame.K_z, pygame.K_q, pygame.K_s, pygame.K_d]:
                            resultat_visee = self.joueur.deplacer(event.key, self.manoir, self.inventaire, validation=False)
                            self.direction_visee = event.key if resultat_visee else None
                            
                        # 2. VALIDER le mouvement avec ESPACE
                        elif event.key == pygame.K_SPACE and self.direction_visee is not None:
                            resultat = self.joueur.deplacer(self.direction_visee, self.manoir, self.inventaire, validation=True)

                            if resultat is not None and resultat.get('nouvelle_piece'):
                                self.cible_x = resultat.get('cible_x')
                                self.cible_y = resultat.get('cible_y')
                                self.pieces_proposees = self._tirer_pieces()
                                self.etat_jeu = STATE_CHOIX_PIECE
                                self.index_choix = 0
                          #  On mémorise la direction d'entrée pour la rotation
                                self.direction_entree = self.direction_visee
                            
                            self.direction_visee = None 


                    elif self.etat_jeu == STATE_CHOIX_PIECE:
                        # Gérer les touches du menu
                        if event.key == pygame.K_q and self.index_choix > 0: 
                            self.index_choix -= 1
                        elif event.key == pygame.K_d and self.index_choix < len(self.pieces_proposees) - 1: 
                            self.index_choix += 1
                        elif event.key == pygame.K_RETURN: 
                            self._valider_choix_piece()

            # --- Logique de victoire et défaite ---
            if self.inventaire.pas <= 0 and not self.win:
                self.game_over = True
            
            # Condition de victoire : Atteindre l'Antichambre (y=0, x=2)
            if self.joueur.x == 2 and self.joueur.y == 0:
                self.win = True

            # --- PHASE D'AFFICHAGE ---
            self.screen.fill((30, 30, 40))
            self.manoir.afficher(self.screen)
            self.joueur.afficher(self.screen) 
            self.inventaire.afficher(self.screen)
            
            if self.etat_jeu == STATE_CHOIX_PIECE:
                self._afficher_choix_piece()
            
            if self.game_over and self.img_gameover:
                self.screen.blit(self.img_gameover, (0, 0)) 
            elif self.win and self.img_win:
                self.screen.blit(self.img_win, (0, 0)) 
            
            pygame.display.flip()
            self.clock.tick(60)