from typing import Callable
import pygame

class Rectangle:
    def __init__(self,
                 x,
                 y,
                 width,
                 height,
                 window, 
                 color: pygame.Color = pygame.Color(255,255,255))-> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.__rect = pygame.Rect(x,y,width,height)
        self.window = window

    def set_color(self,color:pygame.Color):
        self.color = color
    
    def draw(self)-> None:
        """a filled rectangle"""
        pygame.draw.rect(self.window,self.color,(self.x,self.y,self.width,self.height))
    
    def draw_box(self)-> None:
        """an outline of a rectangle"""
        pygame.draw.rect(self.window,self.color,(self.x,self.y,self.width,self.height),2)

    def collidepoint(self,locations: tuple) -> bool:
        """checks if the coords passed are colliding with this box"""
        self.__rect = pygame.Rect(self.x,self.y,self.width,self.height)
        return (self.__rect.collidepoint(locations))   

class RectButton:
    """a regular rectangular button that is drawn to the screen"""
    def __init__(self,
                 x,
                 y,
                 text,
                 window,
                 border_color: pygame.Color = pygame.Color('lightskyblue3'),
                 hover_color: pygame.Color = pygame.Color('deepskyblue1'), 
                 pressed_color: pygame.Color = pygame.Color('dodgerblue2'),
                 onclick_func: Callable = None) -> None:
        
        self.x = x
        self.y = y
        self.window = window
        
        self.text = text
        self.color = border_color
        self.text_color = (0,0,0)
        
        self.hover_color = hover_color
        self.active_color = pressed_color
        self.deactive_color = self.color
        self.text_deactive_color = self.text_color
        
        self.font = pygame.font.Font(None,32)
        self.textRender = self.font.render(self.text,True,self.text_color)
        self.width = self.textRender.get_width() + 10
        self.height = self.textRender.get_height() + 10
            
        self.__rectangle = Rectangle(self.x,self.y,self.width,self.height,self.window)
        self.__rectangle.set_color(self.color)
        
        self.onclick_func = onclick_func
        

        #mouse events
        self.pressed = False
        self.confirmed = False
        
    
    #checks if the button was pressed, sets the value to false to prevent the button from staying pressed
    def get_pressed(self) -> None:
        temp = self.pressed
        self.pressed = False
        return temp
    
    def align_on_x_axis(self, position: int = 1, amount: int = 1) -> None:
        """this will spread the buttons out evenly horizontally"""
        
        self.x = (self.window.get_width()*position / (amount +1)) - (self.width / 2)
        self.__rectangle.x = self.x
    
    def align_on_y_axis(self, position: int = 1, amount: int = 1) -> None:
        """this will spread the buttons out evenly vertically"""
        self.y = (self.window.get_height()*position / (amount +1)) - (self.height / 2)
        self.__rectangle.y = self.y
        self.x = self.window.get_width() // 2 - self.width // 2
        self.__rectangle.x = self.x
        
    def set_active(self)-> None:
        """swaps all the colors to the active_color"""
        self.color = self.active_color
        self.text_color = self.active_color
        self.__rectangle.set_color(self.active_color)

    def set_deactive(self)-> None:
        """swaps all the colors to the deactive_color"""
        self.color = self.deactive_color
        self.text_color = self.text_deactive_color
        self.__rectangle.set_color(self.deactive_color)
    
    def set_hover(self)-> None:
        """swaps all the colors to the hover_color"""
        self.color = self.hover_color
        self.text_color = self.hover_color
        self.__rectangle.set_color(self.hover_color)

    def set_color(self,color)-> None:
        """sets the button and text color"""
        self.color = pygame.Color(color)
        self.textColor = pygame.Color(color)


    def collidepoint(self,locations) -> bool:
        """returns bool if location is colliding with button"""
        return (self.__rectangle.collidepoint(locations))

            
        
    def draw(self) -> None:
        """draws the button"""
        #render text
        self.textRender = self.font.render(self.text,True,self.text_color)
        
        #draw the outline
        self.__rectangle.draw_box()

        #draw the text
        self.window.blit(self.textRender,(self.x+5,self.y+5))
    
    def logic_checks(self) -> None:
        """does all the logic for the button"""
        mouse_pos = pygame.mouse.get_pos() #mouse pos
        
        #if hovering
        if self.__rectangle.collidepoint(mouse_pos):
            self.set_hover()
            
            #if pressing
            if(pygame.mouse.get_pressed()[0]):
                self.set_active()
                self.pressed = True
                if self.onclick_func is not None:
                    self.onclick_func()
                else: self.pressed = False
        else: 
            self.set_deactive()
            



    
class TexturedButton:
    """button with an image"""
    def __init__(self, image, window, on_click_func: Callable=None):
        self.image = image
        self.x = 15
        self.y = 15
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image_original_size = (self.image.get_width(),self.image.get_height())
        self.window = window
        self.onclick_func = on_click_func
        self.rectangle = Rectangle(self.x,self.y,self.width,self.height,self.window)
        
        self.pressed = False
        self.hover = False 
        
    def set_active(self):
        self.image = pygame.transform.scale(self.image,(min(self.width*2,self.width + 1),min(self.height*2,self.height + 1)))

    
    def set_deactive(self):
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
    
    def draw(self):
        self.window.blit(self.image,(self.x,self.y))
        
        if self.hover:
            print(self.hover)
        else:
            print(self.hover)
    
    def logic_checks(self) -> None:
        """does all the logic for the button"""
        mouse_pos = pygame.mouse.get_pos() #mouse pos
        
        #if hovering
        if self.rectangle.collidepoint(mouse_pos):
            self.hover = True            
            #if pressing
            if(pygame.mouse.get_pressed()[0]):
                self.pressed = True
                self.set_active()
                if self.onclick_func is not None:
                    self.onclick_func()
                else: self.pressed = False
        else:
            self.hover = False
            self.set_deactive()

