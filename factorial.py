#factorial of given number
def main():
    n=int(input('enter a number: '))
    res=factorial(n)
    display_nums(n,res)

def factorial(n):
    fact=1
    while n:
        fact*=n
        n-=1
    return fact

def display_nums(n,res):

    print(f' factorial of {n}  is:{res}')

main()