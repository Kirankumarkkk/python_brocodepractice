#variables

name="kiran"             #string double quotes
fullname='kiran kumar k' #string single quotes
age=10                   #int
height=5.4               #float
male=True                #bool
complexvariable=1+2j     #complex

#list tuples and dict

my_list=[10,2.5,"kiran",3+4j,'kiran kumar kkk']    #list different datatypes
my_list1=[1,2,3]  #list 
my_nestedlist=[1,[10,20,30],['a','b','c'],4]  #nested list 
my_tuples=('a','b,','c','d','e','f')      #tuples
my_tuples1=([1,2,3],(4,5,6))       #nested tuples
a,b,c=1,2,3           #tuple assignment
my_dict={'city1':111,'city2':222,'city3':333} #dictionaries dict
my_dict1={(1,2):'start',(3,4):'stop'}     #tuple in dict
height_datatype=type(height)  #datatype
print(name+" "+str(age)+" "+str(height)) #print
print(name+" hello "+fullname) #print variable + variable
print(name[1:5:1])  #string slicing [ start:stop:step increment ]
print(name[:5:1])   #default start
print(name[::-1])   #default start end reverse
print(f"value {2*age} hello {name} name_capital {name.upper()}")  #f"string value*age,lower 2 upper     
print(f"name_captilize {name.capitalize()} name_findr {name.find('r')} ") #capitilize find r
print(f"name_countr {name.count('i')} name_lower {name.islower()}")  #string count i, is lower
print(my_list[1:5:1])   #list start:end:step
print(my_nestedlist[0:5:1])  #nested list [start:end:step increment]
print(f"my_list len {len(my_list)} my_nestedlist {len(my_nestedlist)}") #length of list
my_list[0]=20     #replacing a value in the list
my_list.append(6)  #adding a value to the list
my_list.remove(6)  #removing a value
my_list.pop()    #removing last value from the list
my_list1.extend([4,5,6]) #list extended add this to the list
my_list1.insert(2,20)   #updaing the value in the index 2
print(my_list1.index(1)) #index value of 1
print(my_list1.count(1)) #count value of 1 in the list
print(my_list1 , my_list1)
my_list1.clear()     #clearing the values in the list
print(my_list1)      #print list
print(my_tuples1[0],my_tuples1[1])  #using index to fetch value
print(len(my_tuples1)) #to find the length of tuples
print(my_tuples1)     #print tuples
print(my_tuples[2:6:1]) #tuples[start:stop:step increment] fetch from those index
print(my_tuples.count('a')) #count the value in the tuples
print(my_tuples.index('a'))  #index value of a is 0
print(a,b,c)     #print tuple assignment a,b,c= 1,2,3
a,b=b,a          #swapping tuple assignment values
print(a,b)       #print swapped tuple
print(len(my_dict))  #length of dict
print(my_dict['city1']) #to find the key value 
print(my_dict1)
my_dict['city4']=444  #to add key value pair to dict
print(my_dict)
my_dict['city4']=666  #to update key value pair in the dict
print(my_dict)
del my_dict['city4']  #to delete key value pair in the dict
my_dict.pop('city3') #to remove a key value pair
my_dict.popitem()     #to remove a last key value pair from dict
print(my_dict)
my_dict.clear()       #to delete all the key pairs in the dict
print(my_dict)       
print(my_dict1.items())  #to print dict_items and key pairs
print(my_dict1.keys())    #to print dict keys
print(my_dict1.values())  #to print values
my_dict1.update({(5,6):'step',(7,8):'engage'}) #update key pair values to the dict

