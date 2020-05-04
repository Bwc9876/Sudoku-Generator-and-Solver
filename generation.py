from math import sqrt
from solve import Check, CheckGrid
import pygame
from random import shuffle, randrange

pygame.init()
import constants
from classes import Solution_Tile


def Determine_Nets(sections, dimensions, tiles):
    t_x = 0
    m_x = 1
    m_y = 0
    t_y = 0
    track = 0
    for y in range(sections):
        if t_y == dimensions:
            m_y += dimensions
            t_y = 0
        for x in range(sections):
            if t_x == dimensions:
                m_x += 1
                t_x = 0
            tiles[track].net = int(m_x + m_y)
            t_x += 1
            track += 1
        t_y += 1
        m_x = 0
    return tiles


def Generate_Empty(sections):
    dimensions = sections / sqrt(sections)
    tiles = []
    tracker_y = 0
    for y in range(constants.SCREEN_SIZE[1]):
        tracker_x = 0
        for x in range(constants.SCREEN_SIZE[0]):
            square = Solution_Tile(y + 1, x + 1)
            tiles += [square]
            if tracker_x >= sections - 1:
                break
            tracker_x += 1
        if tracker_y >= sections - 1:
            break
        tracker_y += 1
    tiles = Determine_Nets(sections, dimensions, tiles)
    for i in tiles:
        i.number = 0
    return tiles


def Random_Fill(tiles):
    for x in tiles:
        if x.number == 0:
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            shuffle(nums)
            for y in nums:
                x.number = y
                if not Check(x, tiles):
                    x.number = y
                    if not CheckGrid(tiles):
                        return tiles
                    else:
                        if Random_Fill(tiles):
                            return tiles
            break
    x.number = 0


def Check_If_Possible(tiles):
    global counter
    for x in tiles:
        if x.number == 0:
            for y in range(1, 10):
                x.number = y
                if not Check(x, tiles):
                    x.number = y
                    if not CheckGrid(tiles):
                        counter += 1
                        break
                    else:
                        if Check_If_Possible(tiles):
                            return True
            break
    x.number = 0


def Remove_And_Check(tiles, diff):
    global counter
    attempts = diff
    while attempts > 0:
        print(attempts)
        to_remove = randrange(len(tiles))
        remember = tiles[to_remove].number
        while tiles[to_remove].number == 0:
            to_remove = randrange(len(tiles))
        counter = 0
        tiles[to_remove].number = 0
        copy = tiles
        Check_If_Possible(copy)
        if not counter == 1:
            tiles[to_remove].number = remember
            attempts -= 1
    return tiles


def Generate(sections, diff):
    a = Generate_Empty(sections)
    print('Generated Empty')
    b = Random_Fill(a)
    print('Filled')
    c = Remove_And_Check(b, diff)
    print('Done')
    return c
