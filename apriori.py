import collections
import itertools

# Ordered dict to store the {item : quantity}
items = collections.OrderedDict()

# stores the list of different items
item_list = []

n_items = int(input("Enter no. of items:"))

for i in range(0, n_items):
    item = input("Input item %d:" % (i + 1))
    item_list.append(item)

    # initiialize the quantity  to 0 for each item
    items[item] = 0

n = int(input("Enter no. of transactions:"))
print("**PRESS ENTER TO MOVE TO THE NEXT TRANSACTION**")

# each transaction is a list
transactions = [[] for i in range(0, n)]

for i in range(0, n):
    print("Enter t%d" % (i + 1))
    while True:
        item = input()
        # break when no input and user presses enter
        if not item:
            break
        transactions[i].append(item)

        # increment quantity value in dict
        items[item] += 1

print(item_list)
print(items)
print(transactions)

min_support = float(input("Enter min support in %:"))
min_confidence = int(input("Enter min confidence in %:"))

min_support = (min_support / 100) * n
print(min_support)

combination = list(itertools.combinations(list(item_list), 1))

l = [[] for i in range(0, n_items)]

# traversing for transaction

for i in range(0, n):
    print("****************")
    for j in combination:
        j = frozenset(j)
        # initialize the count of subsequence to 0
        count = 0
        print(j, end=" ")

        for t in transactions:
            if j <= frozenset(t):
                count += 1

        print(count)

        if (count < min_support and i == 0):
            ''' if candidate support < min support count 
            remove it from the item 
            list so that no sub sequence 
            of the item is generated '''
            item_list.remove(list(j)[0])
            print(item_list)

        if (count > min_support):
            d = dict({j:count})
            l[i].append(d)

        print(l)

    combination = list(itertools.combinations(list(item_list), (i+2)))
    # if Li is empty i.e. no subsequences qualify for Li the break
    if not l[i]:
        index =  i - 1
        break

for i in l[index]:
    print("*************")
    rule_count = 0
    # every subsequence in l[index] will form set of rules
    rule = list(list(i.keys())[0])

    for t in transactions:
        if ( set(rule) <= set(t)):
            rule_count += 1
    print(rule_count)

    for j in range(1, len(rule)):
        combination = list(itertools.combinations(rule,j))
        for k in combination:
            count = 0
            print("For rule {0} -> {1}:". format(set(k), set(rule) - set(k)), end="")
            for t in transactions:
                if( set(k) <= set(t) ):
                    count += 1
            confidence = (rule_count/count) * 100
            print(confidence, end="")

            if( confidence < min_confidence ):
                print("RULE NOT SELECTED")
            else:
                print("RULE SELECTED")