#operators
print(1+1)  #add
print(3-1)  #sub
print(3**2) #mul
print(6/2)  #division
print(6//2) #removes decimal in division
print(10 % 2 ) #modulo
print("hello "+","+" world")  #concat of string data types
print(5>3) #greater than
print(3<6) #less than
print(3>=3) #greater than or less than
print(4==4) #comparision operator equal to
print("hello"!="jello") #not equal to operator

#assignment operator
assign_x=10
assign_x += 3 #adding value to variable value and print 
assign_x -= 3  #substract value to variable value and print
assign_x /= 5  #division and print value print(assign_X)
print(assign_x)

#membership operator
assign_y=[1,2,3,4,5]
print( 5 in assign_y)
print( 6 not in assign_y)
assign_message='hello hi'
print('w' in assign_message )

#if/elif/else condition

condition_x=10
condition_y=20
if condition_x!=10:             #if condition
    print("yes condition")
elif condition_x > condition_y:  #elif
    print("yes x < y")
else:                            #else
    print("else statement")
print("End of if statement")

#for loop range ()

#for <loop_variable> in range(<start>, <stop>, <step>):
#    <code>

for n in range(5):
    print(n)   #printing 0 to 4

for n in range(1,5,1):    #range(start,stop,step)
    print("hello "*n)     #printing hello o to 5 times
    
loop_listx=["a","b","c","d","e"]

for i in range(len(loop_listx)):
    print(loop_listx[i])  #print list value 1 by 1
    
for i in range(2,len(loop_listx)):
    print(loop_listx[i])  #print list value 2 by 1
    
for i in range(1,5):
    print(i+1)        #print i+1 start 1 end 5 

for i in range(10,5,-1):
    print(i)          #print 10 to 5 value
    
for i in range(len(loop_listx)-1,1,-1):  
    print(loop_listx[i])   #print e to c start len(list)-1,1,-1 start stop step
    
#iterate string,list,dict

iterate_string="hello kiran"

for i in iterate_string.upper():
    print(i)           #print each character as .upper or .lower() of message string
    
iterate_list=[100,99,98,97,96]

for i in iterate_list:
    print(i)         #print value 1 by 1 from list
    
iterate_dict={"a":1,"b":2,"c":3}

for key in iterate_dict:
    print(key)          #print key from dict

for value in iterate_dict.values():
    print(value)    #print values from dict
    
for key,value in iterate_dict.items():
    print(key,value)   #print key values from dict items
 
for item in iterate_dict.items():
    print(item)      #print key values as tuples from dict   
    
#break

break_list=[1,2,3,4,5]

for i in break_list:
    if i%2==0:
        print("even:",i)
        break                  #break statement used to stop the loop when if condition is met
    else:
        print("odd:",i)

for i in break_list:
    if i%2==0:
        print("continue")
        continue                  #continue statement used to skip the rest of current iteration
    print("odd:",i)
    
#zip function

zip_list1=[1,2,3,4]
zip_list2=[5,6,7,8]
zip_list3=[9,10,11,12]

for i,j,k in zip(zip_list1,zip_list2,zip_list3):  #zip combine multiple lists and print each in seq
    print(i,j,k)              
    
#enumerate function

enumerate_list=[1,2,3,4]

for i,enum in enumerate(enumerate_list):        #enumerate starts at 0 provide sequence for the list
    print(i,enum)

enumerate_message="hello kiran"

for i,message in enumerate(enumerate_message,1):    #string variable, start counter for enumerate
    print(i,message)                                #enumerate message char from o to end 
    

#else for loop

for i in range(1,5):
    if i==1:
        print(i)
        break                #for loop break statement present then else won't run, if break not present else will run
else:
    print("else")            #comment break then run , else will run 
    
#while loop

while_x=1
while_y=1
while while_x<10:           #while loop runs as long as the condition is true 
    print(while_x)          #similar to for loop , while have condition
    while_x+=1
    
while while_y < 10:
    if while_y % 2 == 0:
        print("Even:", while_y)
        break                   #break stops the while loop immediately
    print(while_y)              #continue stops current iteration and start next iteration
    while_y += 1
 
continue_xwhile=5    
while continue_xwhile < 15:
    if continue_xwhile % 2 == 0:
        continue_xwhile += 1
        continue               #continue stops current iteration and start next iteration
    print("Odd:", continue_xwhile)   
    continue_xwhile += 1
else:
    print("All numbers were odd")  #if break found, else doesn't run in while loop
    
#infinite loop

infinite_x=2

while infinite_x<5:
    print(infinite_x)
    infinite_x+=2        #add break or increment to break from infinite loop
    
#nested loop

for i in range(1,3):
    print("=======> outerloop")
    for j in range(2):
        print(i,j)
        
#def function

#def <function_name>(<param1>, <param2>, ...):
#<code>

def pattern(a,b,c):         #def function with params
    defsize=4
    print(a+b,c) 
    print(c)
    for i in range(defsize):
        print("*"*defsize)

pattern(1,2,"hello pattern")           #calling pattern funtion with parameter values

def print_pattern(num_rows):
    for i in range(num_rows):
        for num_cols in range(num_rows-i):
            print("*",end="")                 #print pattern *** ** *
        print()

print_pattern(3)

#def return value

def return_value(a,b=3):      #default parameter value in function
    if a*b==6:
        return a*b                     
    else:
        return None            #based on condition and values, return none or value

print(return_value(2))

def return_valueseq(seq):
    for i in seq:                    
        return i            #passing list values and printing first value
        
print(return_valueseq([1,2,3,4]))

def return_valueseq(seq):
    for i in seq:                    
        print(i)            #passing list values and printing the values one by one
        
return_valueseq([1,2,3,4])

#try/except/else/finally

#try_index=int(input("enter the value:"))     #uncomment to for input 

try:
    my_list = [1, 2, 3, 4]
    print(my_list[try_index])               #try exception with passing value index
except:                                     #except <exception_type> as <name>:  exception type and name
    print("Please enter a valid index.")
else:
    print("skipping this program")        #else will run only if there is no exception
finally:
    print("running finally")             #finally will run only if there is exception
    
#OOP's object-oriented programming 

#class that acts as a blue print, general syntax below

''' class <ClassName>:                     #class name

    <class_attribute_name> = <value>

    def __init__(self,<param1>, <param2>, ...):     #declaring attributes in __init__
        self.<attr1> = <param1>                     #objects will have attributes that we define in the class
        self.<attr2> = <param2>
        .
        .
        .
        # As many attributes as needed

   def <method_name>(self, <param1>, ...):
       <code>

   # As many methods as needed
   
'''

class Dog:                                     #dog class with init method
    
    # Class attributes
    kingdom = "Animalia"
    species = "Canis lupus"

    def __init__(apple, name, age=10):          #default arguments also we can pass
        apple.name = name        #public attribute       
        apple._age = age         #non-public attributes
        apple.speed= 50
        
    def bark(apple):                              #bark method creation
        print(f"woof-woof. I'm {apple.name}")
        
    def increment_speed(apple, value):         #increment method
        apple.speed += value
        
    @property                    #in python, we use properties for getter and setter
    def name(apple):
        print("calling getter")
        return apple._name

    @name.setter
    def name(apple, new_name):
        print("calling setter")
        apple._name = new_name

    @name.deleter
    def name(apple):
        print("calling deleter")
        del apple._name
        
                                 #some class doesn't need argurment, in that case, it will be empty
my_dog = Dog("Nora", 11)         #instance to call class with values(arguments) to attributes

my_dog.bark()                   #calling method after creating instance

my_dog1=Dog("kiddy")            #creating another instance dog1

print(my_dog1.name)             #checking name and speed values
print(my_dog1.speed)
my_dog1.increment_speed(5)      #incrementing the speed and value with method
print(my_dog1.speed)            #print updated value


print(my_dog.name,my_dog._age)    #to fetch instance attribute values

my_dog.name="Norita"             #update instance attribute

print(my_dog.name,my_dog._age)    #printing updated instance attribute

#del my_dog.name             #delete instance attribute and if we try to fetch, it will throw error   

print(my_dog.name,my_dog._age)

#del my_dog                   #delete instance and it will throw error if we try to fetch

print(my_dog.name)           #print instance attribute value

print(Dog.species)           #print class attribute values
print(Dog.kingdom)

Dog.kingdom="New kingdom"   #updating class attribute and printing

print(Dog.kingdom)

#del Dog.kingdom             #delete class attribute

print(Dog.kingdom)           #uncomment above line for delete class attribute

my_dog2=Dog("Bubble")        #creating instance for properties setter

print(my_dog2.name)        

my_dog2.name="doodle"        #setter

print(my_dog2.name)          #getter

del my_dog2.name             #deleter

#to open the file and read
'''
with open("famous_quotes.txt","r") as file:
    for line in file:                            #uncomment and test
        print(line)
'''
        
#create new file and update the content fully in file 

words = ["Amazing", "Green", "Python", "Code","new line 1"]

with open("famous_quotes.txt", "w") as file:
    for word in words:
        file.write(word + "\n")
        
#create new file and append to the existing content , add to exisiting content in the file

words = ["Amazing", "Green", "Python", "Code","new line 2"]

'''
with open("famous_quotes.txt", "a") as file:
    for word in words:                           #uncomment and test this code
        file.write(word + "\n")
'''

#delete a file 

import os

if os.path.exists("famous_quotes1.txt"):          #file path and file with extension
  os.remove("famous_quotes1.txt")
  print("file is deleted")
else:
  print("This file doesn't exist")
  

import math
import math as m
from math import sqrt
from math import sqrt as square_root
from math import *                   #import all elements of module

print(m.sqrt(25))
print(sqrt(36))

'''
The four pillars of OOP are:
Encapsulation: Focuses on bundling data and restricting access.
Abstraction: Focuses on hiding complexity and exposing only necessary details.
Inheritance :  Car inherits the brand and start() method from Vehicle, but it also has its own attribute (model) and method (display_info()).
Polymorphism : Polymorphism allows different types of objects to respond to the same action in their own unique way

'''

#encapsulation example -----------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute (notice the double underscore)

    def get_age(self):
        return self.__age  # A method to access the private age attribute

my_person=Person("Kiddy",28)
print(my_person.name)

print(my_person.get_age())  #age kept privat so, can only get using get_age() method

#Abstraction  example -----------------------------------------

class Car:
    def start_engine(self):
        print("Engine started")

    def drive(self):
        print("Car is driving")
        
    def stop(self):
        print("Car is stopping")

# The user interacts with the car without knowing how the engine works
my_car = Car()
my_car.start_engine()
my_car.drive()
my_car.stop()

#inheritance  example -----------------------------------------

# Parent class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand  # This is an attribute (brand)

    def start(self):
        print(f"{self.brand} vehicle started")  # This is a method

# Child class that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Inherit the brand from Vehicle (parent class)
        self.model = model  # Add a new attribute specific to Car

    def display_info(self):
        print(f"Car: {self.brand}, Model: {self.model}")

# Creating an object of the Car class
my_car = Car("IVM", "Ikenga")
my_car.start()  # Output: IVM vehicle started
my_car.display_info()  # Output: Car: IVM, Model: Ikenga

#Polymorphism example -----------------------------------------

# Parent class
class Animal:
    def sound(self):
        return "Some generic animal sound"

# Child class Dog overriding the sound method
class Dog(Animal):
    def sound(self):
        return "Bark"

# Child class Cat overriding the sound method
class Cat(Animal):
    def sound(self):
        return "Meow"

# Creating instances of each class
my_dog = Dog()
my_cat = Cat()

# Calling the sound method
print(my_dog.sound())  # Output: Bark
print(my_cat.sound())  # Output: Meow


#method overloading -----------------------------------------------------------------

#Method overloading happens when you create multiple methods with the same name, but with different types of parameters inside the same class.

#eg 1 --------------------------------------------------------------------------------

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Create an instance of Calculator
calc = Calculator()

# Call the add method with different numbers of arguments
print(calc.add(5))        # Output: 5 (a = 5, b and c default to 0)
print(calc.add(5, 10))    # Output: 15 (a = 5, b = 10, c default to 0)
print(calc.add(5, 10, 15))# Output: 30 (a = 5, b = 10, c = 15)

#eg 2 -------------------------------------------------------------------------------

class Calculator:
    def add(self, *args):
        return sum(args)

# Create an instance of Calculator
calc = Calculator()

# Call the add method with different numbers of arguments
print(calc.add(5))           # Output: 5 (adds just one number)
print(calc.add(5, 10))       # Output: 15 (adds two numbers)
print(calc.add(5, 10, 15))   # Output: 30 (adds three numbers)

# Constructor __init__ initialise
# A constructor is a special method that automatically runs when you create a new object from a class. It helps to set up the object's initial values (like setting the name or age of a person).

class Student:
    def __init__(self, name, grade):  # The constructor method
        self.name = name  # Setting the name when the object is created
        self.grade = grade  # Setting the grade when the object is created

# Creating a new Student object
student1 = Student("Alice", "A")

# Accessing the student's details
print(student1.name)  # Output: Alice
print(student1.grade)  # Output: A

#destructor __del__ del object ------------------------------------------------------------------------------------
#A destructor is a method that is called when an object is destroyed. In Python, the destructor is defined using __del__.

class Demo:
    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")

obj = Demo()
del obj  # Explicitly calling the destructor