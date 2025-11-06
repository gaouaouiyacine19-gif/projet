import pygame
from manoir import Manoir
from joueur import Joueur  # on ajoute cette ligne

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.manoir = Manoir()

        # position de départ du joueur
        self.joueur = Joueur(x=2, y=8, taille=self.manoir.cell_size)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.joueur.deplacer(event.key, self.manoir)

            self.screen.fill((30, 30, 40))
            self.manoir.afficher(self.screen)
            self.joueur.afficher(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
