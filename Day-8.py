#PROJECT NUMBER - 8
#PRACTICE NO-1
def greet():
    print("HEllo")
    print("How are you")
    print("hope you this message find you in your best regards")

greet()

def greet(name):
    print("Hello", name)
name = "snehal"
greet(name)

def greet_name(name,age):
    print(f"Hello {name}")
    print(f"you are {age} years old")

greet_name("snehal","20") #Positional argumnet

#PROJECT NUMBER - 8
#PRACTICE NO-1
def greet():
    print("HEllo")
    print("How are you")
    print("hope you this message find you in your best regards")

greet()

def greet(name):
    print("Hello", name)
name = "snehal"
greet(name)

def greet_name(name,age):
    print(f"Hello {name}")
    print(f"you are {age} years old")

greet_name("snehal","20") #Positional argumnet


#Practice NO- 2
#Creating paint calculator
test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5
def print_cal(h :int,b : int,cover : int):
    print(f"You'll need {int((h*b)/cover)} cans of paint.")
print_cal(test_h,test_w,coverage)

#Practice NO-3
num = int(input("Check the number:"))
def prime_checker(num):
    val = 0
    for i in range(2,num):
        if num%i != 0:
            val += 1
    
    if val == 0:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime") 
prime_checker(num);
       

#FINAL PROJECT
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
             'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
what = True
while(what):
    direct = input("Type 'encode' to encrypt, type 'decode' to descrypt: ")
    text = input("Type your meaasage: ").lower()
    shift = int(input("Type the shift number: "))
    def ceaser(direct,text, shift : int):
        if(direct == "decode"):
            shift *= -1
        cipher = ""
        for i in text:
          if(i in alphabets):
            pos = alphabets.index(i)
            new_pos = pos+ shift
            new_i = alphabets[new_pos]
            cipher += new_i
          else:
            cipher += i
        print(f"The {direct}d text is {cipher}")    
    shift %= 26
    ceaser(direct,text,shift)
    value = input("do you like to continue yes/no:")
    if(value == "no"):
        what = False
   

