'''
A user will input two strings, and we find if one of the strings is a sub sequence of the other. Program prints “yes” if either the first string is a sub sequence of the second string or the second string is a sub sequence of the first string.
Assume that, the length of the first string is smaller than or equal to the length of the second string.

An expected output of the program:

Input the first string
tree
Input the second string
Computer science is awesome
YES
'''
s1=input('Enter main string: ')
s2=input('Enter sub sequence string: ')
a=0
b=0
i=0
n1=len(s1)
n2=len(s2)
while i<n1:
	if s1[i]!=s2[a]:
		i=i+1
	
	else:
		i=i+1
		a=a+1
		b=b+1
	if a==n2:
		break
	
		
if b==n2:
	print('YES')
else:
	print('NO')
