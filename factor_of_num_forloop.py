#WAP to print all factors of given num USING FOR LOOP
def main():
    num=int(input('enter a  number to find factors: '))
    display_factors(num)

def  display_factors(num):
    start=1
    for var in range(1,num+1):
        if num%var==0:
            print(var)
        start+=1
main()
