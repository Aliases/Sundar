from collections import deque

def std_bfs (Edge,s,color,parent,distance):
	n = len(Edge)

	#Color scheme:
	#White: -1. Gray : 0. Black: 1.
	for i in range(n):
		color[i] = -1	
		distance[i] = 0 
		parent[i] = -1

	color[s]= 0
	distance[s]= 0

	q = deque()
	q.append(s)
	while q:
		u = q.popleft()
		for v in range(n):
			if Edge[u][v] > 0:
				if color[v] == -1: #white, undiscovered edges
					color[v] == 0 #gray color it
					distance[v] += 1
					parent[v] = u
					q.append(v)
		color[u]=1 #color of u becomes black

def mod_bfs(Edge,s,parent,sink):
	n = len(Edge)

	#Color scheme:
	#White: -1. Gray : 0. Black: 1.
	color = [-1 for x in range(n)]
	for i in range(n):
		#color[i] = -1	
		#distance[i] = 0 
		parent[i] = -1

	color[s]= 0
	#distance[s]= 0

	q = deque()
	q.append(s)
	while q:
		u = q.popleft()
		for v in range(n):
			if Edge[u][v] > 0:
				if color[v] == -1: #white, undiscovered edges
					color[v] == 0 #gray color it
					#distance[v] += 1
					parent[v] = u
					q.append(v)
					if v in sink: #v is any unsaturated sink, then we stop here
						return v  #and get out of loop, nothing else needs to be done 
		color[u]=1 #color of u becomes black
	return -1 #no reachable unsat. sink found 

