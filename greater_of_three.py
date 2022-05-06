#WAP to find greater of three num
def main():
    num1=read('enter a number: ')
    num2=read('enter 2nd number: ')
    num3=read('ener 3rd number: ')
    display_greater_of_three(num1,num2,num3)

def display_greater_of_three(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            print(f'{num1} is greater than {num2} and {num3}')
        else:
            print(f'{num3} is greater than {num1} and {num2}')
    elif num2>num3:
        print(f'{num2} is greater than {num1} and {num3}')
    else:
        print(f'{num3} is greater than {num1} and {num2}')
def read(msg):
		return float(input(msg))
main()
