'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

# for each item in the unsorted_list
# current_min shall equal the index 1 or item 0 of unsorted_list
# Index is set to zero
for tup in list(unsorted_list):

    current_min = unsorted_list[0][1]
    index = 0

    # for each item in unsorted_list
        # if index 1 of each item is less than the present value of current_min
            # current_min shall be set to the value of each item in unsorted_list index 1
            # set index to the value of each item in unsorted_list
    for i in range(0, len(unsorted_list)):
        if unsorted_list[i][1] < current_min:
            current_min = unsorted_list[i][1]
            index = i

    #add each item in index to the sorted list
    #remove them from the unsorted list
    sorted_list.append(unsorted_list[index])
    unsorted_list.remove(unsorted_list[index])

print(unsorted_list)
print(sorted_list)

#This is a somehwat simpler version of the previous solutions
# its still hard for me to follow what exactly is going
#though i think i understood this one the best of all so far