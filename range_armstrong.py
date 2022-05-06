#WAP  print  amstrong number between range of numbers
def main():
    lower=int(input('enter a lower limit number'))
    upper=int(input('enter a upper limit number'))
    first_n_armstrong(lower,upper)

def first_n_armstrong(lower,upper):
    for var in range(lower,upper+1):
        ln=len(str(var))
        sum=0
        temp=var
        while temp>0:
            digit=temp%10
            sum=sum+digit**ln
            temp//=10
            if var==sum:
                print(var)
main()