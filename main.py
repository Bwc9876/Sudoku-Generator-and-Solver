import pygame
pygame.init()
import constants
import generation
import solve
from classes import Tile, Cursor
from math import sqrt


# noinspection PyArgumentList
class GUI:
    def __init__(self):
        self.window = pygame.display.set_mode(constants.SCREEN_SIZE)
        self.complete = False
        self.clock = pygame.time.Clock()
        self.sections = 9
        self.moves = 0
        self.dimensions = self.sections / sqrt(self.sections)
        self.block_size = int(constants.SCREEN_SIZE[0] / self.sections)
        self.window.fill(constants.WHITE)
        self.tiles = []
        self.cursor = None
        self.Generate_Grid()
        self.Determine_Nets()
        self.Render_Grid()

    def Refresh(self):
        self.window.fill(constants.WHITE)
        self.Render_Grid()

    def Determine_Nets(self):
        t_x = 0
        m_x = 1
        m_y = 0
        t_y = 0
        track = 0
        for y in range(self.sections):
            if t_y == self.dimensions:
                m_y += self.dimensions
                t_y = 0
            for x in range(self.sections):
                if t_x == self.dimensions:
                    m_x += 1
                    t_x = 0
                self.tiles[track].net = int(m_x + m_y)
                t_x += 1
                track += 1
            t_y += 1
            m_x = 0


    def Render_Grid(self):
        for i in self.tiles:
            # noinspection PyArgumentList
            pygame.draw.rect(self.window, constants.BLACK, i.sqr, width=1)
        self.Render_Sections()

    def Render_Sections(self):
        section_lines = int(sqrt(self.sections))
        increment = int(constants.SCREEN_SIZE[0] / section_lines)
        for x in range(1, section_lines):
            pygame.draw.line(self.window, constants.BLACK, (0, increment * x),
                             (constants.SCREEN_SIZE[0], increment * x), width=5)
            pygame.draw.line(self.window, constants.BLACK, (increment * x, 0),
                             (increment * x, constants.SCREEN_SIZE[0]), width=5)

    def Clear_Tile(self, reset=True):
        self.cursor.tile.Clear(self.window, reset=reset)
        self.Render_Sections()


    def Generate_Grid(self):
        tracker_y = 0
        for y in range(constants.SCREEN_SIZE[1]):
            tracker_x = 0
            for x in range(constants.SCREEN_SIZE[0]):
                square = Tile(pygame.Rect(x * self.block_size, y * self.block_size, self.block_size, self.block_size))
                square.row = y + 1
                square.col = x + 1
                self.tiles += [square]
                if tracker_x >= self.sections - 1:
                    break
                tracker_x += 1
            if tracker_y >= self.sections - 1:
                break
            tracker_y += 1

    def Start(self, diff):
        made = generation.Generate(self.sections, diff)
        for i in range(len(self.tiles)):
            self.tiles[i].number = made[i].number
            if not self.tiles[i].number == 0:
                self.tiles[i].Render_Number(self.window)
                self.tiles[i].Lock_In(self.window)
                self.tiles[i].static = True
        self.Render_Sections()

    def MainLoop(self):
        while not self.complete:
            self.clock.tick(2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.complete = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for b in self.tiles:
                        if not b.static:
                            if b.sqr.collidepoint(pos):
                                if self.cursor is not None:
                                    self.Clear_Tile(reset=False)
                                    self.cursor.tile.Render_Number(self.window)
                                self.cursor = None
                                self.cursor = Cursor(b.sqr)
                                self.cursor.tile = b
                                pygame.draw.rect(self.window, constants.SELECTED, self.cursor.sqr)
                                self.cursor.tile.Render_Number(self.window)
                                break
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    if self.cursor is not None:
                        self.Clear_Tile(reset=False)
                        self.cursor.tile.Render_Number(self.window)
                        self.cursor = None
                elif event.type == pygame.KEYDOWN and event.key in constants.NUM_KEYS:
                    if self.cursor is not None and self.cursor.tile.locked is False:
                        self.cursor.tile.number = constants.NUMBER_TO_KEYS[event.key]
                        self.cursor.tile.Render_Number(self.window)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    if self.cursor is not None:
                        if not self.cursor.tile.number == 0:
                            self.Clear_Tile()
                            self.cursor.tile.locked = False
                            for i in self.tiles:
                                i.Determine_Truth(self.tiles, self.window, invoked=True)
                                i.Re_Render(self.window)
                            self.Render_Sections()
                            self.cursor = None
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if self.cursor is not None:
                        if not self.cursor.tile.number == 0:
                            self.cursor.tile.Lock_In(self.window)
                            self.cursor.tile.Determine_Truth(self.tiles, self.window)
                            self.cursor.tile.Re_Render(self.window)
                            print(self.cursor.tile.invalid)
                            self.Render_Sections()
                            self.cursor = None
                            self.moves += 1
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    for i in self.tiles:
                        if not i.locked:
                            i.number = 0
                            i.Clear(self.window)
                    self.tiles = solve.solve(self.tiles, self.window)
                    for i in self.tiles:
                        i.Render_Number(self.window)
                        i.Lock_In(self.window)
                    self.Render_Sections()

            pygame.display.update()
        print('Exiting...')
        pygame.quit()


def run(difficulty):
    UI = GUI()
    UI.Start(difficulty)
    UI.MainLoop()

if __name__ == '__main__':
    run(5)
