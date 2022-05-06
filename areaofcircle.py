def main():
	radius=read('enter the radius of the circle:')
	display(area(radius),radius)

def read(msg):
	return float(input(msg))

def area(radius):
	return(22/7)*radius*radius

def display(area,radius):
	print(f'the are of circle with {radius=} is {area}')

main()