import itertools

n=int(input("enter no. of items:"))
items=[]
for i in range(0,n):
	items.append(input("enter item no." +str(i+1)+":"))

n=int(input("enter no. of transactions:"))

transaction=[]
for i in range(0,n):
	transaction.append([])
	print("enter transaction no "+str(i+1)+":") 
	while True:
		item=input()
		if not item:
			break
		transaction[i].append(item)
# print(transaction)

minsupport=float(input("enter minimum support in percentage:"))
minconfidence=int(input("enter minimum confidence in percentage:"))
minsupport=(minsupport/100)*n
t=[]
for i in range(0,6):
	combination=list(itertools.combinations(list(items),i+1))
	t.append([])
	for j in combination:
		j=set(j)
		count=0

		for k in transaction:
			if j<=set(k):
				count+=1
		
		if count<minsupport and i==0:
			items.remove(list(j)[0])
		if count>=minsupport:
			t[i].append([list(j),count])

	print(t)
	if t[i]==[]:
		index=i-1
		break

for i in t[index]:
	rule=i[0]
	rule_count=0
	for trans in transaction:
		if set(rule)<=set(trans):
			rule_count+=1
	print(rule_count)

	for j in range(1,len(rule)):
		rule_set=list(itertools.combinations(rule,j))
		print(rule_set)
		for k in rule_set:
			print("rule"+str(set(k))+"->"+str(set(rule)-set(k)),end=" ")
			count=0
			for trans in transaction:
				if set(k)<=set(trans):
					count+=1
			confidence=float(float(rule_count)/float(count)*100.0)
			print("confidence ="+str(confidence),end=" ")

			if confidence>=minconfidence:
				print("ACCEPTED")
			else:
				print("NOT ACCEPTED")



