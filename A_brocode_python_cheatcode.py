name="kiiran"             #string double quotes
fullname='kiran kumar k' #string single quotes
age=10                   #int
height=5.4               #float
male=True                #bool
complexvariable=1+2j     #complex
my_list=[10,2.5,"kiran",3+4j,'kiran kumar kkk']    #list different datatypes
my_nestedlist=[1,[10,20,30],['a','b','c'],4]  #nestedlist 
height_datatype=type(height)  #datatype
print(name+" "+str(age)+" "+str(height)) #print
print(name[1:5:1])  #string slicing [ start:stop:step increment ]
print(name[:5:1])   #default start
print(name[::-1])   #default start end reverse
print(f"value {2*age} hello {name} name_capital {name.upper()}")  #f"string value*age,lower 2 upper     
print(f"name_captilize {name.capitalize()} name_findr {name.find('r')} ") #capitilize find r
print(f"name_countr {name.count('i')} name_lower {name.islower()}")  #string count i, is lower
print(my_list[1:5:1])   #list start:end:step
print(my_nestedlist[0:5:1])  #nested list start:end:step
print(f"my_list len {len(my_list)} my_nestedlist {len(my_nestedlist)}") #length of list
my_list[0]=20     #replacing a value in the list
my_list.append(6)  #adding a value to the list
my_list.remove(6)  #removing a value
my_list.pop()    #removing last value from the list
print(my_list)
