"""
5)Write a Python program to read last n lines of a file. 
"""

f = open("sample.txt","r")

liens=f.read().splitlines()

print(liens)
print(liens[3])