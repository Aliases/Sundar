from fibonacci_heap import FibonacciHeap 
from fibonacci_heap import FibonacciHeapNode
from fibonacci_heap import make_heap, make_node, minimum, is_empty, insert,extract, decrease_key

from random import randint

print "Enter number of vertices: "
n=raw_input()
n=int(n)
#n=10 #Temporarily fixing n, 3 lines above work well though
Capacity   = [[0 for x in range(n)] for x in range(n)]
Capacity2 = [[0 for x in range(n)] for x in range(n)]

#Defining Capacity and capacity2 matrix 
#Capacity matrix is same as capacity2 except negative sign
for i in range(0,n):
	for j in range(0,n):
		Capacity[i][j]=0
		Capacity2[i][j]=0
		if j>i :
			Capacity[i][j]= -(randint(0,9)+1)
			Capacity2[i][j]=-Capacity[i][j]

#print Capacity

#Parent array
p=[-1 for x in range(n)]
#print len(parent)
frozen=[-1 for x in range(n)]
#print frozen
unfrozen_node_list=[-1 for x in range(n)]
frozen_node_list=[]

#define new node using fibheapnode already defined
#add parameters vertex no. and parent_vertex to it
#initiate new node with -1 parent if not already known
#key is the label here. 
class newNode(FibonacciHeapNode):
	"""docstring for newNode"""
	def __init__(self, key, vertex, parent_vertex):
		FibonacciHeapNode.__init__(self,key)
		self.vertex= vertex
		self.parent_vertex = parent_vertex


#function to go through all nodes in heap
#using print_heap for it
#Error possible in this new function,because of curr, not sure whether it updates the value in heap too , need to check for it!! 
#Java takes objects by reference, assuming same for python, leap of faith as of now, check it today from Python documentation
def update_label(heap, new_ind, ind, Capacity):
	length = len(Capacity)
	start= heap.min #minimum node 
	curr= start
	first_iter= True
	while curr != None and (first_iter or curr != start):
		first_iter= False
		if curr.vertex == ind :
			curr.key= Capacity[new_ind][ind]
			break  #break statements because only one such vertex is gonna be there  
		if curr.child != None:
			if curr.vertex == ind: 
				curr.key= Capacity[new_ind][ind]
				break
		curr= curr.right


#freeze source
frozen[0]=1;

#initialize fib heap
Uf_heap = make_heap()

# Define source s and sink t
s=0
t=n-1

#first for source s.
source_node= newNode(0,0,0) #need to think about parent vertex of s, keep -1 but that might mess up later 
frozen_node_list.append(source_node)
for j in range(0,n):
	if Capacity[0][j]<0:
		#add corres. j nodes to unfrozen heap, i.e. make nodes for them in heap
		node = newNode(Capacity[0][j],j,0)
		unfrozen_node_list[j]=node #Does this thing pass a reference to node into the list or does it pass a copy?
		insert(Uf_heap, node)
		p[j]=0 

ret_node= extract(Uf_heap) #returned node
frozen[ret_node.vertex]= 1 #freeze that node 
frozen_node_list.append(ret_node) #append it to frozen node list 
new_s= ret_node.vertex


while new_s!=t :
	for j in range(0,n):
		if Capacity[new_s][j]<0 :
			if p[j]!= -1 :

				if Capacity[new_s][j] < Capacity[p[j]][j] :
					p[j]=new_s #updates parent list 
					unfrozen_node_list[j].key= Capacity[new_s][j]
					#update_label(Uf_heap, new_s, j, Capacity )

				'''
				minimum = 0	#minimum because negative Capacitys

				#updates parent p list appropriately 
				for node in frozen_node_list:
					#need max of Capacity[node.vertex][j]
					if Capacity[node.vertex][j]<minimum
					minimum = Capacity[node.vertex][j] #this min. needs to be new label of node with vertex j
					p[j]=node.vertex '''


				#need to update unfrozen node list 
				#Unfrozen heap also needs to be updated 
				#need to find node with vertex =j
				#how to go through all nodes in unfrozen heap
				#for node_2 in 
				
				#assuming you can't get this done with unfrozen list
				#Using something like print_heap to traverse through nodes of heap
				#update label
					



			else:
				node = newNode(Capacity[new_s][j],j,new_s)
				unfrozen_node_list[j]=node 
				insert(Uf_heap, node)
				p[j]=new_s 

	ret_node= extract(Uf_heap)
	frozen[ret_node.vertex]= 1 
	frozen_node_list.append(ret_node) 
	new_s= ret_node.vertex


p[0]=-1
flow=[]

#print p 

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
print "Capacity Matrix is: "
print Capacity2
print "Final flow value is "+ str(-final_flow )


		