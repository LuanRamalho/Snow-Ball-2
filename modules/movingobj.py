import gfxobject

# By Willi Kappler <grandor@gmx.de>
# Licensed under GPL

class MovingObj(gfxobject.GFXObject):
    "Main class for all the moving objects in the game"
    def __init__(self, screen, level, gfx, x, y):
        gfxobject.GFXObject.__init__(self, screen, level, gfx, x, y)

        self.horizontalMovement = 0
        self.verticalMovement = 0
        self.lastHorizontal = 0
        self.lastVertical = 0

        self.movingUp = -1
        self.movingLeft = -2
        self.turningLeft = -3
        self.lookingLeft = -4
        self.jumping = -5
        self.usingLift = -6
        self.climbingUp = -7

        self.movingDown = 1
        self.movingRight = 2
        self.turningRight = 3
        self.lookingRight = 4
        self.falling = 5
        self.climbingDown = 6

        self.borderX = 0
        self.calcHotSpots()

    def wallUp(self):
        if (self.leftSpotIn >= 0) and (self.rightSpotIn < 15) and (self.topSpotOut >= 0):
            t1 = self.level.frontData[self.topSpotOut][self.leftSpotIn]
            t2 = self.level.frontData[self.topSpotOut][self.rightSpotIn]
            return ((t1 > 0) and (t1 < self.level.doorOpened)) or ((t2 > 0) and (t2 < self.level.doorOpened))
        return True

    def wallDown(self):
        if (self.leftSpotIn >= 0) and (self.rightSpotIn < 15) and (self.bottomSpotOut < 15):
            t1 = self.level.frontData[self.bottomSpotOut][self.leftSpotIn]
            t2 = self.level.frontData[self.bottomSpotOut][self.rightSpotIn]
            return  ((t1 > 0) and (t1 < self.level.doorOpened)) or ((t2 > 0) and (t2 < self.level.doorOpened))
        return True

    def wallLeft(self):
        if (self.topSpotIn >= 0) and (self.bottomSpotIn < 15) and (self.leftSpotOut >= 0):
            t1 = self.level.frontData[self.topSpotIn][self.leftSpotOut]
            t2 = self.level.frontData[self.bottomSpotIn][self.leftSpotOut]
            return ((t1 > 0) and (t1 < self.level.doorOpened)) or ((t2 > 0) and (t2 < self.level.doorOpened))
        return True

    def wallRight(self):
        if (self.topSpotIn >= 0) and (self.bottomSpotIn < 15) and (self.rightSpotOut < 15):
            t1 = self.level.frontData[self.topSpotIn][self.rightSpotOut]
            t2 = self.level.frontData[self.bottomSpotIn][self.rightSpotOut]
            return ((t1 > 0) and (t1 < self.level.doorOpened)) or ((t2 > 0) and (t2 < self.level.doorOpened))
        return True

    def check(self):
        pass

    def move(self):
        pass

    def calcHotSpots(self):
        self.leftSpotIn = int((self.x + self.borderX) / 32)  # Garantir que o índice seja inteiro
        self.rightSpotIn = int((self.x + 31 - self.borderX) / 32)  # Garantir que o índice seja inteiro
        self.topSpotIn = int(self.y / 32)  # Garantir que o índice seja inteiro
        self.bottomSpotIn = int((self.y + 31) / 32)  # Garantir que o índice seja inteiro

        self.leftSpotOut = int((self.x - 1 + self.borderX) / 32)  # Garantir que o índice seja inteiro
        self.rightSpotOut = int((self.x + 32 - self.borderX) / 32)  # Garantir que o índice seja inteiro
        self.topSpotOut = int((self.y - 1) / 32)  # Garantir que o índice seja inteiro
        self.bottomSpotOut = int((self.y + 32) / 32)  # Garantir que o índice seja inteiro

        self.midX = int((self.x + 16) / 32)  # Garantir que o índice seja inteiro
        self.midY = int((self.y + 16) / 32)  # Garantir que o índice seja inteiro


    def centerTile(self):
        if (self.midY >= 0) and (self.midY < 15):
            if (self.midX >= 0) and (self.midX < 15):
                return self.level.frontData[self.midY][self.midX]
        return -1

    def leftTile(self):
        if (self.midY >= 0) and (self.midY < 15):
            if self.leftSpotOut >= 0:
                return self.level.frontData[self.midY][self.leftSpotOut]
        return -1

    def rightTile(self):
        if (self.midY >= 0) and (self.midY < 15):
            if self.rightSpotOut < 15:
                return self.level.frontData[self.midY][self.rightSpotOut]
        return -1

    def topTile(self):
        if (self.midX >= 0) and (self.midX < 15):
            if self.topSpotOut >= 0:
                return self.level.frontData[self.topSpotOut][self.midX]
        return -1

    def bottomTile(self):
        if (self.midX >= 0) and (self.midX < 15):
            if self.bottomSpotOut < 15:
                return self.level.frontData[self.bottomSpotOut][self.midX]
        return -1

    def topLeftTile(self):
        if (self.topSpotOut >= 0) and (self.leftSpotOut >= 0):
            return self.level.frontData[self.topSpotOut][self.leftSpotOut]
        return -1

    def topRightTile(self):
        if (self.topSpotOut >= 0) and (self.rightSpotOut < 15):
            return self.level.frontData[self.topSpotOut][self.rightSpotOut]
        return -1

    def bottomLeftTile(self):
        if (self.bottomSpotOut < 15) and (self.leftSpotOut >= 0):
            return self.level.frontData[self.bottomSpotOut][self.leftSpotOut]
        return -1

    def bottomRightTile(self):
        if (self.bottomSpotOut < 15) and (self.rightSpotOut < 15):
            return self.level.frontData[self.bottomSpotOut][self.rightSpotOut]
        return -1

    def leftLeftTile(self):
        if (self.midY >= 0) and (self.midY < 15):
            if self.leftSpotOut >= 1:
                return self.level.frontData[self.midY][self.leftSpotOut - 1]
        return -1

    def rightRightTile(self):
        if (self.midY >= 0) and (self.midY < 15):
            if self.rightSpotOut < 14:
                return self.level.frontData[self.midY][self.rightSpotOut + 1]
        return -1

    def bottomLeftLeftTile(self):
        if (self.bottomSpotOut < 15) and (self.leftSpotOut >= 1):
            return self.level.frontData[self.bottomSpotOut][self.leftSpotOut - 1]
        return -1

    def bottomRightRightTile(self):
        if (self.bottomSpotOut < 15) and (self.rightSpotOut < 14):
            return self.level.frontData[self.bottomSpotOut][self.rightSpotOut + 1]
        return -1

