
#選ばれている駒の可動範囲を検索する
def search_position(first, type_piece, x_now, y_now):
    print("seach_position")

    if type_piece == 0:
        search_pawn(first, x_now, y_now)   
    if type_piece == 1:
        search_rook(first, x_now, y_now)
    if type_piece == 2:
        search_knight(first, x_now, y_now)
    if type_piece == 3:
        search_bishop(first, x_now, y_now)
    if type_piece == 4:
        search_queen(first, x_now, y_now)
    if type_piece == 5:
        search_king(first, x_now, y_now)


#ポーンの移動範囲を検索する
def search_pawn(first, x_now, y_now):
    print("search_pawn")
    
    if first == 0:

        #初期位置のとき２マス進める
        if y_now == 1 and board[2][x_now][0] == -1 and board[3][x_now][0] == -1:
            movable_position[3][x_now] = 1
        
        #駒が存在しないとき1マス進める
        x_next = x_now
        y_next = y_now + 1
        if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) == -1:
            movable_position[y_next][x_next] = 1
        
        #敵の駒があるとき進める
        x_next = x_now + 1
        if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) == 1:
            movable_position[y_next][x_next] = 1

        #敵の駒があるとき進める
        x_next = x_now - 1
        if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) == 1:
            movable_position[y_next][x_next] = 1
    
    else:
        #初期位置のとき２マス進める
        if y_now == 6 and board[5][x_now][0] == -1 and board[4][x_now][0] == -1:
            movable_position[4][x_now] = 1
        
        #駒が存在しないとき1マス進める
        x_next = x_now
        y_next = y_now - 1
        if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) == -1:
            movable_position[y_next][x_next] = 1
        
        #敵の駒があるとき進める
        x_next = x_now + 1
        if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) == 0:
            movable_position[y_next][x_next] = 1

        #敵の駒があるとき進める
        x_next = x_now - 1
        if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) == 0:
            movable_position[y_next][x_next] = 1


#ルークの移動範囲を検索する
def search_rook(first, x_now, y_now):
    
    if first == 0:

        for i in range(4):
            x_next = x_now
            y_next = y_now
            OK = True
            while(OK):
                OK = False
                if i == 0: y_next -= 1
                if i == 1: y_next += 1
                if i == 2: x_next += 1
                if i == 3: x_next -= 1
                if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) != 0:
                    movable_position[y_next][x_next] = 1
                    OK = get_existence(x_next, y_next) != 1

    else:

        for i in range(4):
            x_next = x_now
            y_next = y_now
            OK = True
            while(OK):
                OK = False
                if i == 0: y_next -= 1
                if i == 1: y_next += 1
                if i == 2: x_next += 1
                if i == 3: x_next -= 1
                if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) != 1:
                    movable_position[y_next][x_next] = 1
                    OK = get_existence(x_next, y_next) != 0


#ナイトの移動範囲を検索する
def search_knight(first, x_now, y_now):
    
    if first == 0:

        for i in range(4):
            for j in range(2):
                x_next = x_now
                y_next = y_now
                if i == 0 and j == 0: y_next, x_next = y_next+2, x_next+1
                if i == 0 and j == 1: y_next, x_next = y_next+1, x_next+2
                if i == 1 and j == 0: y_next, x_next = y_next+2, x_next-1
                if i == 1 and j == 1: y_next, x_next = y_next+1, x_next-2
                if i == 2 and j == 0: y_next, x_next = y_next-2, x_next-1
                if i == 2 and j == 1: y_next, x_next = y_next-1, x_next-2
                if i == 3 and j == 0: y_next, x_next = y_next-2, x_next+1
                if i == 3 and j == 1: y_next, x_next = y_next-1, x_next+2
                if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) != 0:
                    movable_position[y_next][x_next] = 1
    else:
        
        for i in range(4):
            for j in range(2):
                x_next = x_now
                y_next = y_now
                if i == 0 and j == 0: y_next, x_next = y_next+2, x_next+1
                if i == 0 and j == 1: y_next, x_next = y_next+1, x_next+2
                if i == 1 and j == 0: y_next, x_next = y_next+2, x_next-1
                if i == 1 and j == 1: y_next, x_next = y_next+1, x_next-2
                if i == 2 and j == 0: y_next, x_next = y_next-2, x_next-1
                if i == 2 and j == 1: y_next, x_next = y_next-1, x_next-2
                if i == 3 and j == 0: y_next, x_next = y_next-2, x_next+1
                if i == 3 and j == 1: y_next, x_next = y_next-1, x_next+2
                if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) != 1:
                    movable_position[y_next][x_next] = 1

