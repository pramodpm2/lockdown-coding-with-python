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
