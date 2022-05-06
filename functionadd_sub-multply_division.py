#add two number
print('code started')

def main():

    num1=int(input('enter 1st number:'))
    num2=int(input('enter 2nd number:'))
    print(num1,'+',num2,'=',num1+num2)#old method of formatting
    print(f'{num1}+{num2}={num1+num2}')#new method of formatting add two number
    print(f'{num1}-{num2}={num1-num2}')#subtract two number
    print(f'{num1}*{num2}={num1*num2}')#multiply two number
    print(f'{num1}/{num2}={num1/num2}')#divide two number
main()
print('code ended')
