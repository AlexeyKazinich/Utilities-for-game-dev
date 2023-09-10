import pygame
import os



def load_image(path: str = "",colorkey: tuple = (0,0,0)) -> pygame.Surface:
    img = pygame.image.load(path)
    img.set_colorkey(colorkey)
    return img

def load_images(path: str = "", colorkey: tuple = (0,0,0)) -> list:
    images = []
    
    for img_name in os.listdir(path):
        images.append(load_image(path + img_name,colorkey))
    return images

class Animation:
    def __init__(self, images: list, img_dur: int = 5, loop:bool = True):
        self.images = images
        self.loop = loop
        self.img_duration = img_dur
        self.done = False
        self.frame = 0
        
    def update(self) -> None:
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True
    
    def img(self) -> pygame.Surface:
        return self.images[int(self.frame / self.img_duration)]