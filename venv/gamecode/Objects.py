import Behaviour
import pygame


class Object(pygame.sprite.Sprite):

    def __init__(self, x, y, dynamic, image, behaviour):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.xSpeed = 0
        self.ySpeed = 0
        self.dynamic = dynamic
        self.image_link = image
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.xCenter = x
        self.rect.bottom = y
        self.behaviour = behaviour
        self.reflected = False
        self.totalMovement = 0

    def get_type(self):
        return "object"

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def dynamic(self):
        return self.dynamic

    def get_image(self):
        return self.image

    def get_image_link(self):
        return self.image_link

    def get_behaviour(self):
        return self.behaviour

    def set_x(self, x):
        self.x = self.rect.xCenter

    def set_y(self, y):
        self.y = self.rect.bottom

    def set_dynamic(self, dynamic):
        self.dynamic = dynamic

    def set_image(self, image):
        self.image_link = image

    def set_behaviour(self, behaviour):
        self.behaviour = behaviour

    def update(self):
        # x movement
        if not self.get_behaviour().get_x() == 0 and self.dynamic and not self.reflected:
            self.rect.x += self.get_behaviour().get_speed()
            self.totalMovement += self.get_behaviour().get_speed()
            if self.get_behaviour().get_x() < self.totalMovement:
                self.rect.x -= self.totalMovement - self.get_behaviour().get_x()
                self.totalMovement = self.get_behaviour().get_x()
                if self.behaviour.get_reflect():
                    self.totalMovement = 0
                    self.reflected = True
        elif not self.get_behaviour().get_x() == 0 and self.dynamic and self.reflected:
            self.rect.x -= self.get_behaviour().get_speed()
            self.totalMovement += self.get_behaviour().get_speed()
            if self.get_behaviour().get_x() < self.totalMovement:
                self.rect.x += self.totalMovement - self.get_behaviour().get_x()
                self.totalMovement = self.get_behaviour().get_x()
                if self.get_behaviour().get_reflect():
                    self.totalMovement = 0
                    self.reflected = False
        if self.get_behaviour().get_repeat() and self.totalMovement == self.get_behaviour().get_x():
            self.totalMovement = 0

        # y movement
        if not self.get_behaviour().get_y() == 0 and self.dynamic and not self.reflected:
            self.rect.y += self.get_behaviour().get_speed()
            self.totalMovement += self.get_behaviour().get_speed()
            if self.get_behaviour().get_y() < self.totalMovement:
                self.rect.y -= self.totalMovement - self.get_behaviour().get_y()
                self.totalMovement = self.get_behaviour().get_y()
                if self.get_behaviour().get_reflect():
                    self.totalMovement = 0
                    self.reflected = True
        elif not self.get_behaviour().get_y() == 0 and self.dynamic and self.reflected:
            self.rect.y -= self.get_behaviour().get_speed()
            self.totalMovement += self.get_behaviour().get_speed()
            if self.get_behaviour().get_y() < self.totalMovement:
                self.rect.y += self.totalMovement - self.get_behaviour().get_y()
                self.totalMovement = self.get_behaviour().get_y()
                if self.get_behaviour().get_reflect():
                    self.totalMovement = 0
                    self.reflected = False
        if self.get_behaviour().get_repeat() and self.totalMovement == self.get_behaviour().get_y():
            self.totalMovement = 0


