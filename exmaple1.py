# def calculator(a,b):
# 	"""calculator()-this is actually performing addition,subtraction,multiplication and divison"""
# 	x=a+b
# 	y=a-b
# 	z=a*b
# 	q=a/b
# 	return x,y,z,q
# res1,res2,res3,res4=calculator(10,20)
# print(res1,res2,res3,res4)
# print(calculator.__doc__)

# def power_off(num,power):
# 	return num**power
# res1=power_off(2,5)
# res2=power_off(5,2)
# print(res1)
# print(res2)


# from turtle import Turtle
# t=Turtle()
# t.color("black")
# t.fillcolor("red")
# for i in range(4):
#       t.fd(200)
#       t.lt(90)	 

# print("Enter the first number for addition:")
# a = int(input())
# print("Enter the second number for addition:")
# b = int(input())
# c = a + b
# print("The added result is:", c)

with open("example.text",'r')as s:
	print(s.read())

# with open ("example",'w')as s:
# 	s.write("INDIA\n")
# 	s.write("won\n")
# 	s.write("the\n")
# 	s.write("match\n")/

try
	with open("sunil",'r'):
		for line in s:
			print(line,end='')
except FileNotFoundError:
		print("file does not exist!!")


