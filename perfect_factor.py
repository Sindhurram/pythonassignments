#WAP to find number is  perfect factors  or not
def main():
    num=int(input('enter a  number to find factors: '))
    if num==1:
        print(f'{num} is perfect factor')
    else:
        list=display_factors(num)
    
def  display_factors(num):
    start=1
    total=0
    while start<=num:
        if num%start==0:
            print(start)
            total+=start
        start+=1 
    total-=num
    if total==num:
        print(f'{num} is perfect factor')
    else:
        print(f'{num} is not perfect factor')
main()
