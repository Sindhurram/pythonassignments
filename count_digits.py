#WAP to find number of digits in given number
def main():
    num=int(input(' enter a number'))
    find_count(num)

def find_count(num):
    count=0
    temp=num
    while num:
        last_digit=num%10
        count+=1
        num=num//10
    print(f'{temp} has {count} digits')
main()