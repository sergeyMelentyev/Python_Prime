import timeit       # create new namespace as a container for all obj; execute the code;
import array, math, fractions, random
import timeit as timer      # custom name to refer to a module
from timeit import foo      # load specific definition within a module
from timeit import *        # load all definitions except those that start with an underscore

'''COMPARISON'''
w < x < y < z       # the same as
w < x and x < y and y < z
x == y      # equal value
x is y      # equal obj in memory
z = x if x < y else y       # conditional expression

'''NAMESPACE'''
all_global = globals().keys()       # get all global objects as one dictionary
all_global_one = globals()['string_one']        # get object from global scope
globalVarNameOne = 4
GlobalVarNameTwo = 8
def funcName():
    global globalVarNameOne
    globalVarNameOne = 14       # modify global variable
    GlobalVarNameTwo = 0        # create a new local variable

def countDown(start):
    n = start
    def decrement():        # nonlocal does not bind a name to a local variable
        nonlocal n
        n -= 1

'''BUILD-IN SEQUENCES'''
list, tuple, collections.deque      # container sequences, hold ref to other obj (mix type)
str, bytes, bytearray, memoryview, array.array      # flat sequences, physically store the value (same type)

list, bytearray, array.array, collections.deque, memoryview     # mutable sequences
tuple, str, bytes       # immutable sequences

'''OPERATORS WITH ANY SEQUENCES'''
objOne + objTwo     # concatenation
objOne * n      # makes n copies of objOne
varOne, varTwo, varThree = objOne       # variable unpacking
varOne in objOne        # membership
for x in objOne:        # iteration
all(objOne)     # return True if all items are true
any(objOne)     # return True if any item is true
len(objOne)     # length
min(objOne)     # min/max value in objOne
sum(objOne [,initial])      # summ of items with an optional initial value

'''SLICES'''
n_list[start:stop:step]
n_list[:2]; new_list[2:]      # splits a sequence in two non overlapping parts
n_list = [0, 1, 2, 3, 4]; n_list[1:4] = [20, 30]        # [0, 20, 30, 4]

'''STRING IMMUTABLE OBJECTS'''
string_one = "Python version: {x}.{y}".format(x=3, y=14)
string_two = "Python version: %s" % time.ctime()
stringName.capitalize()     # capitalizes the first character
stringName.count(sub [,start [,end]])       # counts occurences of the specified substring
stringName.startswith(prefix [,start [,end]])       # checks whether a string starts with prefix
stringName.endswith(suffix [,start [,end]])     # checks the end of the string for a suffix
stringName.find(sub [,start [,end]])        # finds the first occurrence of the specified sub
stringName.rfind(sub [,start [,end]])       # finds the last occurrence of a sub
stringName.split([sep [,maxsplit]])     # splits a str using separator as a delimiter
stringName.rsplit(sep, [,maxsplit])     # splits a str from the end using separator
stringName.isalnum()        # whether all chars are alphanumeric
stringName.isalpha()        # whether all chars are alphabetic
stringName.isdigit()        # whether all chars are digits
stringName.join(separator)      # joins the string with a separator
stringName.lower()      # to lower case, to upper case
stringName.replace(oldSub, newSub [,maxreplace])        # replace a substring

'''LIST MUTABLE OBJECT'''       # can hold any data type in one list
del listName[index]     # deletes an element
del listName[indexStart : indexEnd]     # deletes a slice
listName.append(obj)        # add one object to the end
listName.clear()        # delete all items
listName.copy()     # shallow copy
listName.extend(newListName)        # add a new list to the end
listName.count(obj)     # counts occurrences of obj
listName.index(obj [,start [,stop]])        # returns the smallest index of obj
listName.insert(index, obj)     # inserts obj at index
listName.pop([index])       # return elem on index and remove it from the list
listName.remove(obj)        # remove obj
listName.reverse()      # reverses items in place
listName.sort([sortFunc [,reverse]])        # inplace sort list of items (return zero to indicate it)
listName.sorted([,reverse, key])        # sort and create a new list (return new list)