#    def bottomTile(self):
#        if (self.bottomSpotOut < 15) and (self.rightSpotIn < 15) and (self.leftSpotIn >= 0) and (self.rightSpotIn == self.leftSpotIn):
#            t = self.level.frontData[self.bottomSpotOut][self.leftSpotIn]
#            return t
#        return -1

    def go(self):
        self.calcHotSpots()
        self.check()
        self.move()
        self.animate()
        self.display()

    def restoreBG1(self):
        self.restoreBG3(self.level.displayXY)

    def restoreBG2(self):
        self.restoreBG3(self.level.displayXYBG)

    def restoreBG3(self, displayFunc):
        x1 = self.x / 32
        x2 = (self.x + 31) / 32
        y1 = self.topSpotIn
        y2 = self.bottomSpotIn
        if x1 == x2:
            if (y1 == y2) or (y2 == 15):
                displayFunc(x1, y1)
            else:
                displayFunc(x1, y1)
                displayFunc(x1, y2)
        else:
            if (y1 == y2):
                if x2 == 15:
                    displayFunc(x1, y1)
                else:
                    displayFunc(x1, y1)
                    displayFunc(x2, y1)
            else:
                displayFunc(x1, y1)
                displayFunc(x1, y2)
                displayFunc(x2, y1)
                displayFunc(x2, y2)
