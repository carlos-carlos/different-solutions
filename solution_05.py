'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

#empty sorted_list shall be set to the sorted() version of unsorted_list
#the key to sort the items by shall be set to the lambda value
# the lambda value represents the relationship between the items within the list, and the tuples within it
# x (unsorted_list : x(the tuples) [1](index one of the tuples

sorted_list = sorted(unsorted_list, key=lambda x: x[1])
print(sorted_list)

# for me this one was by far the easiest to understand and follow because of the simplicity
# even though we have not covered lambdas yet I can surmise from the code
# that the lambda somehow points to the relationship of the items within the list and the tuples
# setting it as the key value in sorted() tells sorted() to order the list
# in ascending order based on the values in that specific relationship
