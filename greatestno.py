print('code started')
def main():
	num1=read('enter a 1st number')
	num2=read('enter a 2nd number')
	greateroftwo(num1,num2)

def read(msg):
	return int(input(msg))

def reminder(num):
	return num%2

def greateroftwo(num1,num2):
	
	if num1>num2:
		print(f'{num1} is greater')
	else:
		print(F'{num2} is greater')

main()
    