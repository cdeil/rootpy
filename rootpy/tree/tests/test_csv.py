import os
from StringIO import StringIO
#from rootpy.tree import Tree
from rootpy.testdata import get_file

def test_read():
	"""Test reading a TTree for a ROOT file"""
	f = get_file('ttree.root')
	tree = f.get('ParTree_Postselect')
	# assert something!

def test_csv_write():
	f = get_file('ttree.root')
	tree = f.get('ParTree_Postselect')
	print len(tree)
	print tree.branchnames
	tree.csv()
	# read head and tail and assert OK!

def test_looping():
	f = get_file('ttree.root')
	tree = f.get('ParTree_Postselect', ignore_unsupported=True)
	n_events = 0
	for event in tree:
		n_events += 1
	assert n_events == 5

if __name__ == "__main__":
    
    test_csv_write()
