#WAP to find prime or not
def main():
    num=int(input('enter a number:      '))
    display(num,is_prime(num))

def is_prime(num):
    if count_of_factors(num)==2:
        return True
    return False

def count_of_factors(num):
    count=0
    for var in range(1,num+1):
        if num%var==0:
            count+=1
        return count

def display(num,flag):
    if flag is True:
        print(f'{num=} is prime')
    else:
        print(f'{num=} is not prime')
main()