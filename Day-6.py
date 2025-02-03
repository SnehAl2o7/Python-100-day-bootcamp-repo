#PROJECT NUMBER 6
#PRACTICE NO-6
#CREATING FUNCTION
#SYNTAX
#def function_name(parameters)->RETURN-TYPE:
#   function body
# return value

def sum(a:int, b:int)->int:#creating a function 
    # with parameters and return type
    return a+b
add = sum(3,4)
print(add)

def sum(a:int , b:int):#creating a parameter function
    return a+b      #return sum
print(sum(3,4))

def sum(): #creating a function without parameter
    print(2+4)
sum()