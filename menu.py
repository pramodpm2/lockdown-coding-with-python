'''
Write a menu program in Python to find Area-Circle, Circumference-Circle, Area- Square, Circumference-Square using functions with menu choice
Create seperate functions for each choice of menu
'''

#save as main.py
def AreaCircle(r):
	return r*r
def CircumferenceCircle(r):
	return 2*3.14*r

def AreaSquare(b,h):
	return b*h
def CircumferenceSquare(h):
	return 4*h

#save as pm.py

from main import*

r=float(input("Enter Radius Of Circle: "))
ac=AreaCircle(r)
print("Area Of Circle: ",ac)
cc=CircumferenceCircle(r)
print("Circumference Of Circle is: ",cc)


b=float(input('Enter Base Of Square: '))
h=float(input('Enter Height Of Square: '))
As=AreaSquare(b,h)
print("Area Of Square Is: ",As)
cs=CircumferenceSquare(h)
print("Circumference Of Square Is: ",cs)
