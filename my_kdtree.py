import sys
import re
import kdtree

##Initiating lists and dictionaries
query = []
query_int = []
tree_col = []
tree_col_int = []
thisdict = {}
t_dict={}

#Updating the Dictionary with new values
def datadict(x):
        arg1 = (x[0]+","+x[1])
        arg2=x[2]
        t_dict.update({arg1:arg2})
        return(t_dict)


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
	final_val1 = decision(neigh_val1,neigh_val2)
	return (final_val1)
	
#Predicting the Class
def decision(x,y):
	if "x"=="y":
		return (x)  
	elif "x" != "y":
		return (x) ##Taking closest neighbor as high priority

# Creating tree from coordinates
def create_tree (list):
	emptyTree = kdtree.create(dimensions=2)
	f_tree = kdtree.create(list)
	f_tree = f_tree.rebalance()
	return (f_tree)

##Converting all string lists to integer values##
def convertion_query(q):
	q_int=[]
	for x in q:
		q_int.append(list(map(float,x)))
	return (q_int)

#Converting the list to the decimal format 
def convertion_tree_list (t):
	t_col_int=[]
	for x in t:
		t_col_int.append(list(map(float,x)))
	return (t_col_int)

####Reading the data from input file#####
if __name__ == "__main__":
	for line in sys.stdin:
		col_line=line.rstrip().split(" ")	
		try:
			if len(col_line) == 3 and type(float(col_line[0])) == float and type(float(col_line[1])) == float and type(col_line[2]) == str:
				thisdict=datadict(col_line)
				tree_col.append(col_line[:2])
			elif len(col_line) == 2 and type(float(col_line[0])) == float and type(float(col_line[1])) == float:
				query.append(col_line)                	
			else:
                		continue
		except:
			continue

##Invoking convertions
query_int=convertion_query(query)
tree_col_int=convertion_tree_list(tree_col)

##Creating tree from elements in list 
tree=create_tree(tree_col_int)

	
#Fetching query and finding the nearest neighbour
try:
	for out in query_int:
		x = out[0]
		y = out[1]
		neighbors=(tree.search_nn((x,y)))
		new_value=neigh(neighbors[0],neighbors[1])
		print (x,y,new_value)	
		x = format(float(out[0]), '.2f')
		y = format(float(out[1]), '.2f')
		str1=' '.join((str(x),str(y),new_value))
		str2=str1.split(" ")[:3]
		thisdict=datadict(str2) 						##Updating the dictionary with the new value
		str3=str1.split(" ")[:2]
		tree_col.append(str3)					##Updating the list with which tree is created
		tree_col_int=convertion_tree_list(tree_col)          	##Reconverting list to float values for error minimization
		tree=create_tree(tree_col_int)			##Recreating tree before every new search
except IOError:
	print('An Error occured trying to read the file')
except ValueError:
        print('Non-Numeric data found in the file')
except ImportError:
        print('No module found')
except EOFError:
        print('An Error occured while reading a file')
except:
        print('An Error occured')

