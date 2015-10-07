from copy import copy, deepcopy #to copy matrices 
from max_augmenting_path import max_aug_flow
from random import randint

#takes as input capacity matrix, no. of vertices, source, sink, 

def edmonds_karp(n,s,t,Capacity,Flow):
	maxFlow=0
	parent = [-1 for x in range(n)]
	x=0
	while 1 :
		print "iteration number: ", x
		x +=1
		augmented_flow = max_aug_flow(n,s,t,Capacity,Flow,parent)
		if augmented_flow == 0:
			break
		maxFlow += augmented_flow
		v = t 
		while v!=s : 
			u = parent[v]
			Flow[u][v] += augmented_flow
			#Flow[v][u] -= augmented_flow
			Capacity[u][v] += augmented_flow # += because negative capacities and positive flow taken
			v= u;



	return maxFlow

