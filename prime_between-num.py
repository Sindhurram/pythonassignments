#WAP to print prime number bwtween  two number
def main():
    lower=int(input('enter a  of number'))
    upper=int(input('enter a  of number'))
    print(f'prime number  {lower} and {upper} are:')
    first_n_prime(lower,upper)

def first_n_prime(lower,upper):
    for val in range(lower,upper):
        if val>1:
            for i in range(2,val):
                if val%i==0:
                    break
            else:
                print(val,end=' ')                    
main()