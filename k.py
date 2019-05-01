import math
data=[['a',1,1],['b',2,1],['c',2,3],['d',4,2]]

def initmean(data,k):
	centroid=[]
	for i in range(0,k):
		centroid.append([i,data[i]])
	return centroid	
def distance(data,centroid):
	eu=[]
	for i in range(len(centroid)):
		sum=0.0
		for j in range(1,len(centroid[i][1])):
			sum=sum+ (data[j]-centroid[i][1][j])**2
		eu.append([i,math.sqrt(sum)])
	return eu

def mineu(eu):
	pos=eu[0][0]
	value=eu[0][1]
	for  i in range(len(eu)):
		if value>eu[i][1]:
			pos=eu[i][0]
			value=eu[i][1]
	return [pos,value]
def upcen(centroid,data):
	cen=[]
	cen.append(data[0])
	for i in range(1,len(centroid[1])):
		cen.append((float(data[i])+float(centroid[1][i]))/2)
	return [centroid[0],cen]
def kmeans(data,k):
	centroid=initmean(data,k)
	old_centroid=[]

	while old_centroid!=centroid:
		old_centroid=centroid[:]
		cluster=[[] for i in range(0,k)]
		for i in range(len(data)):
			mineu1=mineu(distance(data[i],centroid))
			cluster[mineu1[0]].append(data[i])
			centroid[mineu1[0]]=upcen(centroid[mineu1[0]],data[i])

	print(cluster)

print(upcen([0, ['a', 1, 1]],data[3]))
print(mineu(distance(data[3],[[0, ['a', 1, 1]], [1, ['b', 2, 1]]])))
kmeans(data,2)