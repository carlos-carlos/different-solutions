'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''
#driver code and empty list for the desired results
unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

#for each item in the unsorted_list for the whole list
#set to 'min' to value of list index 0 tuple index 1
for x in range(0, len(unsorted_list)):

    min = unsorted_list[0][1]
    print(min)
    index = 0

    #for each item in unsorted_list for the whole list
    # if index 1 of each item in unsorted_list is less than the value of 'min'
    # min should equal the value of index 1 of each item in unsorted_list
    # 'index' shall equal each item in the unsorted list
    for i in range(0, len(unsorted_list)):
        if unsorted_list[i][1] < min:
            min = unsorted_list[i][1]
            index = i

    # add to sorted_list each index from unsorted_list
    sorted_list.append(unsorted_list[index])

    #remove each index from unsorted_list
    unsorted_list.remove(unsorted_list[index])


print(unsorted_list)
print(sorted_list)

# this is super confusing to me. I'm not exactly sure what is going on starting from 'min'
# especially confused by the unsorted_list[0][1] bit and the use of range(). Why not use just len()?
# I lost track of how the end connects to index which is set to zero
