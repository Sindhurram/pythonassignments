#WAP to find square of num
def main():
        n=read('enter the value ')
        display(area(n),perimeter(n))

def read(msg):
    return int(input(msg))

def area(n):
    return n**2

def perimeter(n):
    return 4*n

def display(area,perimeter):
    print(f'the area  of square is {area}')
    print(f'the area  of square is {perimeter}')
main()