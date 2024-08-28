def find_winner(board):
    pass
if __name__ == "__main__":
    t=int(input())
    board=[]
    for i in range(1,t+1):
        for j in range(3):
            board.append(input())
        winner = find_winner(board)
        print(f"Game #{i}: {winner}")
