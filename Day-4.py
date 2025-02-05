#PROJECT NUMBER- 4
#PRACTICE NO - 1

#to import random
import random
#to import random integer
c = random.randint(1, 10)
print(c)
#random module -> each module is responsible for different functionality
import my_module #import from local file
print(my_module.pi)

#generating random float between 0 and 1
fl = 3*random.random()
print(fl)

#FLIP THE COIN
coin = random.randint(0,1)
if coin == 0:
    print("HEADS")
else:
    print("TAILS")

#PRACTICE NO-2
#LIST DATATYPE
#SYNTAX
#LIST = [item1, item2, item3, item4, item5]
states_of_India = ["Uk","UP","HP","MP"]
print(states_of_India[-1])
#0 is from start index and -1 is the last index
print(states_of_India)
states_of_India.extend("AP")
print(states_of_India)

#PRACTICE NO-3
names = ["ello","ratio","m"]
name= random.choice(names)
print(name)

#PRACTICE NO-4
#TREASURE HUNT -2
row1 = ["*","*","*"]
row2 = ["*","*","*"]
row3 = ["*","*","*"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
hori = int(position[0])
verti = int(position[1])
map[hori-1][verti-1] = "X"
print(f"{row1}\n{row2}\n{row3}")

#PROJECT NUMBER -4
print("What do you choose?")
print("type 0-> Rock,1 for Paper,2 for Scissors")
us = int(input("Enter your choice: "))
u = random.randint(0,2)
if(us == u):
    print(u)
    print("Tie!")
elif (us == 0 and u == 1)or(us == 1 and u == 2) or (us == 2 and u == 0):
    print(u)
    print(" You lose!")
else:
    print(u)
    print("You win!")

            
