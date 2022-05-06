#WAP to print all factors of given num USING WHILE LOOP
def main():
    num=int(input('enter a  number to find factors: '))
    display_factors(num)

def  display_factors(num):
    start=1
    while start<=num:
        if num%start==0:
            print(start)
        start+=1
        
main()
