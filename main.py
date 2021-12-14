import pygame
import random

#intialization display
pygame.init()
WIN_WIDTH = 1100
WIN_HEIGHT = 1100
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Chess")

#load images
pieces = [['0' for j in range(6)]for i in range(2)]
for i in range(2):
    for j in range(6):
        pieces[i][j] = pygame.image.load(f"./image/{i}{j}.png")

#chess board
board = [[[-1 for k in range(2)] for j in range(8)]for i in range(8)]

#colors
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
GRAY = [193, 162, 129]


def draw_board():

    for i in range(8):
        for j in range(8):
            x_ren = 100*(j+1)+10*j
            y_ren = 100*(i+1)+10*i
            pygame.draw.rect(WIN, GRAY, (x_ren, y_ren, 100, 100))
            if board[i][j][0] == -1: continue
            WIN.blit(pieces[board[i][j][0]][board[i][j][1]],(x_ren+25,y_ren)) 

    start_pos = [[80,80],[990,80],[990,990],[80,990]]
    pygame.draw.lines(WIN, WHITE, True, start_pos, 2)


def init_board():

    board[0][0] = [0,1]
    board[0][1] = [0,2]
    board[0][2] = [0,3]
    board[0][3] = [0,5]
    board[0][4] = [0,4]
    board[0][5] = [0,3]
    board[0][6] = [0,2]
    board[0][7] = [0,1]

    for x in range(8):
        board[1][x] = [0,0]

    board[7][0] = [1,1]
    board[7][1] = [1,2]
    board[7][2] = [1,3]
    board[7][3] = [1,5]
    board[7][4] = [1,4]
    board[7][5] = [1,3]
    board[7][6] = [1,2]
    board[7][7] = [1,1]
    
    for x in range(8):
        board[6][x] = [1,0]


def main():
    run = True
    init_board()

    while run:
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        
        WIN.fill(BLACK)
        draw_board()
        pygame.display.update()

if __name__ == '__main__':
    print("###########")
    print("#         #")
    print("####   ####")
    print("   #   #   ")
    print("   #####   ")
    main()