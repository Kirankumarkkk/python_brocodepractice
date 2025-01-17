name="kiiran"             #string double quotes
fullname='kiran kumar k' #string single quotes
age=10                   #int
height=5.4               #float
male=True                #bool
complexvariable=1+2j     #complex
my_list=[10,2.5,"kiran",3+4j]    #list different datatypes
my_nestedlist=[[10,20,30],['a','b','c']]     #nested list
my_nestedlist1=[1,[10,20,30],['a','b','c'],4]  #nestedlist 
height_datatype=type(height)  #datatype
age_datatype=type(age)
male_datatype=type(male)
print(name+" "+str(age)+" "+str(height)+" "+str(male))
print(my_list)
print(complexvariable)
print(fullname)
print(height_datatype)
print(age_datatype)
print(male_datatype)
print(type(complexvariable))
strindexname=name[1:5:1]   #string slicing [start : stop : step]
strindexnamelast=name[-1]  #string slicing
print(strindexname)
print(strindexnamelast)
print(name[2:5:1])  #start end step
print(name[:5:1])   #default start 
print(name[::-1])   #default start end step reverse string
print(f"hello {name} full_name {fullname}")  #f"string variable to value
print(f"value {2*age} hello {name} full__name {fullname}")  #f"string multipying value 2*age,2*10     
print(f"value {2*age} hello {name} name_capital {name.upper()}")  #f"string value*age,lower 2 upper     
print(f"name_captilize {name.capitalize()} name_findr {name.find('r')} ") #capitilize find r
print(f"name_countr {name.count('i')} name_lower {name.islower()}")  #string count i, is lower
print(my_list[1:4:1])   #list start:end:step
print(my_nestedlist[0:2:1])  #nested list start:end:step
print(my_nestedlist[:2])   #nested list start default
print(my_nestedlist1[1:5:1])  #nested list start:end:step
print(f"my_list len {len(my_list)} my_nestedlist {len(my_nestedlist)}") #length of list
print(my_list)
my_list[0]=20        #replacing a value
print(my_list)
my_list.append(6)    #adding value to the list
print(my_list)
my_list.pop()   #remove last value from the list
print(my_list)  