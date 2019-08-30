'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''
# driver code to be acted upon
unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]

# empty list that will contain sorted elements
sorted_list = []

# empty list to store the just the values in the tuples
value_list = []

#for each item (tuple) in unsorted list
# append that item at index '1' of the tuple to value_list
for tuple_ in unsorted_list:
    value_list.append(tuple_[1])

print(value_list)

# sorts value_list items in ascending order
value_list.sort()

# iterate through items in value_list
for value in value_list:

    # nested loop to iterate through the remaining items in the unsorted_list
    for tuple_ in unsorted_list:

        # conditional statement, compares the element in unsorted_list with the element in value_list
        # add to sorted_list if tuple_ and value are the same for each time that they are
        # then remove it from unsorted_list
        # then stop when you're done

        if tuple_[1] == value:
            sorted_list.append(tuple_)
            unsorted_list.remove(tuple_)
            break

print(sorted_list)

# I really don't understand how the last block of code starting with 'if' works