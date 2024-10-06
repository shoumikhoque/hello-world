def if_exists(board, word):
    ROWS,COLS=len(board),len(board[0])
    path=set()
    def search_character(r,c,i):
        if i==len(word):
            return True
        if (r<0 or c<0 or r>=ROWS or c>=COLS or
            word[i]!=board[r][c] or (r,c )in path):
            return False
        path.add((r,c))
        res=(search_character(r+1,c,i+1) or
             search_character(r,c+1,i+1) )
        path.remove((r,c))
        return res
    for i in range(ROWS):
        for j in range(COLS):
            if search_character(i,j,0):
                return True
    return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(if_exists(board,word))