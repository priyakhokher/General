#!usr/bin/env/python27

import sys

def find_occurence(l,a,b):
	start = 0
	end = len(l)-1
	result = -1

	while(start<=end):
		mid = (start+end)/2
		if l[mid] == a:
			result = mid
			if b==-1:
				end = mid+b
			else:
				start = mid+b


		elif l[mid]<=a:
			start = mid + 1

		elif l[mid]>=a:
			end = mid - 1

	return result









if __name__ == '__main__':
	l = map(lambda x: int(x), sys.argv[1:])
	l = sorted(l)
	a = int(raw_input("Enter the element: \n"))
	
	first_occurence = find_occurence(l,a,-1)
	last_occurence = find_occurence(l,a,1)
	print (last_occurence - first_occurence + 1)
