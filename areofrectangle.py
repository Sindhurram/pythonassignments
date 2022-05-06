def main():
	length=read('enter the len of rectangle:')
	breadth=read('enter the breadth of rectangle:')
	area_of=area(length,breadth)
	display(length,breadth,area_of)

def read(msg):
		return float(input(msg))

def area(length,breadth):
		return length * breadth

def display(length,breadth,area_of):
		print(f'the area of rectangle with {length=} and {breadth=} is {area_of}')

main()