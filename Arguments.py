#default arguments
def add(num1=10,num2=20):

	print(f'{num1=}+{num2=}={num1+num2}')
add(100,200)
add(12)
add(10)

#explicitly arguments

print('=============assign values explicitly arguments============')
def add(num1,num2):
	print(f'{num1=}+{num2=}={num1+num2}')
add (num2=100, num1=250)

#keyword Variable arguments:
print('=============keyword variable arguments============')
def add(*args):
	print(args)
add()
add(3,20)
add(1,2,3,4,5,6,7,8)

#keyword  arguments:
print('=============keyword  arguments============')

print(10,'this is first',sep='-->',end='\t')
print('wow')
