def solution(maps):
	n = len(maps)
	m = len(maps[0])
	visited = [[0] * m for _ in range(n)]
	dy = [0, 1, 0, -1]
	dx = [1, 0, -1, 0]
	visited[0][0] = 1
    queue = [[0, 0, 0]]
	res = -1
	while queue:
  		y, x, cnt = queue.pop(0)
		if (y == n - 1 and x == m - 1):
			res = cnt
			break
		for k in range(4):
			ny, nx = y + dy[k], x + dx[k]
			if visited[ny][nx] continue
			if not (0<=ny<n and 0<=nx<m) continue
			if not maps[ny][nx] continue
			visited[ny][nx]
			queue.append([ny, nx, cnt + 1])		
	return res



solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])