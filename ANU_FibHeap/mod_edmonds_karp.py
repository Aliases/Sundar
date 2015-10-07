from copy import copy, deepcopy #to copy matrices 
from max_augmenting_path import max_aug_flow
from random import randint

#takes as input capacity matrix, no. of vertices, source, sink, 

def edmonds_karp(n,s,t,Capacity,Flow):
	maxFlow=0
	#parent = [-1 for x in range(n)]
	iter_no=0

	#print "Capacity matrix: ", Capacity
	#Make edge matrix:
	Edge  = [[0 for x in range(n)] for x in range(n)]
	for i in range(0,n):
		for j in range(0,n):
			if Capacity[i][j] < 0:
				Edge[i][j] = 1
				
	

	Res_graph = deepcopy (Capacity)
	while 1 :
	#while x < 10:
		print "iteration number: ", iter_no

		iter_no +=1

		parent = [-1 for x in range(n)]
		augmented_flow = max_aug_flow(n,s,t,Res_graph, Flow,parent)
		print "parent here1: ", parent
		if augmented_flow == 0:
			break
		maxFlow += augmented_flow
		v = t 
		#print "parent again: ", parent   #for check, can be removed
		while v!=s : 
			u = parent[v]
			Flow[u][v] += augmented_flow #flow is positive matrix
			Flow[v][u] -= Flow[u][v]
			#Flow[v][u] -= augmented_flow
			#Capacity[u][v] += augmented_flow #positive addition because negative capacity taken due to fib heap structure and postive augmented flow 
			v= u

		#Make residual graph and send residual graph in the max_aug_flow function
		for i in range(0,n):
			for j in range(0,n):
				if Edge[i][j] == 1:
					Res_graph[i][j] = -(-Capacity[i][j]-Flow[i][j]) #capacity is negative matrix, hence - sign required and because we need res_graph to have negative values 
					#othewise, Cf = c(u,v) - f(u,v)
					Res_graph[j][i] = -(-Flow[i][j]) #Cf(v,u) = -f(u,v) , here as positive, because negative capacities for fib heap to work

		print "Capacity matrix is "
		print Capacity

		print "Flow matrix is: "
		print Flow 

		print "Res_graph is "
		print Res_graph
		print ""
	



	return maxFlow

