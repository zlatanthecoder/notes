->4 / 2 = 2.0
->4 // 2 = 2  // means Integer Division
-> 2 ** 3 = 8  ** means Power of 
-> print('hello') = print("hello")
->print("Hello's world") = Hello's world
->print('Hello "World"') = Hello "World"
->print('Hello\'s "World"') = Hello's "World"
->'hello'*3 = 'hellohellohello'
->print('c:\doc\name')
c:\doc
ame
->print(r'c:\doc\name') = c:\doc\name
r tells python to print the raw string. donot convert anything
->_+x  _(underscore) means use result from the previous operations & add it to x
->name='hello'
name[0] = 'h'
name[4] = 'o'
name[-1] = will give the last letter from the right which is 'o'
name[-2] = will give the second last letter from the right which is 'l'
so - will print the values from the last
name[0:2] = 'he' it means starting from index 0 & end with [2-1] index
name[1:4] = 'ell' starting from index 1 & end with [4-1] index

#mentioning the starting poin & not specify ending point
name[2:] = 'llo' it will start with 2 index & print till the last

#mentioning the ending point but not the starting point
name[:4] = 'hell' it will start with the 1st letter & ends with index [4-1]

#we dont have 10-1 index here but it will not give any errors.
name[2:10] = 'llo'  it will print till the last characters

#Strings in python is immutable so we cant change the values
name[0]='S' TypeError: 'str' object does not support item assignment 

#length of String. len is inbuilt function in python
len(name) = 5

->#creating a list. list is mutable means we can change the values
nums = [10,20,50,60]

#accessing individual element
nums[3] = 60

#starting from index 2 which is 3rd element & print till the end
nums[2:] = [50, 60]

#-1 means print last value
nums[-1] = 60

#we can create list of different types of values
values = [10,5.5,'hello'] 

#creating a list with 2 list objects
mis = [nums, values] #[[10, 20, 50, 60], [10, 5.5, 'hello']]

#append function will append value at the end
nums.append(100) #[10, 20, 50, 60, 100]

#insert function will insert the value at a particular index
nums.insert(2,1002) #[10, 20, 1002, 50, 60, 100]

#remove(index) function remove the element passed
nums.remove(1002) #[10, 20, 50, 60, 100]

#pop(index) will remove the value present in index 3 & return it
nums.pop(3) #60

#pop() will remove the last element & returns it
nums.pop()  #100

#delete all values starting from index 2 till the last
del nums[2:] [10, 20]

#add multiple values in list
nums.extend([44,55,66,77])  #[10, 20, 44, 55, 66, 77]

min(nums) #10
max(nums) #77
sum(nums) #272
nums.sort() #[10, 20, 44, 55, 66, 77]

->#Tuple= immutable list is tuples means we cannot change the values
tup = (50,40,60,30,80)
tup[1] #40
tup[1] = 100 #TypeError: 'tuple' object does not support item assignment
tup.count(50) #1 #count(element) will return the no of times that element occured in tuple
tup.index(60) #2 index(element)it will return the index of that element
iteration in tuple is faster than list as values are fixed in tuple

->set = collection of unique element
s = {22,15,14,21,5}
set use the concept of hash so fetching is faster in set
s[2] #Error #indexing is not possible in set

->add below to the PATH to work python commands work in cmd
C:\Users\Shubham\AppData\Local\Programs\Python\Python37-32
->open help
help()
->getting address of a variable
num = 10 #whenever we create a variable a box named num at a particular address will be created with the value 10
id(num) #1702287680 give the address of num variable

in python address will be generated on the basis of data not the variable
a = 10 #this is called tagging. here 10 is tagged by variable a
b = a
in this case a & b points to the same data i.e. 10 so value of id(a) = id(b) = id(10)
so python is memory effiecient as we dont create multiple variable which are having the same values
a = 9 now here address of a will be changed as address of a will be generated on the basis of value which is 9 here
whenever we have data which is not being used or not being tagged by any variable, it will be garbage collected later
#declaring constant variable
we cant declare constant variable
#know the inbuilt type of the variable
type(num) = <class 'int'>
->data types of variables
