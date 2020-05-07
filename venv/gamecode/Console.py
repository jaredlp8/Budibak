import pygame
import Objects
import Behaviour

WIDTH = 800
HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
BLUE = (60, 60, 120)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

size = 0


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


class Frame:

    def changeDimension(self, height, width):
        window = pygame.display.set_mode((width, height))
        return window


class Level:

    def __init__ (self, name = "Default", objects = []):
        self.name = name
        self.objectList = objects

    def getName(self):
        return self.name

    def get_objects(self):
        return self.objectList

    def get_size(self):
        return len(self.objectList)

    def updateObjects(self):
        for obj in self.objectList:
            obj.update()


current = "empty"


class Console:
    gameOver = False
    LevelComplete = False
    gameCompleted = False
    current = "void"

    def __init__(self):
        pass

    def set_current(self, current):
        self.current = current

    def collision_player_object(self,player,object):
        player_xRight=player.get_x()+player.get_image().get_rect().size[0]
        player_xLeft=player.get_x()
        player_yu=player.get_y()
        player_yd=player.get_y()+player.get_image().get_rect().size[1]
        object_xr=object.get_x()+object.get_image().get_rect().size[0]
        object_xl=object.get_x()
        object_yu = object.get_y()
        object_yd=object.get_y()+object.get_image().get_rect().size[1]
