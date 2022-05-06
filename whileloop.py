#print first n natural number
def main():
    n=read('enter a number: ')
    display_nums(n)

def display_nums(n):
    start=1
    stop=1
    while(start<=n):
        print(start)
        start+=stop

def read(msg):
		return float(input(msg))
main()