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

def max_aug_flow(n,s,t,Capacity,Flow,p):
	frozen=[-1 for x in range(n)]
	unfrozen=[-1 for x in range(n)]
	unfrozen_node_list=[-1 for x in range(n)]
	frozen_node_list=[]

	#freeze source
	frozen[0]=1;

	#initialize fib heap
	Uf_heap = make_heap()

	#first for source s.
	source_node= newNode(0,0,0)
	frozen_node_list.append(source_node)
	#unfrozen_node_list.append(source_node)
	new_s = s #initialize with source node 

	while new_s!=t :
		for j in range(0,n):
			if Capacity[new_s][j]<0 :
				if p[j]!= -1 :

					if Capacity[new_s][j] < Capacity[p[j]][j] :
						p[j]=new_s #updates parent list 
						unfrozen_node_list[j].key = Capacity[new_s][j]
						

				else:
					node = newNode(Capacity[new_s][j],j,new_s)
					unfrozen_node_list[j]=node
					unfrozen[j]= 1
					#print "added new node j"
					insert(Uf_heap, node)
					p[j]=new_s 

		ret_node= extract(Uf_heap)
		if ret_node == None:
			return 0
		frozen[ret_node.vertex]= 1 
		frozen_node_list.append(ret_node)
		unfrozen[ret_node.vertex]= -1
		new_s= ret_node.vertex

		#say no node left in unfrozen node list, hence see if everything is -1


	p[0]=-1
	flow=[]


	#Need to trace path from sink to source using parent p list
	trace_parent_index=n-1
	while p[trace_parent_index] != -1 :
		curr_flow=Capacity[p[trace_parent_index]][trace_parent_index]
		if curr_flow <0 :
			flow.append(curr_flow)
		
		trace_parent_index = p[trace_parent_index]

	#Accordingly update a new flow list 
	#Find the min. of flow list (or max. because negative capacities)
	#Min. is the maximum flow 
	final_flow = max(flow)
	return -final_flow



		