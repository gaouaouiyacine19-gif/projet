import pygame

class Inventaire:
    def __init__(self):
        # --- Objets Consommables (Ressources / Colonne DROITE) ---
        self.pas = 70       
        self.pieces_or = 0  
        self.gemmes = 2     
        self.cles = 0       
        self.des = 0        
        
        # --- Objets Permanents (Équipement / Colonne GAUCHE) ---
        self.pelle = False          # Shovel (Pelle)
        self.marteau = False        # Hammer (Marteau)
        self.kit_crochetage = False # Lockpick Kit (Kit de crochetage)
        self.detecteur_metal = False 
        self.patte_lapin = False    

    def perdre_pas(self, quantite=1):
        """Décrémente le nombre de pas."""
        self.pas -= quantite 

    def afficher(self, screen):
        """Affiche l'inventaire dans deux colonnes distinctes."""
        
        font = pygame.font.Font(None, 24) 
        line_height = 25
        start_y = 50
        
        # --- 1. CONFIGURATION DE LA COLONNE DE DROITE (Ressources) ---
        # Cette colonne affichera les valeurs (Pas, Clés, Gemmes, etc.)
        X_RESSOURCES = 750
        
        ressources = [
            (self.pas, "PAS"),
            (self.cles, "CLÉS"),
            (self.des, "DÉS"),
            (self.gemmes, "GEMMES"),
            (self.pieces_or, "PIÈCES D'OR")
        ]
        
        y_pos = start_y
        
        # Affiche le titre de la section Ressources
        text_titre = font.render("RESSOURCES", True, (200, 200, 200))
        screen.blit(text_titre, (X_RESSOURCES, y_pos))
        y_pos += line_height * 2

        for valeur, nom in ressources:
            # Affiche la valeur (le chiffre)
            text_valeur = font.render(f"{valeur}", True, (255, 255, 255))
            screen.blit(text_valeur, (X_RESSOURCES, y_pos)) 
            
            # Affiche le nom de la ressource à côté pour référence rapide
            text_nom = font.render(nom, True, (150, 150, 150))
            screen.blit(text_nom, (X_RESSOURCES + 50, y_pos))
            
            y_pos += line_height

        # --- 2. CONFIGURATION DE LA COLONNE DE GAUCHE (Objets Permanents) ---
        # Cette colonne affichera le statut des objets (possédé ou non)
        X_PERMANENTS = 500
        
        permanents = [
            ("Pelle", self.pelle),
            ("Marteau", self.marteau),
            ("Kit de crochetage", self.kit_crochetage),
            ("Détecteur de métaux", self.detecteur_metal),
            ("Patte de lapin", self.patte_lapin),
        ]

        y_pos = start_y
        
        # Affiche le titre de la section Objets
        text_titre = font.render("OBJETS", True, (200, 200, 200))
        screen.blit(text_titre, (X_PERMANENTS, y_pos))
        y_pos += line_height * 2

        for nom, possede in permanents:
            couleur = (0, 255, 0) if possede else (150, 150, 150) # Vert si possédé, gris si non
            statut = "[X]" if possede else "[ ]"
            
            # Affichage du statut
            text_statut = font.render(statut, True, couleur)
            screen.blit(text_statut, (X_PERMANENTS, y_pos))
            
            # Affichage du nom
            text_nom = font.render(nom, True, couleur)
            screen.blit(text_nom, (X_PERMANENTS + 30, y_pos))
            
            y_pos += line_height