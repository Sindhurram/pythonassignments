print('code started')
def main():
	marks=read('enter the percentage')
	display(marks)

def read(msg):
	return int(input(msg))


def display(marks):
	
	if marks>=85:
		print(f'marks is  {marks} and grade is A')
	elif  marks>=70 and marks<=85:
		print(f' marks is {marks} and grade is B')
	elif marks>=60 and marks<=70:
		print(f' marks is {marks} and grade is C')
	elif marks>=50 and marks<=60:
		print(f' marks is {marks} and grade is D')
	elif marks>=35 and marks<=50:
		print(f' marks is {marks} and grade is E')
	else:	
		print(f' marks is {marks} and grade is fail')
main()
print('code ended')