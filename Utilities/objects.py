import pygame as pg

class Rectangle:
    def __init__(self,x,y,width,height,window, color: pg.Color = pg.Color(r=255,g=255,b=255,a=255))-> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.__rect = pg.Rect(x,y,width,height)
        self.window = window

    def set_color(self,color:pg.Color):
        self.color = color
    
    def draw(self)-> None:
        """a filled rectangle"""
        pg.draw.rect(self.window,self.color,(self.x,self.y,self.width,self.height))
    
    def draw_box(self)-> None:
        """an outline of a rectangle"""
        pg.draw.rect(self.window,self.color,(self.x,self.y,self.width,self.height),2)

    def collidepoint(self,locations: tuple) -> bool:
        """checks if the coords passed are colliding with this box"""
        self.__rect = pg.Rect(self.x,self.y,self.width,self.height)
        if(self.__rect.collidepoint(locations)):
            return True
        else:
            return False

class Button:
    def __init__(self,x,y,width,height,text,window,color: pg.Color = pg.Color('lightskyblue3'),text_color: pg.Color = pg.Color('lightskyblue3'), hover_color: pg.Color = pg.Color('deepskyblue1'), active_color: pg.Color = pg.Color('dodgerblue2'))-> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window
            
        self.text = text
        self.color = color
        self.text_color = text_color
        self.hover_color = hover_color
        self.active_color = active_color
        self.deactive_color = self.color
        self.font = pg.font.Font(None,32)
        self.__rectangle = Rectangle(self.x,self.y,self.width,self.height,window)
        self.__rectangle.set_color(self.color)
        

        #mouse events
        self.pressed = False
        self.confirmed = False
        self.hover = False
        
        


    #checks if the button was pressed, sets the value to false to prevent the button from staying pressed
    def get_pressed(self)-> None:
        temp = self.pressed
        self.pressed = False
        return temp
    
    def center_of_screen_x(self):
        self.x = (self.window.get_width() / 2) - (self.width / 2)
        
    def set_active(self)-> None:
        self.color = self.active_color
        self.text_color = self.active_color
        self.__rectangle.set_color(self.active_color)

    def set_deactive(self)-> None:
        self.color = self.deactive_color
        self.text_color = self.deactive_color
        self.__rectangle.set_color(self.deactive_color)
    
    def set_hover(self)-> None:
        self.color = self.hover_color
        self.text_color = self.hover_color
        self.__rectangle.set_color(self.hover_color)

    def set_color(self,color)-> None:
        self.color = pg.Color(color)
        self.textColor = pg.Color(color)


    def collidepoint(self,locations) -> bool:
        if(self.__rectangle.collidepoint(locations)):
            return True
        else:
            return False

    def draw(self)-> None:
        """draw the button"""
        #render the current font
        self.textRender = self.font.render(self.text,True,self.text_color)

        #draw the outline
        self.__rectangle.draw_box()

        #draw the text
        self.window.blit(self.textRender,(self.x+5,self.y+5))
    
    def update(self) -> None:
        """run this to draw the button as well as check for collisions"""
        self.draw()
        self.check_click()
    
    def check_click(self)-> None:
        mouse_pos = pg.mouse.get_pos() #mouse pos
        #if hovering
        if self.__rectangle.collidepoint(mouse_pos):
            self.hover = True
            self.set_hover()
        else: 
            self.hover = False
            self.set_deactive()
            
        #if clicking while hovering
        if(self.hover):
            if(pg.mouse.get_pressed()[0]):
                self.set_active()
                self.pressed = True
            else: self.pressed = False