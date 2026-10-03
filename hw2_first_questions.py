# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.
#

def triple(x):
    triple_x = x*3
    return triple_x

print(triple(4))

# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
#

def subtract(x,y):
    subtract_two = x-y
    return subtract_two

print(subtract(5,3))

# 3)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.


def dictionary_maker(tuple_list):
    new_dict = {}
    for key, value in tuple_list:
        new_dict[key] = value

    return new_dict

print(dictionary_maker([('foo', 1), ('bar', 3), ('hi', 5)]))


#
# For example, if given: [('foo', 1), ('bar', 3), ('hi', 5)]
# it should return {'foo': 1, 'bar': 3, 'hi': 5}
# You should program the function and not use
# the function "dict" directly