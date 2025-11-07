import pygame

class Inventaire:
    def __init__(self):
        # --- Objets Consommables (Ressources) ---
        self.pas = 70       
        self.pieces_or = 0  
        self.gemmes = 2     
        self.cles = 0       
        self.des = 0        
        
        # --- Objets Permanents (Équipement) ---
        self.pelle = False          
        self.marteau = False        
        self.kit_crochetage = False 
        self.detecteur_metal = False 
        self.patte_lapin = False    

    def perdre_pas(self, quantite=1):
        self.pas -= quantite 

    def afficher(self, screen):
        """Affiche l'inventaire dans deux colonnes distinctes."""
        
        font = pygame.font.Font(None, 24) 
        line_height = 25
        start_y = 50
        
        X_PERMANENTS = 500
        X_RESSOURCES = 750
        
        # 1. AFFICHAGE DES RESSOURCES (Colonne DROITE)
        ressources = [
            (self.pas, "PAS"), (self.cles, "CLÉS"), (self.des, "DÉS"),
            (self.gemmes, "GEMMES"), (self.pieces_or, "PIÈCES D'OR")
        ]
        y_pos = start_y
        dessiner_ligne = lambda txt, x, y, color: screen.blit(font.render(txt, True, color), (x, y))

        dessiner_ligne("RESSOURCES", X_RESSOURCES, y_pos, (200, 200, 200))
        y_pos += line_height * 2

        for valeur, nom in ressources:
            dessiner_ligne(f"{valeur}", X_RESSOURCES, y_pos, (255, 255, 255))
            dessiner_ligne(nom, X_RESSOURCES + 50, y_pos, (150, 150, 150))
            y_pos += line_height

        # 2. AFFICHAGE DES OBJETS PERMANENTS (Colonne GAUCHE)
        permanents = [
            ("Pelle", self.pelle), ("Marteau", self.marteau),
            ("Kit de crochetage", self.kit_crochetage), ("Détecteur de métaux", self.detecteur_metal),
            ("Patte de lapin", self.patte_lapin),
        ]

        y_pos = start_y
        dessiner_ligne("OBJETS", X_PERMANENTS, y_pos, (200, 200, 200))
        y_pos += line_height * 2

        for nom, possede in permanents:
            couleur = (0, 255, 0) if possede else (150, 150, 150)
            statut = "[X]" if possede else "[ ]"
            
            dessiner_ligne(statut, X_PERMANENTS, y_pos, couleur)
            dessiner_ligne(nom, X_PERMANENTS + 30, y_pos, couleur)
            y_pos += line_height