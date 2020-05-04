import pygame
import constants


# noinspection PyArgumentList
class Tile:
    def __init__(self, sqr, static=False):
        self.sqr = sqr
        self.invalid = {'Row' : False, 'Col' : False, 'Net' : False}
        self.number = 0
        self.center = (self.sqr.width / 2 + self.sqr.left, self.sqr.height / 2 + self.sqr.top)
        self.pos = (self.sqr.left, self.sqr.top)
        self.static = static
        self.intersecting = []
        self.locked = False
        self.net = 0
        self.col = 0
        self.row = 0

    def Render_Number(self, screen):
        if not self.static:
            if not self.number == 0:
                if self.locked:
                    if True in self.invalid.values():
                        color = constants.INVALID
                    else:
                        color = constants.BLACK
                    num = constants.NUM_FONT.render(str(self.number), True, color)
                    screen.blit(num, (self.sqr.width / 4 + self.sqr.left, self.sqr.height / 4 + self.sqr.top))
                else:
                    num = constants.NUM_FONT.render(str(self.number), True, constants.GREY)
                    screen.blit(num, self.pos)

    def Re_Render(self, screen):
        if not self.number == 0:
            self.Clear(screen, reset=False)
            self.Render_Number(screen)

    def Determine_Truth(self, tiles, screen, invoked=False):
        flag = False
        for i in tiles:
            if not i == self:
                if not i.number == 0:
                    if i.locked:
                        if i.row == self.row and i.number == self.number:
                            self.invalid['Row'] = True
                            flag = True
                            if not invoked:
                                i.Determine_Truth(tiles, screen, invoked=True)
                                i.Re_Render(screen)
                        elif i.col == self.col and i.number == self.number:
                            self.invalid['Col'] = True
                            flag = True
                            if not invoked:
                                i.Determine_Truth(tiles, screen, invoked=True)
                                i.Re_Render(screen)
                        elif i.net == self.net and i.number == self.number:
                            self.invalid['Net'] = True
                            flag = True
                            if not invoked:
                                i.Determine_Truth(tiles, screen, invoked=True)
                                i.Re_Render(screen)
        if not flag:
            self.invalid['Col'] = False
            self.invalid['Row'] = False
            self.invalid['Net'] = False

    def Clear(self, screen, reset=True):
        if not self.static:
            if reset: self.number = 0
            pygame.draw.rect(screen, constants.WHITE, self.sqr)
            pygame.draw.rect(screen, constants.BLACK, self.sqr, width=1)

    def Lock_In(self, screen):
        if not self.static:
            if not self.locked:
                self.Clear(screen, reset=False)
                self.locked = True
                self.Render_Number(screen)

class Cursor:
    def __init__(self, sqr):
        self.sqr = sqr
        self.tile = None

class Solution_Tile:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.net = None
        self.number = 0