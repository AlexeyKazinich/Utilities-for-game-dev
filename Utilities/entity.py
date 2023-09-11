import pygame




class Entity:
    """this is an entity that does not have an animation"""
    def __init__(self):
        pass
    
    def draw(self):
        pass
    


class AnimatedEntity(Entity):
    """this entity has an animation associated with it"""
    def __init__(self):
        pass
    
    def draw(self):
        pass
    
class PhysicsEntity(Entity):
    def __init__(self):
        pass
    
class CollidablePhysicsEntity(Entity):
    def __init__(self):
        pass

class CollidableEntity(Entity):
    def __init__(self):
        pass