'''ARRAY MUTABLE OBJECT'''      # import array
arr_name.__add__(arr_name_new)      # concatenation
arr_name.__iadd__(arr_name_new)      # in-place += concatenation
arr_name.append(i)      # append after last
arr_name.__contains__(i)        # i in arr_name
arr_name.__copy__()     # copy.copy
arr_name.__deepcopy__()     # copy.deepcopy
arr_name.count(i)       # count occurrences of an element
arr_name.__delitem__(p)     # remove item at position p
arr_name.extend(iter)       # append items from iterable
arr_name.tofile(f)      # save items to binary file f
arr_name.tolist()       # return items as numeric objects in a list
arr_name.__fromfile(f, n)       # append n items from binary file f
arr_name.__getitem__(p)     # get item at position
arr_name.index(e)       # find position of first occurrence of e
arr_name.insert(p, e)       # insert element e before the item at position p
arr_name.itemsize       # length in bytes of each item
arr_name.__len__()      # number of items
arr_name.pop([p])       # remove and return item at position p
arr_name.remove(e)      # remove first occurrence of element e by value
arr_name.reverse()      # reverse the order
arr_name.__setitem(p, e)        # put e in position p, overwriting existing item

floats = array('d', (random() for i in range(10**3)))       # first argument defines the storage type
fp = open('floats.bin', 'wb'); floats.tofile(fp); fp.close()        # floats.fromfile(fp, 10**3)

arr_name = array.array(arr_name.typecode, sorted(arr_name))     # sort an array
bisect.insort(arr_name, new_item)     # inserts new_item into arr_name so as to keep seq in order

'''DEQUE MUTABLE OBJECT'''      # from collections import deque
dq = deque(range(10), maxlen=10)        # good for fast inserting and removinf from both ends
dq.rotate(3); dq.rotate(-4)     # when it is full it descards items from the opposite end

'''DICTIONARY MUTABLE UNORDERED HASH TABLES'''     # key can be any immutable object (string, number, tuple)
dict_name = dict(one=1, two=2, three=3)
dict_name = {'one': 1, 'two': 2, 'three': 3}
dict_name = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
dict_name = dict([('one', 1), ('two', 2), ('three', 3)])
dict_name = dict({'one':1, 'two': 2, 'three': 3})

key in dictName         # returns true if key is here
dictName.keys()     # make a list of all keys/values/items
dectName.__len__()      # number of items
del dictName[key]       # removes item with key from dictName
dictName.clear()        # removes all items
dictName.copy()     # shalow copy
dictName.fromkeys(sequence [,value])        # new dict with keys from sequence and values all set to value
dictName.get(key [,value])      # returns dictName[key], otherwise none
dictName.pop(key [,default])        # returns dictName[key] and removes it from dictName
dictName.update(dictNewName)        # add all obj from dictNewName to dictName
dictName.setdefault(k, [default])       # if k in dictName, return dictName[k], else set dictName[k]

collections.OrderedDict     # dict variation, maintains keys in insertion order
collections.ChainMap        # dict variation, holds a list of mappings that can be searched as one
collections.Counter         # dict variation, mapping that holds an int value for each key
collections.UserDict        # dict variation, pure Python map implementation

'''SET MUTABLE UNORDERED HASH TABLES'''        # unordered collect of unique items optimized for fast membership
setName = {1, 2, 3}     # set literals, use set() empty constructor for set initialization
setName.copy()      # shallow copy
setName.add(setNewName)     # add elements
setName.clear()     # remove all elements
setName.discard(e)      # remove element e from setName
setName.pop()       # remove and return an element from setName
setName.remove(e)       # remove e from setName
setName.difference(setNewName)      # returns all the items in setName but not in setNewName
setName.intersection(setNewName)    # returns all the items that are both in two sets
setName.isdisjoint(setNewName)      # returns true if both have no items in common
setName.issubset(setNewName)        # true if setName is a subset of setNewName
setName.isuperset(setNewName)       # true if setName is a superset of setNewName
setName.symmetric_difference(setNewName)        # return items that are in 1st/2nd set but not in both
setName.union(setNewName)       # return all items in setNewName or setName

