import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.running = True
        self.clock = pygame.time.Clock()
     
    def run(self):
        while self.running:
            self.logic_checks()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
    
    def draw(self):
        self.screen.fill((255,255,255))
    
    def logic_checks(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
            
        # Update the display
        pygame.display.flip()
        self.clock.tick(60)