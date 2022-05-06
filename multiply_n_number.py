#print first n natural number and total sum
def main():
    n=read('enter a number: ')
    display_nums(n)

def display_nums(n):
    start=1
    stop=1
    mul=1
    while(start<=n):
        print(start)
        mul=start*mul
        start+=stop
        
    print(f' multiplication of n number  is:{mul}')
def read(msg):
		return float(input(msg))
main()