class Goal(pygame.sprite.Sprite):

    def __init__(self, x, y, dynamic, image, behaviour):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.xSpeed = 0
        self.ySpeed = 0
        self.dynamic = dynamic
        self.image_link = image
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.xCenter = x
        self.rect.bottom = y
        self.behaviour = behaviour
        self.reflected = False
        self.totalMovement = 0

    def get_type(self):
        return "goal"

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def dynamic(self):
        return self.dynamic

    def get_image(self):
        return self.image

    def get_image_link(self):
        return self.image_link

    def get_behaviour(self):
        return self.behaviour

    def set_x(self, x):
        self.x = self.rect.xCenter

    def set_y(self, y):
        self.y = self.rect.bottom

    def set_dynamic(self, dynamic):
        self.dynamic = dynamic

    def set_image(self, image):
        self.image_link = image

    def set_behaviour(self, behaviour):
        self.behaviour = behaviour

    def update(self):
        # x movement
        if not self.get_behaviour().get_x() == 0 and self.dynamic and not self.reflected:
            self.rect.x += self.get_behaviour().get_speed()
            self.totalMovement += self.get_behaviour().get_speed()
            if self.get_behaviour().get_x() < self.totalMovement:
                self.rect.x -= self.totalMovement - self.get_behaviour().get_x()
                self.totalMovement = self.get_behaviour().get_x()
                if self.behaviour.get_reflect():
                    self.totalMovement = 0
                    self.reflected = True
        elif not self.get_behaviour().get_x() == 0 and self.dynamic and self.reflected:
            self.rect.x -= self.get_behaviour().get_speed()
            self.totalMovement += self.get_behaviour().get_speed()
            if self.get_behaviour().get_x() < self.totalMovement:
                self.rect.x += self.totalMovement - self.get_behaviour().get_x()
                self.totalMovement = self.get_behaviour().get_x()
                if self.get_behaviour().get_reflect():
                    self.totalMovement = 0
                    self.reflected = False
        if self.get_behaviour().get_repeat() and self.totalMovement == self.get_behaviour().get_x():
            self.totalMovement = 0

        # y movement
        if not self.get_behaviour().get_y() == 0 and self.dynamic and not self.reflected:
            self.rect.y += self.get_behaviour().get_speed()
            self.totalMovement += self.get_behaviour().get_speed()
            if self.get_behaviour().get_y() < self.totalMovement:
                self.rect.y -= self.totalMovement - self.get_behaviour().get_y()
                self.totalMovement = self.get_behaviour().get_y()
                if self.get_behaviour().get_reflect():
                    self.totalMovement = 0
                    self.reflected = True
        elif not self.get_behaviour().get_y() == 0 and self.dynamic and self.reflected:
            self.rect.y -= self.get_behaviour().get_speed()
            self.totalMovement += self.get_behaviour().get_speed()
            if self.get_behaviour().get_y() < self.totalMovement:
                self.rect.y += self.totalMovement - self.get_behaviour().get_y()
                self.totalMovement = self.get_behaviour().get_y()
                if self.get_behaviour().get_reflect():
                    self.totalMovement = 0
                    self.reflected = False
        if self.get_behaviour().get_repeat() and self.totalMovement == self.get_behaviour().get_y():
            self.totalMovement = 0


class Character(pygame.sprite.Sprite):

    def __init__(self, x, y, dynamic, image, behaviour):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.coldirection = [False, False, False, False]
        self.xSpeed = 0
        self.ySpeed = 0
        self.dynamic = dynamic
        self.image_link = image
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.xCenter = x
        self.rect.bottom = y
        self.behaviour = behaviour
        self.reflected = False
        self.totalMovement = 0
        self.canJump = False
        self.onplat = False

    def get_type(self):
        return "character"

    def get_coldirection(self):
        return self.coldirection

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def dynamic(self):
        return self.dynamic

    def get_image(self):
        return self.image

    def get_image_link(self):
        return self.image_link

    def get_behaviour(self):
        return self.behaviour

    def get_image(self):
        return self.image

    def set_x(self, x):
        self.x = self.rect.xCenter

    def set_coldirection(self, dir):
        self.coldirection = dir

    def set_y(self, y):
        self.y = self.rect.bottom

    def set_dynamic(self, dynamic):
        self.dynamic = dynamic

    def set_image_link(self, image_link):
        self.image_link = image_link

    def set_image(self, image):
        self.image = image

    def set_behaviour(self, behaviour):
        self.behaviour = behaviour

    def update(self):
        keystate = pygame.key.get_pressed()
        # x movement
        if keystate[pygame.K_a]:
            self.xSpeed += -1
            if self.xSpeed < -self.get_behaviour().get_speed():
                self.xSpeed = -self.get_behaviour().get_speed()
        if keystate[pygame.K_d] and not self.get_behaviour().get_x() == 0:
            self.xSpeed += 1
            if self.xSpeed > self.get_behaviour().get_speed():
                self.xSpeed = self.get_behaviour().get_speed()
        if (not keystate[pygame.K_a] and not keystate[pygame.K_d]) or (keystate[pygame.K_a] and keystate[pygame.K_d]):
            if self.xSpeed > 0:
                self.xSpeed -= .7
            if self.xSpeed < 0:
                self.xSpeed += .7
        # y movement through gravity
        if not self.get_behaviour().get_y() == 0 and self.get_behaviour().get_gravity():
            # self.ySpeed = 0
            if keystate[pygame.K_w] and self.canJump:
                self.ySpeed = -12
                self.canJump = False
                self.onplat = False
            self.ySpeed += .5
            if self.ySpeed > 10:
                self.ySpeed = 10
        # y movement through w and s
        elif not self.get_behaviour().get_y() == 0 and not self.get_behaviour().get_gravity():
            if keystate[pygame.K_w]:
                self.ySpeed = -self.get_behaviour().get_speed()
            if keystate[pygame.K_s]:
                self.ySpeed = self.get_behaviour().get_speed()
            if (not keystate[pygame.K_w] and not keystate[pygame.K_s]) or (
                    keystate[pygame.K_w] and keystate[pygame.K_s]):
                self.ySpeed = 0

        if self.coldirection[3] or self.coldirection[2]:
            if self.coldirection[3]:
                self.coldirection[2] = False
                self.onplat = True
                if keystate[pygame.K_w]:
                    self.rect.y -= 5
                    self.ySpeed = -12
                    self.onplat = False
                    self.coldirection[3] = False
            if self.coldirection[2]:
                self.ySpeed = 0
                self.onplat = False
                self.rect.y += 5
            if self.onplat:
                self.ySpeed = 0
                self.canJump = True

        if (self.coldirection[1] and keystate[pygame.K_a]) or (self.coldirection[0] and keystate[pygame.K_d]):
            self.xSpeed = 0

        if not self.coldirection[0] and not self.coldirection[1] and not self.coldirection[1] and not self.coldirection[
            1]:
            self.canJump = False
            self.onplat = False

        self.rect.x += self.xSpeed
        self.rect.y += self.ySpeed


