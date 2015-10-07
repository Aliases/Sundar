from fibonacci_heap import FibonacciHeap 
from fibonacci_heap import FibonacciHeapNode
from fibonacci_heap import make_heap, make_node, minimum, is_empty, insert,extract, decrease_key

from random import randint

class newNode(FibonacciHeapNode):
	"""define new node using fibheapnode already defined
add parameters vertex no. and parent_vertex to it
initiate new node with -1 parent if not already known
key is the label here. """
	def __init__(self, key, vertex, parent_vertex):
		FibonacciHeapNode.__init__(self,key)
		self.vertex= vertex
		self.parent_vertex = parent_vertex

def max_aug_flow(n,s,t,Capacity,Flow,p, No_Edge_Sat_Max_Flow):
	frozen=[-1 for x in range(n)]
	unfrozen=[-1 for x in range(n)]
	unfrozen_node_list=[-1 for x in range(n)]
	frozen_node_list=[]

	#p = [-1 for x in range(n)]
	print "Current source is: ", s
	print "Current sink is: ", t
	print "input parent list is: ", p
	print "input capacity graph is: ", Capacity
	#freeze source
	frozen[0]=1;

	#initialize fib heap
	Uf_heap = make_heap()

	#first for source s.
	source_node= newNode(0,s,0)
	frozen_node_list.append(source_node)
	#unfrozen_node_list.append(source_node)
	new_s = s #initialize with source node 

	temp_var = 0
	while new_s!=t :
		temp_var +=1
		for j in range(0,n):
			print "edge capacity for", new_s," : ",j, "is" ,Capacity[new_s][j]
			if Capacity[new_s][j]<0 :
				#test call
				print "this j is ", j, "and parent is: ", p[j]
				if p[j]!= -1 :
					if Capacity[new_s][j] < Capacity[p[j]][j] :
						p[j]=new_s #updates parent list 
						print "Current j is " , j
						unfrozen_node_list[j].key = Capacity[new_s][j]
						

				else:
					node = newNode(Capacity[new_s][j],j,new_s)
					print "new node ", j, "added" 
					unfrozen_node_list[j]=node
					unfrozen[j]= 1
					#print "added new node j"
					insert(Uf_heap, node)
					p[j]=new_s 

		print "parent list is : ", p
		ret_node= extract(Uf_heap)
		
		if ret_node == None:
			print "temp_var is: ", temp_var
			return 0

		print "returned node is ", ret_node.vertex 

		frozen[ret_node.vertex]= 1 
		frozen_node_list.append(ret_node)
		unfrozen[ret_node.vertex]= -1
		new_s= ret_node.vertex
		print "new_s is: ", new_s
		#say no node left in unfrozen node list, hence see if everything is -1


	p[s]=-1
	flow=[]


	#Need to trace path from sink to source using parent p list
	trace_parent_index=t

	print "n: ", n , " and current sink: ", t 

	max_curr_flow = -1000
	while p[trace_parent_index] != -1 :
		curr_flow=Capacity[p[trace_parent_index]][trace_parent_index]
		print "curr_flow: ", curr_flow
		if curr_flow <0 :
			flow.append(curr_flow)

		'''#store u and v for saturated edge(u,v)
		if curr_flow > max_curr_flow:
			sat_u = p[trace_parent_index] #store u and v for saturated edge(u,v)
			sat_v = trace_parent_index    '''
		
		trace_parent_index = p[trace_parent_index]

	#No_Edge_Sat_Max_Flow[sat_u][sat_v] += 1

	#Separate loop and not using only the bottleneck capacity because multiple edges with same capacity might get saturated 
	v = t 
	while p[v] != -1 :
		if max(flow) == Capacity[p[v]][v]:
			No_Edge_Sat_Max_Flow[p[v]][v] += 1 
		v = p[v]

	print "flow ", flow 
	print "parent here too: ", p
	#Accordingly update a new flow list 
	#Find the min. of flow list (or max. because negative capacities)
	#Min. is the maximum flow 
	final_flow = max(flow)
	return -final_flow
	#return -final_flow, sat_u, sat_v




		