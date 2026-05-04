'''
elif (else if)
nested conditional statements
marks=int(input('Enter your marks: '))
if marks>=0 and marks<=100:
    if marks>=80 and marks<=100:
        print(marks,'Grade \'A\'')
    elif marks>=70 and marks<80:
            print(marks,'Grade \'B\'')
    elif marks>=40 and marks<70:
        print(marks,'Grade C')
    else:
        print(marks,'Grade \'F\'')   
else:
     print('Enter a proper marks') 
match case (3.12)
day=int(input('Enter the Number to find the day: '))

match day:
    case 0:
        print('SUN')
    case 1:
        print('MON')
    case 2:
        print('TUS')
    case 3:
        print('WED')
    case 4:
        print('THURS')
    case 5:
        print('FRI')
    case 6:
        print('SAT') 
    case _:
        print('Enter a proper day number from 0 to 6')  
 
'''


print('''
Welcome to AchieversIT
-----------------------
COURSES WE HAVE
1.PFS
2.JFS
3.DA
4.DS
5.DASE ADMIN                                          
''')
COURSE=input('Choose your course:')                          
      

