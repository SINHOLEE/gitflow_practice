A, B = map(int, input().split())
N, M = map(int, input().split())

board = [[0] * A for _ in range(B)]

# print(directopn['E'],directopn['E']["dy"],directopn['E']["dx"])
      # s e,n,w
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

robots = [[0,0,0] for _ in range(N+1)]
for i in range(1,N+1):
	x, y, d = map(str, input().split())
	if d == 'S':
		d = 0
	elif d == 'E':
  		d = 1
	elif d == 'N':
  		d = 2
	else:
  		d = 3

	robots[i] = [int(y) - 1, int(x) - 1, d]  # y, x , d
	board[int(y) - 1][int(x) - 1] = i

def turn_l(robot, rnd):
	y, x, d = robots[robot]
	d = (d + rnd) % 4
	robots[robot] = [y, x, d]

def turn_r(robot, rnd):
	y, x, d = robots[robot]
	d = (d - rnd) % 4
	robots[robot] = [y, x, d]


def get_message_f(robot, rnd):
	y, x, d = robots[robot]
	board[y][x] = 0
	for i in range(rnd):
		newY, newX = y + dy[d], x + dx[d]
		if not (0 <= newY < B and 0 <= newX < A):
			return 'Robot %d crashes into the wall' % robot
		if board[newY][newX]:
			return 'Robot %d crashes into robot %d' % (robot, board[newY][newX])
		y, x = newY, newX
	board[y][x] = robot
	robots[robot] = [y,x,d]
	return 0

print(robots)
print(board)
for i in range(M):
	robot, command, rnd = map(str, input().split())
	robot = int(robot)
	rnd = int(rnd)

	if (command == "F"):
		res = get_message_f(robot, rnd)
		if (res):
			break
		
	if (command == "L"):
		turn_l(robot,rnd)
	if (command == "R"):
		turn_r(robot, rnd)
	res = 'OK'
	print("=============")
	print(robot,command,rnd)
	print(robots)
	print(board)
print(res)


# 5 4
# 2 3
# 1 1 E
# 5 4 W
# 1 R 1
# 1 F 3
# 2 F 4