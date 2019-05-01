import numpy as np
import math
no_of_nodes=input("Enter no of nodes:")
print(no_of_nodes)
nodes=[]
for i in range(0,no_of_nodes):
	nodes.append(raw_input("enter node no "+str(i)+":"))
AM=[]
for i in range(0,no_of_nodes):
	AM.append([])
	for j in range(0,no_of_nodes):
		AM[i].append(input(nodes[i]+"->"+nodes[j]+":"))
U=[]
k=input("no. of iterations:")
iterations=1
while(iterations<=k):
	for i in range(0,no_of_nodes):
		U.append(1)
	AM=np.array(AM,dtype='float')
	AT=np.transpose(AM)
	U=np.array([U],dtype='float')
	UT=U.T
	V=AT.dot(UT)
	U=AM.dot(V)
	sumU=0
	sumV=0
	if iterations>1:
		for i in range(len(U)):
			for j in range(0,1):
				sumU=sumU+(U[i][j]*U[i][j])
				sumV=sumV+(V[i][j]*V[i][j])
		U=U/math.sqrt(sumU)
		V=V/math.sqrt(sumV)
	iterations=iterations+1
for i in range(len(U)):
	for j in range(0,1):
		print("hub "+nodes[i]+": "+str(U[i][j]))

for i in range(len(U)):
	for j in range(0,1):
		print("Authority "+nodes[i]+": "+str(V[i][j]))
