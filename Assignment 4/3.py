def convert2index(n , coordinates):
	dim = 13
	if(n == 1):
		return coordinates[0]
	elif(n == 2):
		return coordinates[1] * dim + coordinates[0]
	elif(n == 3):
		return coordinates[2] * (dim ** 2) + coordinates[1] * dim + coordinates[0]
	elif(n == 4):
		return coordinates[3] * (dim ** 3) + coordinates[2] * (dim ** 2) + coordinates[1] * dim + coordinates[0]
	# n == 5
	return coordinates[4] * (dim ** 4) + coordinates[3] * (dim ** 3) + coordinates[2] * (dim ** 2) + coordinates[1] * dim + coordinates[0]


def convert2coordinate(n , index):
	coordinates = []
	for i in range(n - 1 , -1 , -1):
		coordinate = index // (13 ** i)
		coordinates.append(coordinate)
		index -= (coordinate * (13 ** i))
	return coordinates[::-1]


def make_adjacency_list(n):
	adj_list = {}
	for node in range(13 ** n):
		adj_list[node] = []
		u = convert2coordinate(n , node)
		for i in range(n):
			v_1 = node + (13 ** i)
			v_2 = node - (13 ** i)
			if(u[i] == 0 and v_1 < 13 ** n and v_1 >= 0):
				adj_list[node].append(v_1)
			elif(u[i] == 12 and v_2 < 13 ** n and v_2 >= 0):
				adj_list[node].append(v_2)
			elif(v_1 < 13 ** n and v_1 >= 0 and v_2 < 13 ** n and v_2 >= 0):
				adj_list[node].append(node + (13 ** i))
				adj_list[node].append(node - (13 ** i))
	
	return adj_list


def BFS(start , target , adj_list , barriers , n):
	visited = [False] * (13 ** n)
	dist = [float("inf")] * (13 ** n)
	queue = []

	queue.append(start)
	visited[start] = True
	dist[start] = 0
	while(len(queue) != 0):
		u = queue.pop(0)
		for node in adj_list[u]:
			if(not visited[node] and not barriers[node]):
				queue.append(node)
				visited[node] = True
				dist[node] = dist[u] + 1
			
			if(visited[target]):
				return dist[target]
	
	return -1



n , m , x = list(map(int , input().split()))
barriers = [False] * (13 ** n)

for _ in range(m):
	barrier = list(map(int , input().split()))
	barrier = [coordinate + 6 for coordinate in barrier]
	barriers[convert2index(n , barrier)] = True

adj_list = make_adjacency_list(n)
print(BFS(convert2index(n , [6] * n) , convert2index(n , [x + 6] * n) , adj_list , barriers , n))