class Enemies(pygame.sprite.Sprite):
    def __init__(self, x, y, dynamic, image, behaviour):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.coldirection = [False, False, False, False]
        self.xSpeed = 0
        self.ySpeed = 0
        self.dynamic = dynamic
        self.image_link = image
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.xCenter = x
        self.rect.bottom = y
        self.behaviour = behaviour
        self.reflected = False
        self.totalMovement = 0
        self.canJump = True
        self.onplat = False

    def get_type(self):
        return "enemy"

    def get_coldirection(self):
        return self.coldirection

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def dynamic(self):
        return self.dynamic

    def get_image_link(self):
        return self.image_link

    def get_image(self):
        return self.image

    def get_behaviour(self):
        return self.behaviour

    def set_x(self, x):
        self.x = self.rect.xCenter

    def set_y(self, y):
        self.y = self.rect.bottom

    def set_dynamic(self, dynamic):
        self.dynamic = dynamic

    def set_image_link(self, image):
        self.image_link = image

    def set_behaviour(self, behaviour):
        self.behaviour = behaviour

    def update(self):
        # x movement
        if not self.get_behaviour().get_x() == 0 and self.dynamic and not self.reflected:
            self.rect.x += self.get_behaviour().get_speed()
            self.totalMovement += self.get_behaviour().get_speed()
            if self.get_behaviour().get_x() < self.totalMovement:
                self.rect.x -= self.totalMovement - self.get_behaviour().get_x()
                self.totalMovement = self.get_behaviour().get_x()
                if self.behaviour.get_reflect():
                    self.totalMovement = 0
                    self.reflected = True
        elif not self.get_behaviour().get_x() == 0 and self.dynamic and self.reflected:
            self.rect.x -= self.get_behaviour().get_speed()
            self.totalMovement += self.get_behaviour().get_speed()
            if self.get_behaviour().get_x() < self.totalMovement:
                self.rect.x += self.totalMovement - self.get_behaviour().get_x()
                self.totalMovement = self.get_behaviour().get_x()
                if self.get_behaviour().get_reflect():
                    self.totalMovement = 0
                    self.reflected = False
        if self.get_behaviour().get_repeat() and self.totalMovement == self.get_behaviour().get_x():
            self.totalMovement = 0

        # y movement through no gravity
        if not self.get_behaviour().get_y() == 0 and self.dynamic and not self.reflected and not \
                self.get_behaviour().get_gravity():
            self.rect.y += self.get_behaviour().get_speed()
            self.totalMovement += self.get_behaviour().get_speed()
            if self.get_behaviour().get_y() < self.totalMovement:
                self.rect.y -= self.totalMovement - self.get_behaviour().get_y()
                self.totalMovement = self.get_behaviour().get_y()
                if self.get_behaviour().get_reflect():
                    self.totalMovement = 0
                    self.reflected = True
        elif not self.get_behaviour().get_y() == 0 and self.dynamic and self.reflected and not \
                self.get_behaviour().get_gravity():
            self.rect.y -= self.get_behaviour().get_speed()
            self.totalMovement += self.get_behaviour().get_speed()
            if self.get_behaviour().get_y() < self.totalMovement:
                self.rect.y += self.totalMovement - self.get_behaviour().get_y()
                self.totalMovement = self.get_behaviour().get_y()
                if self.get_behaviour().get_reflect():
                    self.totalMovement = 0
                    self.reflected = False
        if self.get_behaviour().get_repeat() and self.totalMovement == self.get_behaviour().get_y():
            self.totalMovement = 0
        # y movement through gravity
        if not self.get_behaviour().get_y() == 0 and self.get_behaviour().get_gravity() and not self.coldirection[3]:
            # self.ySpeed = 0
            self.ySpeed += .5
            if self.ySpeed > 10:
                self.ySpeed = 10

        if self.coldirection[3] or self.coldirection[2]:
            if self.coldirection[3]:
                self.coldirection[2] = False
                self.onplat = True
            if self.onplat:
                self.ySpeed = 0
        if not self.coldirection[3]:
            self.onplat = False

        if (self.coldirection[1] and self.reflected) or (self.coldirection[0] and not self.reflected):
            self.reflected = not self.reflected
            self.totalMovement = 0

        if not self.coldirection[0] and not self.coldirection[1] and not self.coldirection[1] and not \
                self.coldirection[1]:
            self.onplat = False

        self.rect.x += self.xSpeed
        self.rect.y += self.ySpeed
