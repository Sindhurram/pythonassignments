#WAP to print prime number below given number
def main():
    num=int(input('enter a  of number'))
    print(f'prime number below {num} are:')
    first_n_prime(num)

def first_n_prime(num):
    start=2
    for val in range(start,num):
        if val>1:
            for i in range(2,val):
                if val%i==0:
                    break
            else:
                print(val,end=' ')                    
main()