'''FROZEN SET IMMUTABLE OBJECTS'''
frozenset(range(10))

'''TUPLE IMMUTABLE OBJECTS'''       # immutable ordered collection and records with no keyes
tuple_one = (1, 1, 2); x, y, z = tuple_one     # tuple unpacking
tuple_count = tuple_one.count(1)        # calc how many times arg take place in tuple
tup = (20, 8); x, y = divmod(*tup)      # prefixing an arg with a star when calling a func
*a, b, c = range(2)     # ([], 0, 1) parallel assignment
*a, b, c = range(5)     # ([0, 1, 2], 3, 4)

ids = [('USA', '311'), ('BRA', 'CE3')]      # unpacking mechanism
for i, _ in sorted(ids): print(i)

'''NAMED TUPLE'''       # from collections import namedtuple
Any_Name = namedtuple('City', 'name country population coordinates')        # class name and list of names
msk = Any_Name('Moscow', 'Russia', 36.93, (35.68, 137.69))
Any_Name._fields        # field names of the class
Any_Name._make(new_data)        # instantiate named tuple from an iterable
msk._asdict()      # returns collections.OrderedDict

'''SEQUENCE ITERATOR''' # vars inside sequences have their own local scope
matrix_one = [[1, 1, 1], [4, 5, 6], [7, 8, 9]]
matrix_two = [(1, 2), (3, 4), (5, 6)]

l_comp_one = [row[0] for row in matrix_one]     # take the first element in each row
l_comp_two = [(letter+'a') for letter in 'Hi']      # what you want + how you call it + where
l_comp_three = [(z+1) for z in range(5) if z % 2 == 0]      # what you want + how you call it + where + if
l_comp_four = [(x,y) for x in listA for y in listB]     # listA[0] with all elements from listB...
l_comp_four = [(x,y) for x in listB for y in listA]     # listB[0] with all elements from listA...

g_express_one = (10 * i for i in matrix_one)        # generator expression yields items one by one
g_express_one.next()

dial_codes = [(86, 'China'), (91, 'India'), (1, 'US')]
d_comp_one = {country: code for code, country in dial_codes}      # dict comprehensions

s_comp_one = {i for i in range(10)}     # set comprehensions

colors = ['black', 'white']; sizes = ['S', 'M', 'L']        # yields items 1 by 1, full list is not produced
for shirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(shirt)

while expression: pass
for x in range(10): pass     # generator function (will not save each value in ram)
for y in matrix_one: pass        # work with any sequence
for (a, b) in matrix_two: pass       # tuple unpacking
for (key, value) in dict_one.items(): pass       # dictionary iteration

for index, value in enumerate(matrix_one):      # iterator that returns sequence of tuples (index, value)
    matrix_one[index] = value * value

for x, y in zip(listOne, listTwo):      # combines two lists into a sequence of tuples
    # (listOne[0], listTwo[0]), (listOne[1], listTwo[1])

for x in matrix_one:        # else will be executed if loop is runs to completion
    if not True:
        break       # else clause is skipped
else:
    raise RuntimeError("Error")

'''GENERATORS'''
# yield = return in order to keep track only on current call

'''FUNCTIONS FIRST CLASS OBJECTS'''
lambda arg_one,arg_two: arg_one + arg_two     # inline anonymous function

def factorial(n): return 1 if n < 2 else n * factorial(n-1); fact = factorial
list(map(fact, range(6)))       # map build-in func
[fact(n) for n in range(6)]     # list comprehension version

list(map(factorial, filter(lambda n: n % 2, range(6))))     # map and filter build-in funcs
[fact(n) for n in range(6) if n % 2]        # list comprehension version

reduce(add, range(100))     # reduce build-in func, apply some operator to the sequence (accumulating)
sum(range(100))     # from operator import add, sum new altarnative to reduce

all(iterable)       # return True if every element is true
any(iterable)       # return True if any element is true

