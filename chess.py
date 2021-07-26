def solution(n,m):


	dx = [1, 2, 2, 1]
	dy = [2, 1, -1, -2]

	dic = {}
	max_value = 0

	def go(y, x, cnt, visited):
		print(y, x, cnt, visited)
	
		if not (0 <= y < n and 0 <= x < m):
			return
		if (cnt <= 4):
			max_value = max(cnt, max_value)
		elif (sum(visited) == 4):
			max_value = max(cnt, max_value)
    
		for k in range(4):
			ny, nx = y + dy[k], x + dx[k]
			key = str(ny)+" "+str(nx)+" "+str(visited)
			if not (dic.get(key)):
				dic[key] = cnt
				visited[k] = 1
				go(ny, nx, cnt+1, visited)
				visited[k] = 0

	go(0,0,0,[0,0,0,0])


if __name__ == '__main__':
    n,m = map(int, input().split())
    solution(n,m)
    