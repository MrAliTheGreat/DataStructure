import sys
sys.setrecursionlimit(100000)

def find_min_node(node , relations , cost_friendships , new_visited , min_cost_friendship , target_friend):
	new_visited[node] = True
	for friend in relations[node]:
		if(not new_visited[friend]):
			if(cost_friendships[friend] < min_cost_friendship):
				min_cost_friendship = cost_friendships[friend]
				target_friend = friend
			min_cost_friendship , target_friend = find_min_node(friend , relations , cost_friendships , new_visited , min_cost_friendship , target_friend)
	return min_cost_friendship , target_friend

def DFS(node , relations , visited , total_cost , k):
	visited[node] = True
	if(node in relations.keys()):
		for friend in relations[node]:
			if(not visited[friend]):
				total_cost = DFS(friend , relations , visited , total_cost , k)
	return total_cost + k

def find_friendship_cost(relations , cost_friendships , num_people , num_friendships , k):
	total_cost = 0
	visited = [False] * num_people
	
	for i in range(num_people):
		if(i not in relations.keys() or cost_friendships[i] < k):
			total_cost += cost_friendships[i]
			visited[i] = True

	for i in range(num_people):
		if(visited[i]):
			total_cost = DFS(i , relations , visited , total_cost - k , k)

	for i in range(num_people):
		if(not visited[i]):
			min_cost_friendship , target_friend = find_min_node(i , relations , cost_friendships , [False] * num_people , cost_friendships[i] , i)
			total_cost += min_cost_friendship
			total_cost = DFS(target_friend , relations , visited , total_cost - k , k)

	return total_cost



relations = {}
num_people , num_friendships , k = list(map(int , input().split()))
cost_friendships = list(map(int , input().split()))

for _ in range(num_friendships):
	person_1 , person_2 = list(map(int , input().split()))
	person_1 -= 1 ; person_2 -= 1
	if(person_1 not in relations.keys()):
		relations[person_1] = [person_2]
	else:
		relations[person_1].append(person_2)

	if(person_2 not in relations.keys()):
		relations[person_2] = [person_1]
	else:
		relations[person_2].append(person_1)

print(find_friendship_cost(relations , cost_friendships , num_people , num_friendships , k))
