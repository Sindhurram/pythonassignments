#WAP to print range of numbers from -ve to =ve(-250 to 250) and 
# from n1 to n2 NOTE:: num2>num1 do increment num1<num2 do decrement

def main():
    start=read('enter a start number: ')
    stop=read('enter a end number: ')
    greater=greater_of_two(start,stop)
    if greater==stop:
        display_inc(start,stop)
    else:
        display_dec(start,stop)
def read(msg):
    return int(input(msg))

def greater_of_two(num1,num2):
    if num1>num2:
        return num1
    return num2

def display_inc(start,stop):
    while start<=stop:
        print(start)
        start+=1
def display_dec(start,stop):
    while start>=stop:
        print(start)
        start-=1

main()