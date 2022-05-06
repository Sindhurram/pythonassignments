print('code started')
def main():
	num=read('enter a number')
	res=reminder(num)
	display(num,res)

def read(msg):
	return int(input(msg))

def reminder(num):
	return num%2

def display(num,res):
	
	if res==0:
		print(f'{num} is even')
    else:
		print(f'{num} is not even')
main()
print('code ended')