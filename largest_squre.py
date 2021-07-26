def solution(board):
    n = len(board)
    m = len(board[0])
    answer = 0
    dp = [[0 for c in range(m)] for r in range(n)]
    for r in range(n):
        dp[r][0] = board[r][0]
    for c in range(m):
        dp[0][c] = board[0][c]
    
    for r in range(1, n):
        for c in range(1, m):
            if not board[r][c]:
                continue
            dp[r][c] = board[r][c] + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
  
    answer = max([max([dp[r][c] for c in range(m)]) for r in range(n)])
    return answer ** 2


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))

