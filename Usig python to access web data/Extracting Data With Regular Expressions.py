''' Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file
and compute the sum of the numbers. '''





import re

fh=open('actualdata.txt')
l=[]
s=0
for i in fh:
	
      l+=re.findall('[0-9]+', i)
for i in l:
	s+=int(i)	

print(s)