def html_tag(name, *content, cls=None, **attrs):
    if cls is not None: attrs['class'] = cls
    if attrs: attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else: attr_str = ''
    if content: return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else: return '<%s%s />' % (name, attr_str)
html_tag('p')       # single positional argument catched with first arg (name)
html_tag('h3', 'Header', 'New')     # any number of args after the first are catched with *content as tuple
html_tag('h2', 'Header', id=1, src='name.jpg')      # any number of keyword args that are not explicitly named are catched with **arrts as a dict
html_tag('h3', 'Header', 'New', cls='sidebar', id=33)       # cls parameter can only be passed as a keyword arg
my_tag = {'name': 'img', 'title': 'Sunset', 'src': 'sunset.jpg', 'cls': 'framed'}
html_tag(**my_tag)      # prefix dict with ** passes all its items as separate args

def name(text:str, max_len:'int > 0' = 80) -> str:      # each arg with annotation expression preceded by :
    """ annotation goes here"""
    return text

'''CLOSURES'''      # is a func that retains the bindings of the free vars that exist when the func is defined
def make_average():
    series = []
    def average(new_value):     # use nonlocal modifier with immutable types
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return average
avg = make_average()        # make_average has already returned, its local scope is long gone
print(avg(10)); print(avg(11)); print(avg(12))      # series[] is a free var that isnt bound in the local scope

'''CLASSES AND OBJECTS'''       # methods, class variables, computed attributes (properties)
class SampleClass(object):
    species = 'Human'       # class object attribute the same for all instances

    @staticmethod
    def static_method(arg): pass

    @classmethod
    def class_method(cls, arg): pass

    def __init__(self, name, last_name):
        self.__name = name
        self.__last_name = last_name

    @property       # property getter, accessed as instanceName.name
    def name(self):
        return self.__name

    @name.setter        # property setter, accessed as instanceName.name = "new str"
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be a string!")
        self.__name = value

    @name.deleter
    def name(self):
        raise TypeError("Cannot delete name")

    def instance_method(self):
        pass

# create a callable obj that wraps both a method and an associated instance
classInstance = SampleClass("Sergey", "Melentyev")
boundMethod = classInstance.instance_method
boundMethod()

# create a callable obj that wraps the method, but expecs an instance of the propper type to be passed
unboundMethod = SampleClass.instance_method
unboundMethod(classInstance, "Sergey", "Melentyev")

class Sample_Sub_Class(SampleClass):
    def __init__(self, name, last_name, second_name):       # sub class constructor
        SampleClass.__init__(self, name, last_name)     # call super class constructor
        self.second_name = second_name

    def sub_instance_method(self):
        super().instance_method()       # call super class method
        pass

'''DECORATORS'''        # import time execution, before runtime
registry = []
def decorator_func(func_arg):       #run at import time before any other func call
    print('running decorator_func(%s)' % func_arg)
    registry.append(func_arg)
    return func_arg

@decorator_func
def func_one(): print('running func_one()')     # run only if explicitly invoked

