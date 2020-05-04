import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (105,105,105)
INVALID = (255,0,0)
SELECTED = (135,206,250)
SCREEN_SIZE = [640, 640]
NUM_KEYS = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
NUMBER_TO_KEYS = {
pygame.K_0 : 0,
pygame.K_1 : 1,
pygame.K_2: 2,
pygame.K_3 : 3,
pygame.K_4 : 4,
pygame.K_5 : 5,
pygame.K_6 : 6,
pygame.K_7 : 7,
pygame.K_8 : 8,
pygame.K_9 : 9
}
CENTER = [int(SCREEN_SIZE[0] / 2), int(SCREEN_SIZE[1] / 2)]
NUM_FONT = pygame.font.SysFont("calibri", 60)