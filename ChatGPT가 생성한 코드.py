#chatGPT

# List
my_list = [1, 2, 3, 4, 5]
print("List:")
print("Original List:", my_list)
my_list.append(6)
my_list[1] = 10
del my_list[2]
print("Modified List:", my_list)
print()

# Tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:")
print("Original Tuple:", my_tuple)
# Tuples are immutable, so you can't append or modify directly
# You can create a new tuple with modifications
new_tuple = my_tuple + (6,)
print("Modified Tuple:", new_tuple)
print()

# Set
my_set = {1, 2, 3, 4, 5}
print("Set:")
print("Original Set:", my_set)
my_set.add(6)
my_set.remove(2)
print("Modified Set:", my_set)
print()

# Dict
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Dictionary:")
print("Original Dictionary:", my_dict)
my_dict['d'] = 4
del my_dict['b']
print("Modified Dictionary:", my_dict)