#Personal practical Python learning reference 
#based on                   https://www.learnpython.org/
#Details about Slice        https://stackoverflow.com/questions/509211/understanding-slice-notation
#Pandas addtional info      https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
#List Comprehension         https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
#Iterators and generators   https://hackaday.com/2018/09/19/learn-to-loop-the-python-way-iterators-and-generators-explained/

#More resources to check    https://www.python.org/about/gettingstarted/
#                           https://pl.python.org
#                           https://data-flair.training/blogs/python-best-practices/
#                           https://www.flynerd.pl/2018/06/500-zadan-w-pythonie-i-kazdym-innym-jezyku.html

#Basics      ------------------------------------------------------------------------------------------------
#Numerical types
intNum    = 965      #integer
floatNum  = float(1) #float
floatNum += 2.0      #float also
                     #Python also suports complex numbers

#Text type
text  = 'Use "double quotes" inside single ones'
text2 = "And 'vice versa'"
print(text2 * 4)                #Python supports string and list multiplication
print(r'C:\Print directory\Without escaping\by using raw strings\preced string literal with r ')
print('Hex value of %d is %x (uppercase %X)' % (intNum, intNum, intNum))
soughtcharacter='o'
print('First occurence of %s in variable text (%s) is at character %d.' 
       %(soughtcharacter, text, text.index(soughtcharacter)))
print('%s occurs in there %d times' %(soughtcharacter, text.count(soughtcharacter)))
start, stop, step = 4, 20, 1    #Slicing, stop is first value NOT in slice
print('substring of from character %d to character %d: %s' % (start, stop, text[start:stop]))
print('To reverse string just specify indexes as [::-1]: %s' %text[::-1])

#Collections
mylist = [1,2,3]     #list, zero-indexed
mylist.append(4)
print("mylist %s contains %d objects." % (mylist, len(mylist))) #String substitution ? (self explained)
print('mylist[1] ** mylist[2] = %d' % mylist[1]**mylist[2])    # ** is power poerator

if 1 in mylist:                 #in operator, returns true if values is present in iterable variable
    print('mylist contains 1')  #Python uses idnentation for blocks, standard is four spaces
else: 
    print('mylist does not contain 1')

if 1 is mylist:                 #is operator, compares if instances point to the same objects
    print('mylist IS the same instance as 1')
else:
    print('mylist is %d , 1 is %d. They are not the same instance.' %(id(mylist), id(1)))

dictionary = {}
dictionary["Element #0"]=0    #key-value pairs
dictionary["Element #1"]=1
dictionary["Element #2"]=2
dictionary2 = {
    "Element #0" : 0,
    "Element #1" : 1,
    "Element #3" : 2
}

for name, value in dictionary.items():
    print("%s has value %d" %(name, value))

del dictionary["Element #1"]
dictionary.pop("Element #2")

print("Type of dictionary variable is %s" %type(dictionary))


#Operations
pass                                #pass is null operation - doing nothing

numbers=[4,1,0,3,2] 
for number in sorted(numbers):      #sorted function sorts collections
    if 0==number:
        print('For loop, iteration %d.' % number)
        continue                    #early loop termination
    if 0==number % 2:
        print('For loop, iteration %d. Even' % number)
    else:
        print('For loop, iteration %d. Odd' % number)

for number in range(2,5):           #range returns collection, xrange returns iterator which is more efficient
    print('Ranged for loop, object %d' % numbers[number])
else:
    print('You can use else clause in Python loops!')

iteration=1
while True:
    if iteration == 3:
        print('We have ran 3rd time')
        iteration+=1
        continue
    print('While loop, iteration #', iteration)
    iteration+=1
    if iteration >= 5:
        break
else:
    print("This won't be printed because of brak command")

def function(answer):
    return('does this work? %s' %answer)

print(function('Yes it does'))

#Classses and objects
def Classes_and_objects():
    class MyClass():
        mymember="Look ma i'm a member!"

        def attribute(self):
            print(self.mymember)

    MyObject=MyClass()
    MyClass.attribute(MyObject)

Classes_and_objects()


#Modules & packages
#Modules are just other files, name of a file is the name of module
#Packages are namespaces which contain modules
#They are simply directories, that HAVE to contain file named __init__.py, It can be empty. #regular package Python <= 3.3
#__all__=["Module name"]            #__init__.py decides what modules are exported as API, while other are kept internal 
import urllib.response              #importing package.module
                                    #python compiles files as .pyc format so it would not have to parse file on each call
                                    #at first import modules are ran once to initialize them
                                    #so local variables in modules act as singletons
#import function as alias           #you can alias imported fucntion - very useful!
from urllib import request          #import function directly into module namespace, * to import all
                                    #in case of name collision imported name overwrites local
urllib.request.urlopen("https://www.hackaday.com")  #calling function from imported module
#dir(urllib)                        #Useful to list all the functions of module, used in Python terminal
#help(urllib.request.urlopen)       #get info about function
                                    
#PYTHONPATH = /foo python Module.py #Extending module load path - 1st way  
#sys.path.append("/foo")            #Extending module load path - 2nd way


#if this script is executed main() is executed
#if __name__='__main__':
#    main()


#DataScience ------------------------------------------------------------------------------------------------
#NumpyArray
#import numpy
#Create 2 numpy arrays from height and weight
#np_height = numpy.array([1.87,  1.87, 1.82, 1.91, 1.90, 1.85])
#np_weight = numpy.array([81.65, 97.52, 95.25, 92.98, 86.18, 88.45])
#bmi = np_weight / np_height ** 2           #Calculate bmi for all elements at once
#bmi[bmi > 23]                              #print only elements that match criteria

#PandaBasics                        https://www.learnpython.org/en/Pandas_Basics
#import pandas
#dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
#       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
#       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
#       "population": [200.4, 143.5, 1252, 1357, 52.98] }
#brics = pandas.DataFrame(dict)
#print(brics)
#brics.index = ["BR", "RU", "IN", "CH", "SA"]
#print(brics)
#cars = panda.read_csv('cars.csv', index_col = 0) #you can import directly from CSV file
#print(cars)
#print(cars['cars_per_cap'])                #Print out country column as Pandas Series
#print(cars[['cars_per_cap']])              #Print out country column as Pandas DataFrame
#print(cars[['cars_per_cap', 'country']])   #Print out DataFrame with country and drives_right columns
#print(cars[4:6])                           #Print out fifth and sixth observation
#print(cars.iloc[2])                        #Select data based on row number
#print(cars.loc[['AUS', 'EG']])             #Select data by label or condition



#Advanced    ------------------------------------------------------------------------------------------------
#Generators
import types
def fibonacci_generator(arg1, arg2, *otherargs):    #variable amount of arguments
    def fib():                  #Generators are functions returning (yielding) sets that you can iterate over
        a, b = 1, 1
        while a<100:
            yield a
            a, b = b, a + b
    
    if type(fib()) == types.GeneratorType:
        print("Good, The fib function is a generator.")

    for num in fib():
        print(num)

    print('Argument #1: %s' %arg1)
    print('Argument #2: %s' %arg2)
    print('Argument #3: %s' %list(otherargs))   #dealing with additional arguments
fibonacci_generator("One", "Two", "Three", "Four", "Five")

#List comprehension
#new_list = [expression(i) for i in old_list if filter(i)]
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)

