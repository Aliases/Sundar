from copy import deepcopy
from bfs import std_bfs, mod_bfs
from mod_edmonds_karp import max_min_bottleneck 
#from edmonds_karp_1 import edmonds_karp

def min_cost(no_of_nodes, demand, Edge, Cost, Flow  ):
	n = no_of_nodes
	fulfilled_demand = [0 for x in range(n)] #indicates current fulfilled demands
	curr_demand = deepcopy(demand)  #current demand remaining 
	node_potential = [0 for x in range(n)]
	Part_Flow = [[0 for x in range(n)] for x in range(n)]

	source=[]
	sink=[]
	
	
	for i in range(n):
		if demand[i] > 0:
			source.append(i)
		elif demand[i] <0 :
			sink.append(i)
		else:
			pass 


	#Do as long as any unsaturated source/sink exists 
	#we choose source to start with
	for i in range(len(source)):
		s = source[i] #current source 
		#if any unsaturated source is found, then saturate it
		#if demand[s] - fulfilled_demand[s] > 0 :
		if curr_demand[s] >0:
			saturate_source(s,n,Edge,Cost,node_potential,Part_Flow,curr_demand,sink)

	#Flow = deepcopy(Part_Flow)  : Doesn't work, python kind of assumes this Flow to be a different object than the one originally passed 
	for i in range(n):
		for j in range(n):
			Flow[i][j] = Part_Flow[i][j]
	#return Part_Flow
			
def saturate_source(s,n,Edge,Cost, node_potential,Part_Flow, curr_demand, sink ):
	#print "Desaturate source being called "
	#Construct residual graph for it
	#New residual graph required every time
	Gr_Edge = [[0 for x in range(n)] for x in range(n)]
	Gr_Cost = [[0 for x in range(n)] for x in range(n)]
	Gr_Capacity = [[0 for x in range(n)] for x in range(n)] 
	for u in range(n):
		for v in  range(n):
			if Edge[u][v]>0: #if edge (u,v) in original graph, then
				#if tight edge: 
				if (node_potential[u] - node_potential[v]) == Cost[u][v]:
					print "Tight edge", u , ":", v ,"found"
					Gr_Capacity[u][v]= 1000 #infinity capacity
					Gr_Edge[u][v]=1
					Gr_Cost[u][v]=Cost[u][v]

				#reverse arc:
				if Part_Flow[u][v] >0 :
					Gr_Edge[v][u]=1
					Gr_Capacity[v][u]=Part_Flow[u][v]
					Gr_Cost[v][u]= -Cost[u][v]
	#residual graph completed

	#Find if any unsaturated sink t reachable from s
	parent = [-1 for x in range(n)]
	t = mod_bfs(Gr_Edge,s,parent,sink)

	if t != -1 :
	#say path found with flow f, then, along the path
	#Part_Flow[u][v] += f
	#Need to get f by min. 
		if curr_demand[s] > -curr_demand[t] :
			f = -curr_demand[t]
			#sink.remove(t) #saturated sink removed 
		else:
			f = curr_demand[s]
		
		'''#deploy capacity constraint
		v =t 
		min_cap = 0
		cap_list =[]
		while v != s:
			u = parent[v]
			#Part_Flow[u][t] += f
			cap_list.append(Gr_Capacity[u][v])
			v = u 
		min_cap = min(cap_list)
		path_capacity = min(f, min_cap)

		curr_demand[s] -= path_capacity
		curr_demand[t] += path_capacity #because sink has negative demand while source has positive demand, hence the sign difference
		if curr_demand[t] == 0:
			sink.remove(t)

		#Update flow along the path
		while t!=s : 
			u = parent[t]
			Part_Flow[u][t] += path_capacity
			t = u'''

		#Finding max. flow between source and sink first found (using modified edmondns karp to find max. augmenting path)
		MF_Capacity = [[0 for x in range(n)] for x in range(n)] 
		MF_Flow = [[0 for x in range(n)] for x in range(n)] 
		for u in range(n):
			for v in range(n):
				MF_Capacity[u][v] = -min(f, Gr_Capacity[u][v]) #-ve sign because -ve capacities for fib heap, 
				# min of these 2 because flow cannot be more than supply/demand at source/sink
		maxFlow = max_min_bottleneck(n,s,t,MF_Capacity, MF_Flow,f )

		for u in range(n):
			for v in range(n):
				Part_Flow[u][v] += MF_Flow[u][v]

		print ""		
		print "maxFlow found is: ", maxFlow
		curr_demand[s] -= maxFlow
		curr_demand[t] += maxFlow #because sink has negative demand while source has positive demand, hence the sign difference
		if curr_demand[t] == 0:
			sink.remove(t)
			print "Sink removed: ",t 
			#print ""
		print "Current demand array is: ", curr_demand 
		 



		#check if source is saturated: 
		if curr_demand[s] > 0:
			saturate_source(s,n,Edge,Cost,node_potential,Part_Flow,curr_demand,sink)

	else: #i.e. when no reachable unsat. sink from this unsat. source s, we raise node potentials, definitely define new routine for this
		print "We need to raise node potential for source ", s
		raise_node_potentials(s, n, Edge, Cost, node_potential, Gr_Edge)

		# need to go through this source again and unsaturate it
		saturate_source(s,n,Edge,Cost,node_potential,Part_Flow,curr_demand,sink)

def raise_node_potentials(s, n, Edge, Cost, node_potential, Gr_Edge):
	color =[-1 for x in range(n)]
	parent =[-1 for x in range(n)]
	distance =[0 for x in range(n)]

	std_bfs (Gr_Edge,s,color,parent,distance)

	#Need to get visited nodes. Color changed to gray or black 
	visited=[]
	unvisited=[]
	for i in range(n):
		if color[i] == -1:
			unvisited.append(i)
		else:
			visited.append(i)

	min= 1000
	print color 
	print node_potential



	for a in visited:
		for b in unvisited:
			if Edge[a][b] == 1:
				delta = Cost[a][b] - (node_potential[a]-node_potential[b])
				print delta 
				#print "Are we coming here? Yes, we are raising node potentials here"
				if delta< min:
					min = delta
					to_be_raised =a
				#	print "here"

	print "visited: ", visited
	print "unvisited: ", unvisited
	
	for a in visited:
		node_potential[a] += min 
	#node_potential[to_be_raised] += min
	
	print to_be_raised ," node's potential to be increased"
	

					



