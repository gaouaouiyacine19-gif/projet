import pygame

class Inventaire:
    def __init__(self):
        # La valeur que nous allons modifier
        self.pas = 70       
        self.gemmes = 2     
        self.cles = 0       
        # ... autres artefacts ...

    def perdre_pas(self, quantite=1):
        """Méthode pour décrémenter le compteur de pas."""
        self.pas -= quantite # <--- C'est ici que la valeur est changée

    def afficher(self, screen):
        """Affiche les artefacts, y compris la valeur de self.pas."""
        font = pygame.font.Font(None, 30) 
        start_x = 500
        start_y = 50
        line_height = 30
        
        # Le contenu du texte change à chaque tour de boucle avec la nouvelle valeur de self.pas
        artefacts = [
            (f"PAS: {self.pas}", (255, 255, 0)), 
            (f"GEMMES: {self.gemmes}", (0, 255, 255)),  
            (f"CLÉS: {self.cles}", (255, 100, 100)),    
        ]
        
        for index, (text_content, color) in enumerate(artefacts):
            text_surface = font.render(text_content, True, color)
            screen.blit(text_surface, (start_x, start_y + index * line_height))