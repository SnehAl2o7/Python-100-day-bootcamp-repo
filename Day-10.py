#PROJECT NO-10
#PRACTICE NO-1
#Functions with Outputs

def format_namep(f_name,l_name):
    print(f"{f_name.title()} {l_name.title()}")

def format_namer(f_name,l_name):
    a = f_name.title()+l_name.title()

format_namep("Snehal","Singh")

#Practice no- 2
def isleap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def days_in_month(month,year):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    if isleap(year):
        month_days[1] = 29
    
    return month_days[month-1]

year = int(input("Enter year: "))
month = int(input("Enter month :"))
print(f"Number of day in {month} th month of {year} is {days_in_month(month,year)}")

#DOCSTRING
"""
    Hello Guys I'm learning PYthon
    And it's really going well and enjoying it so much
    What about you are u improving or not

"""

#Practice no-

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b;

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    else:
        return a/b
    
operator = {"+": add,"-":subtract,"*":multiply,"/" : divide}

def calculator():
    a = float(input("Enter the first number :"))
    for i in operator:
        print(i)
    cont = True
    while cont:
        operation = input("Pick up an operation :")
        b = float(input("Enter the second number :"))
        calculation = operator[operation]
        ans= calculation(a,b)
        print(f"Result of {a} {operation} {b} is {ans}")
        check = input("type y to continue and to start new calculation type N and to exit completely type anything ")
        if check == 'y':
            a = ans
        elif check == 'N':
            cont = False
            calculator()
        else:
            cont = False

calculator()

