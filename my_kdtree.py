import sys
import re
import kdtree

data = []
data_int = []
query = []
query_int = []
tree_col = []
tree_col_int = []
thisdict ={}

##Adding all three elements in dictionary##
def datadict(x):
	arg1 = (x[0]+","+x[1])
	arg2=x[2]
	thisdict[arg1]=arg2

##Get the value for key value from thisdict
def neigh(value1,value2):
	num1 = re.sub(r'[\]\[]*', "",str(value1)).split(",")
	num2 = re.sub(r'[\]\[]*', "",str(value2)).split(",")
	num1[0]=format(float(num1[0]), '.2f')   ##Setting precision to match dictionary key 
	num1[1]=format(float(num1[1]), '.2f')
	num2[0]=format(float(num2[0]), '.2f')
	num2[1]=format(float(num2[1]), '.2f')
	q1 = (num1[0]+","+num1[1]) 		##Creating key string
	q2 = (num2[0]+","+num2[1])
	neigh_val1=thisdict[q1]			##Fetching value for key created
	neigh_val2=thisdict[q2]
	decision(neigh_val1,neigh_val2)

def decision(x,y)
	if "x"=="y":
		return neigh_val1

####Reading the data from input file#####
for line in sys.stdin:
	if line.strip()[0] == '#':
		continue
	elif "#" in line:
		data.append(line.rstrip().split('#')[0])
	else:
		col_line=line.rstrip().split(" ")
		if len(col_line) == 3:
			datadict(col_line)
			tree_col.append(col_line[:2])
		elif len(col_line) == 2:
			query.append(col_line)

##Converting all string lists to integer values##
for x in query:
	query_int.append(list(map(float,x)))

for x in tree_col:
	tree_col_int.append(list(map(float,x)))

	
# Creating tree from coordinates
emptyTree = kdtree.create(dimensions=2)
tree = kdtree.create(tree_col_int)

#Fetching query and finding the nearest neighbour
for out in query_int:
	x = out[0]
	y = out[1]
	neighbors=(tree.search_nn((x,y)))
	neigh(neighbors[0],neighbors[1])
