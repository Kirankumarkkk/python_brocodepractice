name="kiran"             #string double quotes
fullname='kiran kumar k' #string single quotes
age=10                   #int
height=5.4               #float
male=True                #bool
complexvariable=1+2j     #complex
my_list=[10,2.5,"kiran",3+4j,'kiran kumar kkk']    #list different datatypes
my_list1=[1,2,3]  #list 
my_nestedlist=[1,[10,20,30],['a','b','c'],4]  #nested list 
my_tuples=('a','b,','c','d','e','f')      #tuples
my_tuples1=([1,2,3],(4,5,6))       #nested tuples
a,b,c=1,2,3           #tuple assignment
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


        