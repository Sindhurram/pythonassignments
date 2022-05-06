#print first n natural number and total sum
def main():
    n=read('enter a number: ')
    display_nums(n)

def display_nums(n):
    start=1
    stop=1
    sum=0
    while(start<=n):
        print(start)
        sum=start+sum
        start+=stop
        
    print(f'Total sum is:{sum}')
def read(msg):
		return float(input(msg))
main()