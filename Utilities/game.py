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
        self.draw()
        self.logic_checks()
    
    def draw(self):
        pass
    
    def logic_checks(self):
        while self.running:
            self.fps_counter.count_fps()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

                    
            self.draw()
            self.logic()
            
            # Update the display
            pygame.display.flip()
            self.clock.tick(60)