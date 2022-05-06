#WAP to check given number is neon number or not
def main():
    num=int(input('enter a number'))
    sq=num**2
    add(num,sq)
        

def add(num,sq):
    res=num
    sum=0
    while sum<num:
        rem=sq%10
        rem_digit=sq//10
        sum=rem+rem_digit
    print(sum)
    if sum==res:
        print(f'{res} is neon number')
    else:
        print(f'{res} is not neon number')
main()







