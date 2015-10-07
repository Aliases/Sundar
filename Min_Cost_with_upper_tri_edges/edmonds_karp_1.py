from collections import deque
from copy import deepcopy

def bfs(n,s,t,Res_graph,Flow,parent):
	#parent array pre-initialized to -1 before every bfs call 

	print "Residual graph after entering into bfs is: ", Res_graph

	temp12=0

	#color coding scheme:
	#-1 for white
	#0 for gray
	#1 for black
	color = [-1 for x in range(n)]
	M = [1000 for x in range(n)] #1000 : very large number basically 
	color[s] = 0
	q = deque()
	q.append(s)
	while q:
		temp12 +=1 
		print "temp12 for while of bfs in max flow : ", temp12
		u = q.popleft()
		print "Enter here4", " and popped node is ", u 
		for v in range(0,n):
			print "Edge capacity in residual graph is: ", Res_graph[u][v], "for node ",u, " linked to node ", v 
			if Res_graph[u][v] > 0:
				if color[v] == -1 : #white edge 
					color[v] = 0  #color it gray
					parent[v] = u
					print "Enter here6"
					if v != t :
						print "Enter here3"
						q.append(v)
					else:
						break 
		color[u] = 1 #set color of this to black			

	#tracing parent to get list of capacities along the path found. Use this list to get bottleneck capacity
	w = t 

	#if no path found
	if parent[t] == -1:
		print "Enter here2"
		return 0

	#if path found 
	while w !=s :
		M[w] = Res_graph[parent[w]][w]
		w  = parent[w]
	return min(M)


def edmonds_karp(n,s,t,Capacity,Flow, max_possible_flow):
	maxFlow = 0
	f = max_possible_flow
	#defining residual graph
	Res_graph = deepcopy (Capacity)
	print "Res_graph is: ", Res_graph
	temp11=0 
	while 1: 
		temp11 +=1 
		print "temp11 for while of edmonds_karp: ", temp11

		parent = [-1 for x in range(n)]
		augment_flow = bfs(n,s,t,Res_graph,Flow,parent)
		flag = 0 
		if augment_flow == 0:
			print "I entered here1"
			break
		else:
			#For min, cost, following condition is required to ensure that source only supplies what it has
			if (maxFlow + augment_flow) > max_possible_flow:
				augment_flow = max_possible_flow - maxFlow
				flag = 1
			
			maxFlow += augment_flow			
			w = t 
			while w != s :
				Flow [parent[w]][w] += augment_flow
				Flow [w][parent[w]] -= augment_flow
				w = parent[w]
			print "Current flow matrix in current iteration is: ", Flow
				#Flow matrix done
			for i in range(n):
				for j in range(n):
					Res_graph[i][j] = Capacity[i][j] - Flow [i][j]
			print "Current capacity matrix is: ", Capacity
			print "Res_graph at end of every while loop iteration is: ", Res_graph
			if flag == 1:
				return maxFlow


	return maxFlow


