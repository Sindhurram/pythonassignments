#WAP to print number is palindrome or not
def main():
    num=int(input(' enter a number'))
    find_palindrome(num)

def find_palindrome(num):
    temp=num
    rev=0    
    while num:
        last_digit=num%10
        rev=rev*10+last_digit
        num=num//10
    if temp==rev:
        print(f'{temp} is palindrome ')
    else:
        print(f'{temp} is not palindrome ') 
main()