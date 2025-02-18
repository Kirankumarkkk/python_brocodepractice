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

''' class <ClassName>:

    <class_attribute_name> = <value>

    def __init__(self,<param1>, <param2>, ...):
        self.<attr1> = <param1>
        self.<attr2> = <param2>
        .
        .
        .
        # As many attributes as needed

   def <method_name>(self, <param1>, ...):
       <code>

   # As many methods as needed
   
'''
