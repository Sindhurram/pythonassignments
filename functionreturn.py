print('fucntion using return')
num1=int(input('enter 1st number'))
num2=int(input('enter 2nd number'))

def square(num):
	sq=num**2
	return sq
sq_num1=square(num1)
sq_num2=square(num2)

def add(n1,n2):
	return n1+n2

sum1=add(num1,num2)
sum2=add(sq_num1,sq_num2)

def sub(n1,n2):
	return n1-n2

print(f'the difference is {sub(sum2,sum1)}')