'''DECORATOR FACTORY'''
registry = set()
def register(active=True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active: registry.add(func)
        else: registry.discard(func)
        return func
    return decorate

@register(active=False)
def f1(): print('running f1()')
@register()
def f2(): print('running f2()')

'''CONTEXT MANAGER AND WITH'''
items = [1, 2, 3]
class ListTransaction(object):
    def __init__(self, theList):
        self.theList = theList
    def __enter__(self):
        self.workingCopy = list(self.theList)
        return self.workingCopy
    def __exit__(self, type, value, tb):
        if type is None:
            self.theList[:] = self.workingCopy
        return False

with ListTransaction(items) as working:     # will produce [1, 2, 3, 4, 5]
    working.append(4)
    working.append(5)

try:
    with ListTransaction(items) as working:     # will produce [1, 2, 3, 4, 5]
        working.append(6)
        working.append(7)
        raise RuntimeError("Something happened!")
except RuntimeError:
    pass

'''EXCEPTION HANDLING'''
try:
    answer = 2 + 'a'
except TypeError:       # check full list of build-in exceptions
    print("This will be printed in case of TypeError acquire")
else:
    print("This will be printed if no errors acquire")
finally:
    print("This will be printed in any case")

try:
    # catch all exceptions in one place
except Exception as e:
    print("An error: {err}\n".format(err=e))

class MyOwnErrorType(Exception):        # create a custom exception
    def __init__(self, errno, msg):
        self.args = (errno, msg)
        self.errno = errno
        self.errmsg = msg

class HostNameError(MyOwnErrorType): pass
class TimeOutError(MyOwnErrorType): pass
def errorOne(): raise HostNameError("Unknown host")
def errorTwo(): raise TimeOutError("Timed out")
try:
    errorOne()
except MyOwnErrorType as e:
    if type(e) is HostNameError:
        #logic here

class ListTransaction(object):
    def __init__(self, theList):
        self.theList = theList
    def __enter__(self):
        self.workingCopy = list(self.theList)
        return self.workingCopy
    def __exit__(self, type, value, tb):
        if type is None:
            self.theList[:] = self.workingCopy
        return False

'''ALGORITHMS'''        # import bisect
bisect.bisect(seq, item)        # binary search for needle in haystack, must be sorted
def grade(score, breakpoint=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoint, score); return grades[i]      # bisect.bisect return index where to insert
[grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]       # ['F', 'A', 'C', 'C', 'B', 'A', 'A']

bisect.insort(seq, item)     # inserts item into seq so as to keep seq in order

'''C_TYPES'''       # proxy to the C Library
import ctypes
libc = ctypes.CDLL("/usr/lib/libc.dylib")
libc.rand()
libc.atoi("1234")

'''CONCURRENCY'''
import multiprocessing
import time

def clock(interval):
    while True:
        print("Function. The time is %s" % time.ctime())
        time.sleep(interval)

p = multiprocessing.Process(target=clock, args=(5,))
p.start()

class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval
    def run(self):
        while True:
            print("Class. The time is %s" % time.ctime())
            time.sleep(self.interval)
cp = ClockProcess(5)
cp.start()

def consumer(input_q):
    while True:
        item = input_q.get()
        if item is None: break
        print(item)
    print("Consumer done")

def producer(sequence_current, output_q):
    for item in sequence_current: output_q.put(item)

q = multiprocessing.Queue()
cons_p = multiprocessing.Process(target=consumer, args=(q,))
cons_p.start()
sequence = [1, 2, 3, 4, 5]
producer(sequence, q)
q.put(None)
cons_p.join()







'''ALGORITHMS MIT'''
# insertion sort (алгоритм сортировки вставкой) for small amount of data

# check speed of a function
timer = timeit.timeit("'-'.join(str(n) for n in range(100))", number=1000)

'''DESIGN PATTERNS'''
from abc import ABCMeta, abstractmethod
from collections import namedtuple
Customer = namedtuple('Customer', 'name fidelity')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    def total(self): return self.price * self.quantity

class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
    def total(self):
        if not hasattr(self, '__total'): self.__total = sum(item.total() for item in self.cart)
        return self.__total
    def due(self):
        if self.promotion is None: discount = 0
        else: discount = self.promotion.discount(self)
        return self.total() - discount
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

class Promotion(metaclass=ABCMeta):
    @abstractmethod
    def discount(self, order): """Return discount as a positive dollar amount"""

class FidelityPromo(Promotion):
    """5% discount for customer with 1000 or more fidelity points"""
    def discount(self, order): return order.total() * .05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo(Promotion):
    """10% discount for each LineItem with 20 or more units"""
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20: discount += item.total() * .1
        return discount

class LargeOrderPromo(Promotion):
    """7% discount for order with 10 or more distinct items"""
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10: return order.total() * .07
        return 0

joe = Customer('John Doe', 0); ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('mellon', 5, 5.0)]
Order(joe, cart, FidelityPromo()); Order(ann, cart, FidelityPromo())
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
Order(joe, long_order, LargeOrderPromo()); Order(ann, long_order, LargeOrderPromo())
