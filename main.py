import pygame
import random
from pygame.locals import *

#intialization display
pygame.init()
WIN_WIDTH = 1100
WIN_HEIGHT = 1100
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Chess")

#駒情報を読み出し、記憶する配列
pieces = [['0' for j in range(6)]for i in range(2)]
for i in range(2):
    for j in range(6):
        pieces[i][j] = pygame.image.load(f"./image/{i}{j}.png")

#盤面、選ばれた座標、駒の可動範囲を記憶する配列
board = [[[-1 for k in range(2)] for j in range(8)]for i in range(8)]
select_position = [[-1 for j in range(8)]for i in range(8)]
moveable_position = [[-1 for j in range(8)]for i in range(8)]

#色
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
GRAY = [193, 162, 129]
BLUE = [51, 255, 255]

#moveable_positionとboardをもとに盤面と選択されている駒、可動範囲を描画する
def draw_board():

    for i in range(8):
        for j in range(8):
            x_ren = 100*(j+1)+10*j
            y_ren = 100*(i+1)+10*i
            if moveable_position[i][j] == 1:
                pygame.draw.rect(WIN, BLUE, (x_ren, y_ren, 100, 100))
            else:
                pygame.draw.rect(WIN, GRAY, (x_ren, y_ren, 100, 100))

            if board[i][j][0] == -1: continue
            WIN.blit(pieces[board[i][j][0]][board[i][j][1]],(x_ren+25,y_ren)) 

    start_pos = [[80,80],[990,80],[990,990],[80,990]]
    pygame.draw.lines(WIN, WHITE, True, start_pos, 2)


#クリックされた座標が盤面上（８☓８）のどの領域にあるのか判断する
def judge_position(x, y):

    for i in range(8):
        for j in range(8):
            x_ren = 100*(j+1)+10*j
            y_ren = 100*(i+1)+10*i
            if x >= x_ren and x_ren+100 >= x and y >= y_ren and y_ren+100 >= y:
                select_position[i][j] = 1
            else:
                select_position[i][j] = -1


#select_positionをもとにクリックされた盤面上（８☓８）座標を取得する
def get_coordinate():

    for i in range(8):
        for j in range(8):
            if select_position[i][j] == 1:
                x_coordinate = j
                y_coordinate = i
    
    return (x_coordinate, y_coordinate)

    
#piecesと座標をもとに駒の種類を取得する
def get_type_pieces(x_now,y_now):

    type_pieces = pieces[board[y_now][x_now][0]][board[y_now][x_now][1]]

    return type_pieces


#select_boardをもとに選択された駒の可動範囲を判断する
def judge_moveable_position(first):
    
    for i in range(8):
        for j in range(8):
            moveable_position[i][j] = -1

    (x_now,y_now) = get_coordinate()
    
    if board[y_now][x_now][0] == first:
        moveable_position[y_now][x_now] = 1
        type_pieces = get_type_pieces(x_now, y_now)
        

#盤面情報の初期化
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
    first = 0
    init_board()

    while run:
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                judge_position(x,y)
                judge_moveable_position(first)
                
    
        WIN.fill(BLACK)
        draw_board()
        pygame.display.update()
        

if __name__ == '__main__':
    main()