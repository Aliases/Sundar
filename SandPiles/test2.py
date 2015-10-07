from numpy import pi
from math import sin, cos 

n = int(raw_input("Give n "))
Double_Sum_Values =[[0 for x in range(n)] for x in range(n)]
Exact_Difference = [[0 for x in range(n)] for x in range(n)]
Approx_Difference = [[0 for x in range(n)] for x in range(n)]
Approx_Difference2 = [[0 for x in range(n)] for x in range(n)]
Diff1 = [[0 for x in range(n)] for x in range(n)]
Diff2 = [[0 for x in range(n)] for x in range(n)]

double_sum = 0
alpha= pi/(2*n)

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

exact_diff_sum = 0
approx_diff_sum = 0
for i in range(n):
	for j in range(i+1,n):
		if (i+j)%2 == 1 :
			if (i+1) < n :
				Exact_Difference[i][j]= Double_Sum_Values[i][j] + Double_Sum_Values[i+1][j]
				# + because the second term is negative in Double_Sum_Values matrix 
				Approx_Difference[i][j] =  (alpha**6)*i*j*j*(j*j + i*i - 2*j*i)
				Approx_Difference2[i][j] = (alpha**6)*i*((j+i+1)**2)* ((j-i-1)**2)
				Diff1[i][j] = Exact_Difference[i][j] - Approx_Difference[i][j]
				Diff2[i][j] = Exact_Difference[i][j] - Approx_Difference2[i][j]
				if Exact_Difference[i][j] > 0:
					exact_diff_sum += Exact_Difference[i][j]
					approx_diff_sum += Approx_Difference[i][j]
first_row_sum = 0 
for j in range(n):
	if (0+j)%2 ==0: #i = 0 for first row 
		first_row_sum += Double_Sum_Values[0][j]

print 'difference matrix 1 with more approximation: '
for i in range(n):
	for j in range(n):
		#print Double_Sum_Values[i][j],
		print '%0.4f' % Diff1[i][j] ,
	print

print 'difference matrix 2 with a little less approximation: '
for i in range(n):
	for j in range(n):
		#print Double_Sum_Values[i][j],
		print '%0.4f' % Diff2[i][j] ,
	print 

print 'Exact_Difference: '
for i in range(n):
	for j in range(n):
		#print Double_Sum_Values[i][j],
		print '%0.4f' % Exact_Difference[i][j] ,
	print 

print 'Approx_Difference: '
for i in range(n):
	for j in range(n):
		#print Double_Sum_Values[i][j],
		print '%0.4f' % Approx_Difference[i][j] ,
	print 

'''
for i in range(n):
	for j in range(n):
		#print Double_Sum_Values[i][j],
		print '%0.4f' %Double_Sum_Values[i][j] ,
	print
'''

print 'Exact difference sum is: ' , exact_diff_sum
print 'Lower bound on d sum is: ', approx_diff_sum
print 'first row negative numbers sum is: ', first_row_sum
print 'Hence effective exact diff. is ', exact_diff_sum + first_row_sum
