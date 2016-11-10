#!usr/bin/env/python2
import os
import sys
import time

def bubble_sort(seq,now):
	'''
	Implement bubble sorting, O(n**2)
	'''
	n = len(seq)
	for i in range(n-1): # run this n-1 times
		
		for j in range(n-1):
			if seq[j]>seq[j+1]:
				seq[j],seq[j+1] = seq[j+1],seq[j]
				


	print seq


if __name__ == '__main__':
	
	now = time.clock()
	seq = map(int,sys.argv[1:])
	bubble_sort(seq,now)