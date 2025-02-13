#DICTIONARIES
#A dictionary is a collection of key-value pairs. 
# It is an unordered and mutable collection of items.   
# It consist of key adn value pairs.
#Both working as {key,values}

dict = {"name":"snehal","age":"20","gender" : "male"}
print(dict["name"]) #prints name

empty_dict = {};
dict["place"] = "Dwarahat";
dict["college"] = "BTKIT";
print(dict)

for ch in dict:
    print(ch)
    print(dict[ch])
# Practice number of times
student = {"Harray" : "81","Ron" : "78"}
for key in student:
    if int(student[key]) > 90:
        student[key] = "outstanding"
    elif int(student[key]) > 80 :
        student[key] = "exceeds exception"
    elif int(student[key]) > 70 :
        student[key] = "acceptable"
    else :
        student[key] = "bad"
print(student)

#Practice -3
#Nesting a dictionary 
#normal 
capital = {"Indai" : "New Delhi","USA" : "Washington"
           ,"UK" : "London"};

#nesting a list in dictionary
travel = {"France" : ["paris","lille","Dijon"],"India" : ["delhi","nainital"]}

#nesting a dictionary in a dictionary
student = {"Harray" : {"maths" : 90,"science" : 80},
           "Snehal" : {"maths" : 80,"science" : 75}}

#nesting a dictionary inside a list
name = [{"cities" : ["nainital","mumbai"]},{"place" : ["mall","mountains"]}]

# Practice -4

#Dictionary methods
travel = [{
    "country" : "France",
    "visit" : 12,
    "cities" : ["paris","Hamburg","stuttgart"]
},
{
    "country" : "germany",
    "visit" : 15,
    "cities" : ["Berlin","Hamburg","Stuttgart"]
}
]
def addcountry(list,dict):
    list.append(dict)

new_country = {"country" : "Russia",
               "visit" : 2,
               "cities" : ["moscow","saint petersburg"]}

addcountry(travel,new_country)
print(travel)

#PROJECT NO-8
bid = {}
print("Start the auction :")
again = True
while(again):
    name = input("Enter your name : ")
    amount = float(input("Enter the bid amount:"))
    def add_bidder(name,amount):
        bid[name] = amount
    add_bidder(name,amount)
    re = input("If there any other user who want to bid :")
    if re == "no":
        again = False
def findlarge():
        return max(bid,key=bid.get)
#print(bid)
print(findlarge())
