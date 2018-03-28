#*** Apriori.py ***
#*** Coded by Marco Fringuelli ***
from random import randrange
import itertools
import numpy as np # Arrays/Matrices manipulation

def create(num,ran):
	# Creates a set of random transactions
	i = 0
	trans = {}
	for i in range(num):
		j = 1
		elems = []
		TID = i
		# This is to randomly set the cardinality of each transaction
		iters = randrange(1,16)
		for j in range(iters):
			elems.append('t'+str(randrange(1,ran+1)))
			trans[TID] = sorted(list(set(elems)), key=TSORT)
			j += 1
		i += 1
	return trans

def print_dict(table):
	# Prints the ordered data dictionary
	for k in sorted(table):
		print k,'|',table[k] 

def count(table):
	# Returns a dictionary where key = product and value = frequency
	items = []
	counts = {}
	for k in sorted(table):
	    for p in table[k]:
		    items.append(p)
	for elem in list(set(items)):
		counts[elem] = items.count(elem)
	return counts
    
def found(list1,list2):
	# Determines whether an element in list1 can be found also in list2
	for elem in list1:
		if elem not in list2:
			return False
	return True

def setp(list1):
	# This function is to replace set() when using list assignment
	list2 = []
	for elem in list1:
		if elem not in list2:
			list2.append(elem)
	return list2

def TSORT(elem):
	return int(elem[1:])


def AP(items,s):
	itemset = sorted(setp(list(np.hstack(items))), key=TSORT)
	# This is the very Apriori algorithm, here in an iterative version
	analyzed = []
	frequents = {}
	# 'it' stands for 'iteration number'
	it, counter = 0,0
	done = False
	new = itemset
	while not done and it <= len(itemset):
		# Statement to be denied if there is still the possibility to refine the results
		done = True
		# its stands for 'itemsets'
		# *** JOIN step ***
		combs = [its for its in itertools.product(new,itemset)]
		# print 'LAST ITERATION L_k-1 =', new
		# Each iterations refines previous one result, new is a register
		new = []
		for its in combs:
			# hstack() creates an object-type array with all the elements in the input matrix
			# setp() is to clean off double values in each list
			its = sorted(setp(list(np.hstack(its))), key=TSORT)
			if len(its) == it+1 and its not in analyzed:
				analyzed.append(its)
				for elem in items:
					if found(its,elem) is True:
						counter +=1
				# *** PRUNE step ***
				if counter >= s:
					# The key value is set to place space and bars correctly
					frequents[' '.join(its)+' '* (30-len(' '.join(its)))] = counter
					# print 'FREQUENT ITEMSET:', its, 'COUNT:', counter
					done = False # Denial
					new.append(its) # Refining
				counter = 0
		it += 1
	return frequents


#-------------------MAIN-----------------------#
s = input('Enter the minimum support count:\n')
ran = 16
table = create(25,ran)
print '\n'
print 'TRANSACTION ID / ITEMS'
print_dict(table)
counted = count(table)
print '\n'
print 'ITEM / FREQUENCY'
print_dict(counted)
print '\n'

items = []
counter = 0
print 'MINIMUM SUPPORT COUNT =',s
print '\n'
for k in sorted(table):
	items.append(table[k])

frequents = AP(items,s) 
print "\nFREQUENT ITEMSET / SUPPORT\n"
print_dict(frequents)





# Calculate confidence of any associative rule

# def test(itemset,s):
# 	items_test = [['t1','t2','t3','t6'], ['t1','t2','t3','t5','t6'], ['t1','t2','t3','t6','t7'], 
# 	['t1','t2','t3','t4','t6'],['t1','t2','t3','t6','t7'], ['t1','t2','t3','t6']]
# 	AP(itemset,items_test,s)
# 	print 'ITEMSET 1,2,3,6 Expected Count Value (for s=4): 6'

# test(itemset,4)









	




	



