from numpy import pi
from math import sin, cos 

#print '%0.2f' %pi 

n = int(raw_input("Give n "))
Double_Sum_Values =[[0 for x in range(n)] for x in range(n)]
double_sum = 0

for i in range(n):
	for j in range(n):
		if i==0 and j==0: 
			Double_Sum_Values[i][j]=0
		else:
			if i != j :
				num = (sin((j-i)*pi/(2*n))*sin((j+i)*pi/(2*n))*cos(i*pi/(2*n))*cos(j*pi/(2*n)))**2
				den = (sin(j*pi/(2*n)))**2 + (sin(i*pi/(2*n)))**2
				Double_Sum_Values[i][j] = ((-1)**(i+j+1))*num/den 
				double_sum += Double_Sum_Values[i][j]

colsum=[0 for x in range(n)]
rowsum=[0 for x in range(n)]
superdiagonal = 0 
firstrow = 0 

for i in range(n):
	for j in range(n):
		#print Double_Sum_Values[i][j],
		print '%0.4f' %Double_Sum_Values[i][j] ,
		if j>i :
			rowsum[i] += Double_Sum_Values[i][j]
		if j == i+1 : 
			superdiagonal += Double_Sum_Values[i][j]
	print 

for j in range(n):
	if Double_Sum_Values[0][j] < 0 :
		firstrow += Double_Sum_Values[0][j]

'''for j in range(n):
	for i in range(n):
		if i > j: 
			colsum[i] += Double_Sum_Values[i][j]
print "Columnsum is: ", colsum'''

print "Double sum is ", double_sum

print "Rowsum is: ", rowsum
print "superdiagonal sum is: ", superdiagonal
print "First row sum is: ", firstrow



#a = pi**2 