#ビショップの移動範囲を検索する
def search_bishop(first, x_now, y_now):
    
    if first == 0:

        for i in range(4):
            x_next = x_now
            y_next = y_now
            OK = True
            while(OK):
                OK = False
                if i == 0: y_next, x_next = y_next+1, x_next+1
                if i == 1: y_next, x_next = y_next-1, x_next-1
                if i == 2: y_next, x_next = y_next+1, x_next-1
                if i == 3: y_next, x_next = y_next-1, x_next+1
                if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) != 0:
                    movable_position[y_next][x_next] = 1
                    OK = get_existence(x_next, y_next) != 1
    
    else:

        for i in range(4):
            x_next = x_now
            y_next = y_now
            OK = True
            while(OK):
                OK = False
                if i == 0: y_next, x_next = y_next+1, x_next+1
                if i == 1: y_next, x_next = y_next-1, x_next-1
                if i == 2: y_next, x_next = y_next+1, x_next-1
                if i == 3: y_next, x_next = y_next-1, x_next+1
                if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) != 1:
                    movable_position[y_next][x_next] = 1
                    OK = get_existence(x_next, y_next) != 0


#クイーンの移動範囲を検索する
def search_queen(first, x_now, y_now):
    
    if first == 0:

        for i in range(8):
            x_next = x_now
            y_next = y_now
            OK = True
            while(OK):
                OK = False
                if i == 0: y_next -= 1
                if i == 1: y_next += 1
                if i == 2: x_next += 1
                if i == 3: x_next -= 1
                if i == 4: y_next, x_next = y_next+1, x_next+1
                if i == 5: y_next, x_next = y_next-1, x_next-1
                if i == 6: y_next, x_next = y_next+1, x_next-1
                if i == 7: y_next, x_next = y_next-1, x_next+1
                if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) != 0:
                    movable_position[y_next][x_next] = 1
                    OK = get_existence(x_next, y_next) != 1
    else:

        for i in range(8):
            x_next = x_now
            y_next = y_now
            OK = True
            while(OK):
                OK = False
                if i == 0: y_next -= 1
                if i == 1: y_next += 1
                if i == 2: x_next += 1
                if i == 3: x_next -= 1
                if i == 4: y_next, x_next = y_next+1, x_next+1
                if i == 5: y_next, x_next = y_next-1, x_next-1
                if i == 6: y_next, x_next = y_next+1, x_next-1
                if i == 7: y_next, x_next = y_next-1, x_next+1
                if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) != 1:
                    movable_position[y_next][x_next] = 1
                    OK = get_existence(x_next, y_next) != 0


#キングの移動範囲を検索する
def search_king(first, x_now, y_now):

    if first == 0:

        for i in range(8):
            x_next = x_now
            y_next = y_now
            if i == 0: y_next -= 1
            if i == 1: y_next += 1
            if i == 2: x_next += 1
            if i == 3: x_next -= 1
            if i == 4: y_next, x_next = y_next+1, x_next+1
            if i == 5: y_next, x_next = y_next-1, x_next-1
            if i == 6: y_next, x_next = y_next+1, x_next-1
            if i == 7: y_next, x_next = y_next-1, x_next+1
            if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) != 0:
                movable_position[y_next][x_next] = 1
                OK = get_existence(x_next, y_next) != 1
    else:
        for i in range(8):
            x_next = x_now
            y_next = y_now
            if i == 0: y_next -= 1
            if i == 1: y_next += 1
            if i == 2: x_next += 1
            if i == 3: x_next -= 1
            if i == 4: y_next, x_next = y_next+1, x_next+1
            if i == 5: y_next, x_next = y_next-1, x_next-1
            if i == 6: y_next, x_next = y_next+1, x_next-1
            if i == 7: y_next, x_next = y_next-1, x_next+1
            if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) != 1:
                movable_position[y_next][x_next] = 1
                OK = get_existence(x_next, y_next) != 0