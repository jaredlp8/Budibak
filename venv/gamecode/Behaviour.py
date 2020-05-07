class Behaviour:
    def __init__(self, xMovement, yMovement, speed, repetition, reflection, gravity):
        self.xMovement = xMovement
        self.yMovement = yMovement
        self.speed = speed
        self.repetition = repetition
        self.reflection = reflection
        self.gravity = gravity

    def getX(self):
        return self.xMovement

    def getY(self):
        return self.yMovement

    def getSpeed(self):
        return self.speed

    def getRepetition(self):
        return self.repetition

    def getReflection(self):
        return self.reflection

    def getGravity(self):
        return self.gravity

    def setX(self, xMovement):
        self.xMovement = xMovement

    def setY(self, yMovement):
        self.yMovement = yMovement

    def setSpeed(self, speed):
        self.speed = speed

    def setRepetition(self, repetition):
        self.repetition = repetition

    def setReflection(self, reflection):
        self.reflection = reflection

    def setGravity(self, gravity):
        self.gravity = gravity
