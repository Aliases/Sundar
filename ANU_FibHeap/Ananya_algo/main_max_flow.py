from random import randint
from mod_edmonds_karp import edmonds_karp


print "Enter number of vertices: "
N=raw_input()
N=int(N)
print "Enter the maximum capacity possible: "
limit = int(raw_input())


Capacity  = [[0 for x in range(N)] for x in range(N)]
Capacity2 = [[0 for x in range(N)] for x in range(N)]
Flow  = [[0 for x in range(N)] for x in range(N)]

#Defining Capacity and capacity2 matrix 
#Capacity matrix is same as capacity2 except negative sign
#Capacity matrix is negative valued matrix 
for i in range(0,N):
	for j in range(0,N):
		Capacity[i][j]=0
		Capacity2[i][j]=0
		if j>i :
			Capacity[i][j]= -(randint(0,limit)+1)
			Capacity2[i][j]=-Capacity[i][j]

'''

print "Enter number of vertices: "
N=5

Capacity  = [[0 for x in range(N)] for x in range(N)]
Capacity2 = [[0 for x in range(N)] for x in range(N)]
Flow  = [[0 for x in range(N)] for x in range(N)]

Capacity2 = [[0,3,3,3,3],[0,0,2,3,5],[0,0,0,4,5],[0,0,0,0,6],[0,0,0,0,0]]

for i in range(0,N):
	for j in range(0,N):
		if j>i :
			Capacity[i][j]=-Capacity2[i][j]

'''


s=0
t=N-1

#print "Capacity matrix is: "
#print Capacity2

maxFlow= edmonds_karp(N,s,t,Capacity,Flow)

print "Flow matrix is: "
print Flow 

print "Max. flow value is: "
print maxFlow