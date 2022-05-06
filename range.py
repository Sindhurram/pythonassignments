#WAP to print range of numbers  ,get input from user input

def main():
    n1=read('enter a start number: ')
    n2=read('enter a end number: ')
    display_nums(n1,n2)

def display_nums(n1,n2):
    start=1
    while(n1<=n2):
        print(n1)
        n1+=start

def read(msg):
		return float(input(msg))
main()