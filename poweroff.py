#WAP to find power of number

def main():
    base=int(input('enter a base number: '))
    exp=int(input('enter a exponent number: '))
    res=power(base,exp)
    display_nums(base,exp,res)

def power(base,exp):
    res=1
    while exp:
        res*=base
        exp-=1
    return res
def display_nums(base,exp,res):

    print(f'  {base}  to power of {exp} is:{res}')

main()