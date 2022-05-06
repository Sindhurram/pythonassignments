#WAP to check given number  is automorphic or not
def main():
    num=int(input('enter a number:  '))
    sq=num**2
    ln=len(str(num))
    sqln=len(str(sq))
    #print(f'{ln}')
    #print(f'{sqln}')
    print(f'square of {num} is {sq}')
    if num%10!=sq%10:
        print(f'{num} is not automorphic')
    else:
        print(f'{num} is automorphic')
main()