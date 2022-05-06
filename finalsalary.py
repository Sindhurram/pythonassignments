#Design a system to calculate salary of employee at the end of month 
#given their salary,days worked and working days
print('code started')

def main():
    salary=read('enter the salary of employee:')
    days_worked=read('enter no of days worked:')
    working_days=read('enter no of working days:')
    end_of_month_sal= sal_cal(salary,days_worked,working_days)
    display(end_of_month_sal)
  
    def sal_cal(salary,days_worked,working_days):
        per_day_sal=salary/30
        extra_days=days_worked-working_days

        if extra_days>0:
            salary += extra_days*2*per_day_sal
        elif extra_days+2<0:
            salary +=(extra_days+2) * per_day_sal
            return salary
 
    def display(end_of_month_sal):
           return float(input())
            print(f'salary of the month= {end_of_month_sal}')
      
    def (msg):
          return int(input(msg))
   
main()