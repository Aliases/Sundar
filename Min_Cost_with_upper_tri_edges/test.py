
from copy import deepcopy

'''Capacity2 = [[0,-1,-1,-1,-1,0],[0,0,0,0,0,-1],[0,0,0,0,0,0,-1],[0,0,0,0,0,0,-1],[0,0,0,0,0,0,-1], [0,0,0,0,0,0]]
Res= deepcopy(Capacity2)
Capacity2[0][0]=999
print Res
print Capacity2
'''

def test_func2(a,b,c):
	print a, b,c
	a = b+c 
	print a

alpha,beta=2,3
gamma=3
test_func2(alpha,beta,gamma)
print alpha 

if 4<=3 :
	print "test "













'''def test_func(list1, list2):
	#list1 = [-1 for x in range(5)]
	for i in range(5):
		list1[i]=0
	list1[0]= 9

list0 =[1,2,3,4,5]
test_func(list0,list0)
print list0
'''

list3 =["dog",2,3,4,5]

'''for i in range(len(list3)):
	if list3[i] == 3:
		list3[i]=6
		i = i-1
	print i, ", ", list3[i]

print list3

min = 3 
a = 2 '''

#for a in list3:
#	print a
#print -min(2,3)

'''def test_func2(a,b):
	return a,b

name1="first"
name2="second"

c= test_func2(name2, name1)
print c, d'''

#list3.insert(0,10)
#print list3

'''N = int(raw_input("Enter number of nodes "))

demand=[0 for x in range(N)]
sum = 0
for i in range(int(round(N/2))):
	demand[i]= 5
	sum += demand[i]
for i in range(int(round(N/2)),N-1):
	demand[i] = -5
	sum += demand[i]

demand.insert(0,10)
demand.pop()
print demand'''

