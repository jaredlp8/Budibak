import pygame
import Objects
import Behaviour
from pygame import mixer

WIDTH = 800
HEIGHT = 600
FPS = 60

BLUE = (60, 60, 120)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = 0




class Node:

    def __init__(self,value,next):
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

    def changeDimensions(self, height, width):
        screen = pygame.display.set_mode((width, height))
        return screen


class Level:

    def __init__ (self, name = "Default", objects = []):
        self.name = name
        self.listOfObjects = objects



    def getName(self):
        return self.name

    def get_objects(self):
        return self.listOfObjects

    def get_size(self):
        return len(self.listOfObjects)

    def updateObjects(self):
        for obj in self.listOfObjects:
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
        player_xright = player.get_x()+player.get_image().get_rect().size[0]
        player_xleft = player.get_x()
        player_yup = player.get_y()
        player_ydown = player.get_y()+player.get_image().get_rect().size[1]
        object_xright = object.get_x()+object.get_image().get_rect().size[0]
        object_xleft = object.get_x()
        object_yup = object.get_y()
        object_ydown = object.get_y()+object.get_image().get_rect().size[1]

        if (player_xright >= object_xleft and player_xleft <= object_xright) and (player_ydown >= object_yup
                                                                                  and player_yup <= object_ydown):
            if player.get_y() > object.get_y() and player_xright > object_xleft + 5 and player_xleft < object_xright-5:
                return 2
            if player.get_y() < object.get_y() and player_xright > object_xleft + 5 and player_xleft < object_xright-5:
                player.rect.y = object.rect.y - player.rect.size[1]
                return 3
            if player.get_x() < object.get_x():
                return 0
            if player.get_x() > object.get_x() :
                return 1

        return -1

    def collision(self,objects):
        player = "hero"
        mob = "villain"
        for index in range(len(objects)):
            if objects[index].get_type() == "character":
               player = objects[index]
        if player != "hero":
            has_left = False
            has_right = False
            has_up = False
            has_down = False
            for index in range(len(objects)):
                if objects[index].get_type() == "object":

                    side = self.collision_player_object(player, objects[index])
                    if side == 0 and not has_right:
                        has_right = True
                    if side == 1 and not has_left:
                        has_left = True
                    if side == 2 and not has_up:
                        has_up = True
                    if side == 3 and not has_down:
                        has_down = True
                    if player.get_y() > HEIGHT:
                        self.gameOver = True
                    if player.get_y() <= 0:
                        has_up = True
                    if player.get_x()+player.get_image().get_rect().size[0] >= WIDTH:
                        has_right = True
                    if player.get_x() <= 0:
                        has_left = True

                elif objects[index].get_type() == "mob":
                    if self.collision_player_object(player, objects[index])!=-1:
                        self.gameOver = True
                elif objects[index].get_type() == "goal":
                    if self.collision_player_object(player, objects[index]) != -1:
                        print ("completed")

                        self.LevelComplete = True
            player.get_coldirection()[0] = has_right
            player.get_coldirection()[1] = has_left
            player.get_coldirection()[2] = has_up
            player.get_coldirection()[3] = has_down
        for index in range(len(objects)):
            if objects[index].get_type() == "mob":
                mob = objects[index]
            if mob != "villain":
                has_left = False
                has_right = False
                has_up = False
                has_down = False
                for ind in range(len(objects)):
                    if objects[ind].get_type() == "object":

                        side = self.collision_player_object(mob, objects[ind])
                        if side == 0 and not has_right:
                            has_right = True
                        if side == 1 and not has_left:
                            has_left = True
                        if side == 2 and not has_up:
                            has_up = True
                        if side == 3 and not has_down:
                            has_down = True
                mob.get_coldirection()[0] = has_right
                mob.get_coldirection()[1] = has_left
                mob.get_coldirection()[2] = has_up
                mob.get_coldirection()[3] = has_down

    def add_sprites(self,current,all_sprites):

        for index in range(len(current.get_value().get_objects())):
            all_sprites.add(current.get_value().get_objects()[index])

        return all_sprites

    def update_level(self,current,all_sprites):
        current2 = current.get_next()
        if current2 == None:
            self.gameCompleted = True
        else:
            current = current2
            print(current)
            all_sprites.empty()
            all_sprites = self.add_sprites(current, pygame.sprite.Group())

        return all_sprites, current

    def run(self):
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Budibak Game")
        clock = pygame.time.Clock()
        mixer.music.load('music.mp3')
        mixer.music.play(-1)

        all_sprites = pygame.sprite.Group()

        self.add_sprites(self.current, all_sprites)

        running = True
        while running:

            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            all_sprites.update()
            screen.fill(BLUE)
            all_sprites.draw(screen)
            self.collision(self.current.get_value().get_objects())
            if self.LevelComplete:
                updates_values = self.update_level(self.current,all_sprites)
                all_sprites = updates_values[0]
                self.current = updates_values[1]
                if self.gameCompleted:
                    all_sprites.empty()
                    screen.fill(WHITE)
                    font = pygame.font.Font(None, 36)
                    text = font.render("You Win!!!", True, BLACK)
                    text_rect = text.get_rect()
                    text_x = screen.get_width() / 2 - text_rect.width / 2
                    text_y = screen.get_height() / 2 - text_rect.height / 2
                    screen.blit(text, [text_x, text_y])
                    all_sprites = self.update_level( self.current,all_sprites)
                    running = False
                self.LevelComplete = False

            if self.gameOver:
                mixer.music.stop()
                all_sprites.empty()
                screen.fill(BLACK)
                font = pygame.font.Font(None, 36)
                text = font.render("Game Over :(", True, WHITE)
                text_rect = text.get_rect()
                text_x = screen.get_width() / 2 - text_rect.width / 2
                text_y = screen.get_height() / 2 - text_rect.height / 2
                screen.blit(text, [text_x, text_y])

            pygame.display.flip()

        pygame.quit()
