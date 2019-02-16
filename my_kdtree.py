import sys
import kdtree

data = []
data_int = []
query = []
query_int = []
tree_col = []
tree_col_int = []
for line in sys.stdin:
	if line.strip()[0] == '#':
		continue
	elif "#" in line:
		data.append(line.rstrip().split('#')[0])
	else:
		col_line=line.rstrip().split(" ")
		if len(col_line) == 3:
			data.append(col_line)
			tree_col.append(col_line[:2])
		elif len(col_line) == 2:
			query.append(col_line)	

##Converting all string lists to integer values##
for x in query:
	query_int.append(list(map(float,x)))

for x in tree_col:
	tree_col_int.append(list(map(float,x)))

###Class##
class Item(object):
    def __init__(self, x, y, data):
        self.coords = (x, y)
        self.data = data

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, i):
        return self.coords[i]

    def __repr__(self):
        return 'Item({}, {}, {})'.format(self.coords[0], self.coords[1], self.data)
	
# Creating tree from coordinates
emptyTree = kdtree.create(dimensions=2)
tree = kdtree.create(tree_col_int)

#Fetching query and finding the nearest neighbour
for out in query_int:
	x = out[0]
	y = out[1]
	output=tree.search_nn((x,y))
	print (output)
