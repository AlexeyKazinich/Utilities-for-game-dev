#this file will have the game state manager and the screens that can be inherited from
import pygame
import sys


class Screen:
    def __init__(self, window):
        self.window = window
        
    def logic_checks(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
        
    def draw(self):
        self.window.fill((255,0,0))
        pygame.display.flip()
    
    def quit(self) -> None:
        """quits the game and closes the window"""
        self.running = False
        pygame.quit()
        sys.exit()
    
    
    
    
class ScreenManager:
    """this is the default implementation of the screen manager which will allow to swap between screens"""
    def __init__(self, window):
        self.window = window
        self.current_screen = "game"
        self.screen = {
            "game": GameScreen(self.window)
        }
        
    def draw(self):
        self.screen[self.current_screen].draw()
        
    def logic_checks(self):
        self.screen[self.current_screen].logic_checks()




class GameScreen(Screen):
    """this is a default implementation of a game screen that uses tiles as the map"""
    def __init__(self,window):
        super().__init__(window)
        
    def draw(self):
        self.window.fill((255,255,255))
        pygame.display.flip()
    
    def logic_checks(self):
        super().logic_checks()