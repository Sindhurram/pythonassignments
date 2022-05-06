print('code started')

def main():
    marks=float(input('enter the marks of the student:'))
    grade=grade_scored(marks)
    display(grade)

def grade_scored(marks):
    if marks>100 or marks<1:
        return 'wrong marks'
    elif marks>85:
        return 'A'
    elif marks>70:
        return 'B'
    elif marks>60:
        return 'C'
    elif marks>50:
        return 'D'
    elif marks>35:
        return 'E'
    else:
        return 'F'

def display(grade):
    if len(grade)>1:
        print(grade)
    else:
         print(f'the student has scored {grade=}')

main()