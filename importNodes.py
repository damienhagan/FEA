import  re

class node(object):

	def __init__(self, n_num, n_coord):

		self.num = n_num
		self.x = n_coord[0]
		self.y = n_coord[1]
		self.z = n_coord[2]
		self.connect = []

	def __str__(self):
		return ("Node %i: %.3f, %.3f, %.3f" % (self.num, self.x, self.y, self.z))

	def connectivity(self, connect_list):
		self.connect.extend(connect_list)



class element(object):

	def __init__(self, n_num):

		self.num = n_num
		self.connect = []

	def __str__(self):
		return ("Element %i" % (self.num))


def removeComments(string):
    string = re.sub(re.compile("\*\*.*?\n" ) ,"" ,string) # remove all occurance singleline comments (//COMMENT\n ) from string
    return string


if __name__ == "__main__":

	n1 = node(2, [3, 3, 4])
	print n1
	print n1.connect
	n1.connectivity([2, 5, 7])
	print n1.connect
	n1.connectivity([1, 2, 7])
	print n1.connect

	f = open('Inc_Nodes.inp', 'r')

	data = removeComments(f.read())

	# Get nodes data
	data_n = re.search(r"\*Node(.*?)\n(.*?)\*", data, re.S)
	l_nodes = []
	for l in data_n.group(2).split('\n'):
		n = l.strip().replace(' ', '').split(',')
		try:
			l_nodes.append(node(int(n[0]), [float(n[1]), float(n[2]), float(n[3])]))
		except:
			pass

	# Get element data
	data_n = re.search(r"\*Element(.*?)\n(.*?)\*", data, re.S)
	l_nodes = []
	for l in data_n.group(2).split('\n'):
		n = l.strip().replace(' ', '').split(',')
		try:
			l_nodes.append(node(int(n[0]), [float(n[1]), float(n[2]), float(n[3])]))
		except:
			pass			

	for n in l_nodes:
		print n





