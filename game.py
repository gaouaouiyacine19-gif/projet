# game.py

import pygame
import random
from manoir import Manoir
from joueur import Joueur
from inventere import Inventaire
from catalogue import CataloguePiece

STATE_DEPLACEMENT = 0
STATE_CHOIX_PIECE = 1
STATE_POPUP_PORTE = 2   # popup ouvrir porte / mur


class game:
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

        # État de jeu
        self.etat_jeu = STATE_DEPLACEMENT
        self.direction_visee = None

        # Cible pour nouvelle pièce
        self.cible_x = -1
        self.cible_y = -1
        self.pieces_proposees = []
        self.index_choix = 0
        self.direction_entree = None

        # Popup porte
        self.popup_lock_level = 0
        self.popup_cible_x = -1
        self.popup_cible_y = -1
        
        # --- NOUVELLE SECTION : FOND D'ÉCRAN PRINCIPAL (bleuprince.png) ---
        # 1. Définir la taille de l'écran (maintenant en attribut de la classe)
        self.largeur_ecran, self.hauteur_ecran = screen.get_size() 
        self.background_game_image = None
        
        try:
            # Le chemin d'accès inclut le dossier 'assets/images/'
            self.background_game_image = pygame.image.load('assets/images/bleuprince.png').convert_alpha()
            
            # Redimensionne l'image pour qu'elle couvre tout l'écran
            self.background_game_image = pygame.transform.scale(
                self.background_game_image, 
                (self.largeur_ecran, self.hauteur_ecran)
            )
        except pygame.error as e:
            print(f"Erreur de chargement de l'image de fond 'bleuprince.png': {e}")
            # Crée un fond noir de secours si l'image manque
            self.background_game_image = pygame.Surface((self.largeur_ecran, self.hauteur_ecran))
            self.background_game_image.fill((0, 0, 0)) 
        
        # ----------------------------------------------------

        # Images de fin de jeu (Bloc existant)
        self.img_win = None
        self.img_gameover = None
        try:
            self.img_win = pygame.image.load('assets/images/win.png').convert_alpha()
            self.img_win = pygame.transform.scale(
                self.img_win,
                (self.screen.get_width(), self.screen.get_height())
            )

            self.img_gameover = pygame.image.load('assets/images/gameover.png').convert_alpha()
            self.img_gameover = pygame.transform.scale(
                self.img_gameover,
                (self.screen.get_width(), self.screen.get_height())
            )
        except Exception:
            self.img_win = None
            self.img_gameover = None
            print("Avertissement: Images fin de jeu non trouvées.")

    # ----------------------
    # PIÈCES / CATALOGUE
    # ----------------------
    def _tirer_pieces(self):
        """Tire 3 pièces depuis le catalogue avec pondération sur la rareté."""
        pioche = self.catalogue.get_pioche_initiale()
        poids = [3 ** (3 - piece.rareté) for piece in pioche]

        if len(pioche) < 3:
            return []

        return random.choices(pioche, weights=poids, k=3)

    def _valider_choix_piece(self):
        """Place la pièce choisie, déduit le coût, déplace le joueur et exécute les effets."""
        piece_choisie = self.pieces_proposees[self.index_choix]
        
        # --- 1. VÉRIFICATION DU COÛT DE VERROUILLAGE (Clés) ---
        
        lock_level = getattr(piece_choisie, "lock_level", 0) 
        cles_consommees = 0

        if lock_level > 0:
            # Vérification de la ressource nécessaire (simplifié à Clés pour le lock_level de la pièce)
            if self.inventaire.cles < lock_level:
                print(f"❌ Pas assez de clés : il faut {lock_level} clé(s).")
                return # Bloque le placement
            
            # Consommation des clés
            self.inventaire.cles -= lock_level
            cles_consommees = lock_level
            print(f"🔑 {lock_level} clé(s) consommée(s) pour le placement.")

        
        # --- 2. VÉRIFICATION ET ALIGNEMENT DE LA ROTATION (Contrainte de la grille) ---
        
        # Déterminer la porte qui DOIT être ouverte sur la pièce choisie (la porte d'entrée)
        porte_attendue = None
        if self.direction_entree == pygame.K_z: 
           porte_attendue = 'S' # Mouvement Nord (Z) -> Attendre porte Sud (S)
        elif self.direction_entree == pygame.K_s: 
           porte_attendue = 'N' 
        elif self.direction_entree == pygame.K_q: 
           porte_attendue = 'E' 
        elif self.direction_entree == pygame.K_d: 
           porte_attendue = 'O' 

        if porte_attendue is not None:
            rotation_count = 0
            
            # Tente de tourner (max 4 fois) pour garantir la connexion
            while not piece_choisie.portes.get(porte_attendue, False) and rotation_count < 4:
                piece_choisie.rotate() 
                rotation_count += 1
                
            # Échec de l'alignement après 4 rotations
            if rotation_count == 4 and not piece_choisie.portes.get(porte_attendue, False):
                print(f"❌ ERREUR: La pièce {piece_choisie.nom} ne peut pas être alignée (pas de porte {porte_attendue}).")
                # Rendre les clés consommées si l'alignement échoue
                self.inventaire.cles += cles_consommees 
                return # Bloque le placement

        
        # --- 3. VÉRIFICATION DU COÛT EN GEMMES ---
        
        if self.inventaire.gemmes < piece_choisie.cout_gemmes:
           print("❌ Pas assez de gemmes pour cette pièce.")
           # Rendre les clés consommées si les gemmes manquent
           self.inventaire.cles += cles_consommees 
           return

        # Consommation des gemmes
        self.inventaire.gemmes -= piece_choisie.cout_gemmes


        # --- 4. PLACEMENT DE LA PIÈCE ET DÉPLACEMENT ---
        
        # Placer la pièce dans la map
        self.manoir.map[self.cible_y][self.cible_x] = piece_choisie
        
        # Déplacer le joueur
        self.joueur.x = self.cible_x
        self.joueur.y = self.cible_y
        
        # Marquer la pièce comme visitée
        piece_choisie.visitee = True


        # --- 5. APPLICATION DES OBJETS ET BONUS ---
        if piece_choisie.objets:
            # Gains/pertes de ressources
            self.inventaire.cles = max(0, self.inventaire.cles + piece_choisie.objets.get('cles', 0))
            self.inventaire.gemmes = max(0, self.inventaire.gemmes + piece_choisie.objets.get('gemmes', 0))
            self.inventaire.pieces_or = max(0, self.inventaire.pieces_or + piece_choisie.objets.get('pieces_or', 0))
            self.inventaire.pas += piece_choisie.objets.get('pas', 0)
            
            # Application des objets permanents
            if piece_choisie.objets.get('marteau'):
                self.inventaire.marteau = True
            if piece_choisie.objets.get('pelle'):
                self.inventaire.pelle = True
            if piece_choisie.objets.get('kit_crochetage'):
                self.inventaire.kit_crochetage = True
            if piece_choisie.objets.get('detecteur_metal'):
                self.inventaire.detecteur_metal = True
            if piece_choisie.objets.get('patte_lapin'):
                self.inventaire.patte_lapin = True

        print(f"✅ Pièce {piece_choisie.nom} placée et alignée.")

        # --- 6. RETOUR À L'ÉTAT DÉPLACEMENT ---
        self.etat_jeu = STATE_DEPLACEMENT
        self.pieces_proposees = []
        self.direction_entree = None

    def _afficher_choix_piece(self):
        w, h = self.screen.get_width(), self.screen.get_height()
        # Fond semi-transparent
        s = pygame.Surface((w, h))
        s.set_alpha(220)
        s.fill((0, 0, 0))
        self.screen.blit(s, (0, 0))

        font_titre = pygame.font.Font(None, 38)
        font = pygame.font.Font(None, 26)
        font_small = pygame.font.Font(None, 22)

        titre = font_titre.render("Choisissez une pièce (Q/D, Entrée pour valider)", True, (255, 255, 255))
        self.screen.blit(titre, (w // 2 - titre.get_width() // 2, 30))

        if not self.pieces_proposees:
            return

        carte_w, carte_h = 200, 200
        esp = 60
        total_w = 3 * carte_w + 2 * esp
        start_x = w // 2 - total_w // 2
        y = 100

        for i, piece in enumerate(self.pieces_proposees):
            x = start_x + i * (carte_w + esp)

            # Cadre sélectionné
            if i == self.index_choix:
                pygame.draw.rect(self.screen, (0, 255, 0), (x - 5, y - 5, carte_w + 10, carte_h + 160), 3)

            # Image
            img = piece.image
            if img is not None:
                img_scaled = pygame.transform.scale(img, (carte_w, carte_h))
                self.screen.blit(img_scaled, (x, y))
            else:
                pygame.draw.rect(self.screen, (80, 80, 80), (x, y, carte_w, carte_h))

            # Nom de la pièce
            txt_nom = font.render(piece.nom, True, (255, 255, 255))
            self.screen.blit(txt_nom, (x, y + carte_h + 5))

            # 🔐 LOCK_LEVEL (en gras et visible)
            lock = getattr(piece, "lock_level", 0)
            if lock > 0:
                txt_lock = font.render(f"Serrure : niveau {lock}", True, (255, 200, 0))
                self.screen.blit(txt_lock, (x, y + carte_h + 35))

            # 💎 Coût en gemmes
            txt_cout = font.render(f"Coût : {piece.cout_gemmes} gemme(s)", True, (0, 255, 255))
            self.screen.blit(txt_cout, (x, y + carte_h + 65))

            # 🎁 OBJETS (affichage clair des gains/pertes)
            objets = piece.objets
            if objets:
                y_obj = y + carte_h + 95
                txt_obj = font.render("Objets :", True, (200, 200, 255))
                self.screen.blit(txt_obj, (x, y_obj))
                y_obj += 25

                for nom, val in objets.items():
                    if val == 0:
                        continue

                    # signe pour +/-
                    signe = "+" if val > 0 else ""
                    couleur = (0, 255, 0) if val > 0 else (255, 100, 100)

                    txt = font_small.render(f"{signe}{val} {nom}", True, couleur)
                    self.screen.blit(txt, (x + 10, y_obj))
                    y_obj += 20



    # ----------------------
    # POPUP PORTE / MUR
    # ----------------------
    def _afficher_popup_porte(self):
        """Popup indiquant mur / porte verrouillée et ressource requise."""
        w, h = 460, 180
        x = self.screen.get_width() // 2 - w // 2
        y = self.screen.get_height() // 2 - h // 2

        s = pygame.Surface((w, h))
        s.set_alpha(230)
        s.fill((20, 20, 20))
        self.screen.blit(s, (x, y))

        font_titre = pygame.font.Font(None, 32)
        font_texte = pygame.font.Font(None, 26)

        lock = self.popup_lock_level

        if lock <= 0:
            t1 = "Mur / porte fermée."
            t2 = "Impossible de l'ouvrir. Appuyez sur N pour fermer."
        elif lock == 1:
            t1 = "Porte verrouillée (niveau 1)."
            t2 = "Il faut une CLÉ. Y = ouvrir, N = annuler."
        elif lock == 2:
            t1 = "Porte verrouillée (niveau 2)."
            t2 = "Il faut 1 Mrteau. Y = ouvrir, N = annuler."
        else:  # lock == 3
            t1 = " MUR "
            t2 = "Il faut une pelle pour creuser . Y = ouvrir, N = annuler."

        txt1 = font_titre.render(t1, True, (255, 255, 255))
        txt2 = font_texte.render(t2, True, (220, 220, 220))

        self.screen.blit(txt1, (x + 20, y + 40))
        self.screen.blit(txt2, (x + 20, y + 90))

    # game.py

    def _ouvrir_porte_popup(self):
        lock = self.popup_lock_level
        cible_x = self.popup_cible_x
        cible_y = self.popup_cible_y
        
        ouverture_succes = False # Variable pour suivre si l'ouverture a réussi

        # --- LOGIQUE D'OUVERTURE ---

        if lock == 1:
            if self.inventaire.cles >= 1:
                self.inventaire.cles -= 1
                print("Porte ouverte avec 1 CLÉ.")
                ouverture_succes = True
            else:
                print("Pas assez de CLÉS (niveau 1).")
                
        elif lock == 2:
            
            if self.inventaire.marteau: 
                print("Porte ouverte avec le MARTEAU.")
                ouverture_succes = True # Le marteau n'est PAS consommé
            else:
                print("Il faut le MARTEAU (niveau 2).")

        elif lock == 3: # LOGIQUE PELLE POUR LES MURS
            if self.inventaire.pelle: 
                print("Mur creusé avec succès (PELLE).")
                ouverture_succes = True
            else:
                print("Il faut la PELLE pour creuser (niveau 3).")
        
        # --- PHASE DE TRANSITION (Exécutée SEULEMENT si succès) ---

        if ouverture_succes:
            # 1. Préparer le choix de pièce (le mur est toujours une pièce inconnue)
            self.cible_x = cible_x
            self.cible_y = cible_y
            self.pieces_proposees = self._tirer_pieces()
            self.direction_entree = self.direction_visee
            self.index_choix = 0
            
            # 2. Changer l'état pour afficher le menu de choix
            self.etat_jeu = STATE_CHOIX_PIECE 
        else:
            # En cas d'échec, on retourne simplement à l'état de déplacement
            self.etat_jeu = STATE_DEPLACEMENT

        # Réinitialiser les variables du pop-up quelle que soit l'issue
        self.popup_lock_level = 0
        self.popup_cible_x = -1
        self.popup_cible_y = -1
    # ----------------------
    # BOUCLE PRINCIPALE
    # ----------------------
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN and not self.game_over and not self.win:

                    # ------- ÉTAT DÉPLACEMENT -------
                    if self.etat_jeu == STATE_DEPLACEMENT:

                        # 1. VISÉE (ZQSD)
                        if event.key in [pygame.K_z, pygame.K_q, pygame.K_s, pygame.K_d]:
                            resultat_visee = self.joueur.deplacer(
                                event.key, self.manoir, self.inventaire, validation=False
                            )
                            # On mémorise la direction seulement si mouvement possible (porte ouverte/limite)
                            self.direction_visee = event.key if resultat_visee else None

                        # 2. VALIDATION (ESPACE)
                        elif event.key == pygame.K_SPACE and self.direction_visee is not None:
                            resultat = self.joueur.deplacer(
                                self.direction_visee, self.manoir, self.inventaire, validation=True
                            )

                            if resultat is not None:

                                # CAS : Popup porte / mur (Vérification de verrouillage/ressources)
                                if resultat.get('popup_porte'):
                                    self.popup_cible_x = resultat['cible_x']
                                    self.popup_cible_y = resultat['cible_y']
                                    self.popup_lock_level = resultat['lock_level']
                                    self.etat_jeu = STATE_POPUP_PORTE

                                # CAS : nouvelle pièce (case inconnue)
                                elif resultat.get('nouvelle_piece'):
                                    self.cible_x = resultat['cible_x']
                                    self.cible_y = resultat['cible_y']
                                    self.pieces_proposees = self._tirer_pieces()
                                    self.etat_jeu = STATE_CHOIX_PIECE
                                    self.index_choix = 0
                                    self.direction_entree = self.direction_visee

                            # On réinitialise la direction visée
                            self.direction_visee = None

                    # ------- ÉTAT CHOIX PIECE -------
                    elif self.etat_jeu == STATE_CHOIX_PIECE:
                        if event.key == pygame.K_q and self.index_choix > 0:
                            self.index_choix -= 1
                        elif event.key == pygame.K_d and self.index_choix < len(self.pieces_proposees) - 1:
                            self.index_choix += 1
                        
                        # ROTATION MANUELLE AVEC 'R'
                        elif event.key == pygame.K_r:
                            piece_a_tourner = self.pieces_proposees[self.index_choix]
                            piece_a_tourner.rotate()
                            print(f"Rotation manuelle appliquée à la pièce : {piece_a_tourner.nom}")
                            
                        # VALIDER le choix (ENTRÉE)
                        elif event.key == pygame.K_RETURN:
                            self._valider_choix_piece()

                    # ------- ÉTAT POPUP PORTE / MUR -------
                    elif self.etat_jeu == STATE_POPUP_PORTE:
                        if event.key == pygame.K_y:
                            # On ne tente d'ouvrir que si lock_level > 0
                            if self.popup_lock_level > 0:
                                self._ouvrir_porte_popup()
                        elif event.key == pygame.K_n:
                            # annuler la popup
                            self.etat_jeu = STATE_DEPLACEMENT
                            self.popup_cible_x = -1
                            self.popup_cible_y = -1
                            self.popup_lock_level = 0

            # Victoire / Défaite (Logique)
            if self.inventaire.pas <= 0 and not self.win:
                self.game_over = True

            if self.joueur.x == 2 and self.joueur.y == 0:
                self.win = True

            # --- DÉBUT DE LA PHASE D'AFFICHAGE UNIQUE ---
            
            # 1. Fond (Image bleuprince.png ou couleur de secours)
            if self.background_game_image:
                self.screen.blit(self.background_game_image, (0, 0))
            else:
                self.screen.fill((30, 30, 40)) 
                
            # 2. Éléments du jeu (Dessiné par-dessus le fond)
            self.manoir.afficher(self.screen)
            self.joueur.afficher(self.screen)
            self.inventaire.afficher(self.screen)

            # 3. Menus et Popups (Dessiné par-dessus le jeu)
            if self.etat_jeu == STATE_CHOIX_PIECE:
                self._afficher_choix_piece()
            elif self.etat_jeu == STATE_POPUP_PORTE:
                self._afficher_popup_porte()

            # 4. Écran de fin de jeu (Dessiné par-dessus tout)
            if self.game_over and self.img_gameover:
                self.screen.blit(self.img_gameover, (0, 0))
            elif self.win and self.img_win:
                self.screen.blit(self.img_win, (0, 0))

            # --- FIN DE LA PHASE D'AFFICHAGE ---

            pygame.display.flip() # UN SEUL APPEL À FLIP À LA FIN
            self.clock.tick(60)