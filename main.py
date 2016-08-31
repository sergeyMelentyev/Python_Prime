string_one = "Python version: {x}.{y}".format(x=3, y=14)


'''DICTIONARY OBJECT'''
dict_one = {'k1': 1, 'k2': 2, 'k3': 3}
dict_all_keys = dict_one.keys()                                     # make a list of all keys/values/items


'''SET OBJECT'''
set_one = {1, 2, 3}                                                 # unordered collection of unique items


'''TUPLE OBJECT'''
tuple_one = (1, 1, 2, 3)                                            # immutable ordered collection
tuple_count = tuple_one.count(1)                                    # calc how many times arg take place in tuple


'''SEQUENCE ITERATOR'''
matrix_one = [[1, 1, 1], [4, 5, 6], [7, 8, 9]]
matrix_two = [(1, 2), (3, 4), (5, 6)]

l_comprehension_one = [row[0] for row in matrix_one]                # take the first element in each row
l_comprehension_two = [(letter+'a') for letter in 'Hi']             # what you want + how you call it + where
l_comprehension_three = [(z+1) for z in range(5) if z % 2 == 0]     # what you want + how you call it + where + if

for x in range(10):                                                 # generator function (will not save values in ram)
    pass

for y in matrix_one:                                                # work with any sequence
    pass

for (a, b) in matrix_two:                                           # tuple unpacking
    pass

for (key, value) in dict_one.items():                               # dictionary iteration
    pass


'''SCOPE'''
variable_name = 'any_global_variable_name'                          # use global keyword in order to mark var as global
all_global = globals().keys()                                       # get all global objects as one dictionary
all_global_one = globals()['string_one']                            # get object from global scope


'''CLASSES AND OBJECTS'''
class Sample_Class(object):
    species = 'Human'                                               # class object attribute (the same for all objects)

    def __init__(self, name, last_name):                            # object constructor
        self.name = name
        self.last_name = last_name

    def method_print(self):
        print(self.name, ' + ', self.last_name, ' + ', Sample_Class.species)


class Sample_Sub_Class(Sample_Class):
    def __init__(self, name, last_name, second_name):               # sub class constructor
        Sample_Class.__init__(self, name, last_name)                # call super class constructor
        self.second_name = second_name

    def sub_method_print(self):
        print(self.name, ' + ', self.last_name, ' + ', Sample_Class.species, ' + ', self.second_name)


'''EXCEPTION HANDLING'''
try:
    answer = 2 + 'a'
except TypeError:                                                   # check full list of build-in exceptions
    print("This will be printed in case of TypeError acquire")
else:
    print("This will be printed if no errors acquire")
finally:
    print("This will be printed in any case")


'''BUILD-IN FUNCTIONS'''
# map() apply a func to every item in a list, return a list of all items
sample_list = [0, 22.5, 40, 100]
mapped_lambda = list(map(lambda arg: (9.0/5*arg + 32), sample_list))

def sample_function(arg): return (9.0/5)*arg + 32
mapped_list = list(map(sample_function, sample_list))

# reduce() apply a func to every item in a list in pare of two, return only one final item
# filter() apply a func that return a bool to the list in pare of two, return only one final item
# zip() combine items at each index in a tuple from two lists
# all() return True if all elements are true
# any() return True if any element is true


'''DECORATORS'''
def decorator_func(func):
    def insider_func():                                             # add logic before and after decorated func call
        print('Code here, before executing the func')
        func()
        print('Code here will execute after all')
    return insider_func

@decorator_func
def need_a_decorator():
    print('This function needs a decorator')


'''ITERATORS GENERATORS'''
# yield == return in order to keep track only on current call


'''STANDARD MODULES'''
# from collections import Counter                                   # count every item in a list and create a dict
# from collections import OrderedDict                               # dict that save the order of key/value pare
# from collections import namedtuple                                # the same as class constructor
