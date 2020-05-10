''' 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of 
the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time
using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.'''



name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts={}

for i in handle:
    
    if(i.startswith("From ")):
        l=i.split()
        t=l[5].split(':')
        counts[t[0]]=counts.get(t[0], 0)+1
    

l=(sorted(	(k,v)  for (k,v) in counts.items() ))  # sorting keys and making list of tuples 
for i,j in l:
    print(i, j)
        
    
