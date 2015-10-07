from edmonds_karp_1 import edmonds_karp 
from random import randint 

print "Enter number of vertices: "
N=raw_input()
N=int(N)
print "Enter the maximum capacity possible: "
limit = int(raw_input())

#N=10
#limit = 10

Capacity  = [[0 for x in range(N)] for x in range(N)]
Flow  = [[0 for x in range(N)] for x in range(N)]

#Defining Capacity matrix
#Capacity2 not needed here. Capacity matrix is normal positive matrix 
for i in range(0,N):
	for j in range(0,N):
		#Capacity[i][j]=0
		
		if j>i :
			Capacity[i][j]= randint(0,limit)+1
			



'''N=6

Capacity = [[0,1,1,1,1,0],[0,0,0,0,0,1],[0,0,0,0,0,1],[0,0,0,0,0,1],[0,0,0,0,0,1], [0,0,0,0,0,0]]
#Capacity2 = [[0,-1,-1,-1,-1,0],[0,0,0,0,0,-1],[0,0,0,0,0,-1],[0,0,0,0,0,-1],[0,0,0,0,0,-1], [0,0,0,0,0,0]]
#Capacity = [[0, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0]]
Flow  = [[0 for x in range(N)] for x in range(N)]
'''

s=0
t=N-1
maxFlow = edmonds_karp(N,s,t,Capacity,Flow)

print "Capacity matrix is: "
print Capacity


print "Final flow matrix is: "
print Flow

print "maxFlow value is: ", maxFlow