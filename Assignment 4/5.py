import sys
sys.setrecursionlimit(100000)

def has_cycle(undirected_graph):
	visited = [False] * num_vertex

	for node in undirected_graph.keys():
		if(not visited[node]):
			if(has_cycle_DFS(undirected_graph , node , visited , -1)):
				return True
	return False


def has_cycle_DFS(undirected_graph , node , visited , parent):
	visited[node] = True
	
	for adj_node in undirected_graph[node]:
		if(not visited[adj_node]):
			has_cycle_DFS(undirected_graph , adj_node , visited , node)
		elif(visited[adj_node] and adj_node != parent):
			return True
	return False


def DFS(undirected_graph , node , visited , edges , size_set_amount , traverse_nodes , vertices_set_size):
	visited[node] = True
	node_amount = size_set_amount

	for adj_node in undirected_graph[node]:
		if(not visited[adj_node]):
			if(adj_node in edges.keys()):
				if(node in edges[adj_node]):
					edges[adj_node].remove(node)
					
					if(len(edges[adj_node]) == 0):
						del edges[adj_node]

					traversed , increase = DFS(undirected_graph , adj_node , visited , edges , size_set_amount + 1 , [] , vertices_set_size)
					vertices_set_size[node] += increase
					size_set_amount += increase
					
					for seen_node in traverse_nodes:
						vertices_set_size[seen_node] += increase

					traverse_nodes.extend(traversed)			
			
				else:
					traversed , increase = DFS(undirected_graph , adj_node , visited , edges , size_set_amount , [] , vertices_set_size)
					for seen_node in traverse_nodes:
						vertices_set_size[seen_node] += increase + 1

					traverse_nodes.extend(traversed)
					size_set_amount += increase + 1
			
			else:
				traversed , increase = DFS(undirected_graph , adj_node , visited , edges , size_set_amount , [] , vertices_set_size)
				for seen_node in traverse_nodes:
					vertices_set_size[seen_node] += increase + 1
				traverse_nodes.extend(traversed)
				size_set_amount += increase + 1

	traverse_nodes.append(node)
	vertices_set_size[node] = size_set_amount

	return traverse_nodes , (size_set_amount - node_amount)




undirected_graph = {}
index_visits = {}
edges = {}

num_vertex , num_edges = list(map(int , input().split()))

for _ in range(num_edges):
	u , v = list(map(int , input().split()))
	u -= 1 ; v -= 1

	if(v in edges.keys()):
		edges[v].append(u)
	else:
		edges[v] = [u]

	if(u not in undirected_graph):
		undirected_graph[u] = [v]
	else:
		undirected_graph[u].append(v)

	if(v not in undirected_graph):
		undirected_graph[v] = [u]
	else:
		undirected_graph[v].append(u)

if(has_cycle(undirected_graph)):
	print(-1)
else:
	vertices_set_size = [0] * num_vertex
	visited = [False] * num_vertex
	parents = [-1] * num_vertex

	for node in undirected_graph.keys():
		if(not visited[node]):
			DFS(undirected_graph , node , visited , edges , 0 , [] , vertices_set_size)

	print(" ".join(map(str , vertices_set_size)))