# take the unsorted_list and sort() it based on the relationship between the items in the list and the tuple[1]
# as the determining factor for the ascending order

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]

unsorted_list.sort(key=lambda x: x[1])
print(unsorted_list)

# the first thing that came to my head when I saw this problem is using sorted() or sort()
# and storing that in a variable called sorted list.
# turns out its not that simple and I just got an empty list

# I also wondered if there was someway to use to split() method on the list and the tuples inside and then sort() them
# this would be too complicated because it would make one big list of everything
# You would then somehow need to re-establish the relationships between the items originally in tuples

# since the previous solution already used sorted() i figured i'd add one using sort()
# of all the solutions I came across this one was the simplest to understand for me

# sort() alters the original unsorted_list
# sorted() does not alter the original list, it returns a new one
