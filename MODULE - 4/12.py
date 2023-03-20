"""
12)Write a Python program to copy the contents of a file to another file. 
"""

f1= open("sample.txt",'r')
f2= open("sample_01.txt",'w')

for line in f1:
    f2.write(line)