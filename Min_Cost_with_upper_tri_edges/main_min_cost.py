
#Input: 

#Demand/supply at each node
#supply is positve, demand is negative: name single list demand 

#We consider infinite capacities. Edges needed. So edge matrix 


from min_cost_2 import min_cost 
#from min_cost_2_bottleneck import min_cost
from random import randint 


N = int(raw_input("Enter number of nodes "))
demand_limit = int(raw_input("Maximum demand/supply "))
cost_limit = int(raw_input("Maximum cost "))

demand=[0 for x in range(N)]
sum = 0
for i in range(int(round(N/2))):
	demand[i]= randint(0,demand_limit)
	sum += demand[i]
for i in range(int(round(N/2)),N-1):
	demand[i] = -randint(0,demand_limit)
	sum += demand[i]

if sum < 0:
	demand.insert(0,-sum)  #if remaining is positive, hence source, needs to be added in first half 
	demand.pop() #remove last element 
else:
	demand[N-1] = -sum  #ensures net demand 0

print "length of array is: ", len(demand)


#Generate edge matrix and corresponding cost matrix 
Edge = [[0 for x in range(N)] for x in range(N)]
Cost = [[0 for x in range(N)] for x in range(N)]
Flow = [[0 for x in range(N)] for x in range(N)]

for i in range(N):
	for j in range(i+1,N):
		#completely connected graph as of now, in one direction
		#Different issue how to ensure that all sources are on the edge sending side 
		Edge[i][j] = 1 
		Cost[i][j] = randint(0,cost_limit) + 1 


print "demand is: ", demand
print "Edges are: ", Edge
print "Costs are: ", Cost


#Following example is from Figure 1 on link:
#https://www.topcoder.com/community/data-science/data-science-tutorials/minimum-cost-flow-part-one-key-concepts/
"""N=6
demand =[5,2,0,-1,-4,-2]
Edge = [[0,1,1,0,0,0], [0,0,1,0,0,0], [0,0,0,1,1,1], [0,0,0,0,1,0], [0,0,0,0,0,0] , [0,0,0,0,0,0]]
Cost = [[0,1,4,0,0,0], [0,0,2,0,0,0], [0,0,0,2,5,8], [0,0,0,0,1,0], [0,0,0,0,0,0] , [0,0,0,0,0,0]]
Flow = [[0 for x in range(N)] for x in range(N)]"""

"""N=5
demand =[67, 220, 553, -552, -288]
Edge = [[0, 1, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
Cost = [[0, 7, 43, 30, 46], [0, 0, 53, 23, 33], [0, 0, 0, 23, 45], [0, 0, 0, 0, 9], [0, 0, 0, 0, 0]]
Flow = [[0 for x in range(N)] for x in range(N)]"""

min_cost(N, demand, Edge, Cost, Flow)

print "Final flow looks like:  ", Flow