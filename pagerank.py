nodes=[]
no_of_nodes=input("enter no of nodes :")
for i in range(0,no_of_nodes):
	nodes.append(raw_input("enter names of the nodes:"))
input_graph=[]
for i in range(0,no_of_nodes):
	input_graph.append([])
	for j in range(0,no_of_nodes):
		input_graph[i].append(input("is there a link from "+nodes[i] +"to "+nodes[j]+":"))
# input_graph=[[0,1,1,0], #A
# 			 [0,0,0,1], #B
# 			 [1,1,0,1], #C
# 			 [0,0,1,0]] #D

pagerank=[]

for i in range(len(input_graph)):
	pagerank.append(1/float(len(input_graph)))
pre_pagerank=[]
for i in range(0,2):
	pre_pagerank=pagerank[:]
	for  j in range(len(input_graph)):
		temp_rank=0.0
		for k in range(len(input_graph)):
			if input_graph[k][j]==1:
				count=0
				for l in range(len(input_graph)):
					if input_graph[k][l]==1:
						count=count+1
				temp_rank=temp_rank+pre_pagerank[j]/float(count)
		pagerank[j]=temp_rank
for i in range(len(input_graph)):
	print("pagerank of page "+nodes[i]+" : "+str(pagerank[i]))