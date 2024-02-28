"""Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]),
write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4])"""


start_list = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
new_list = [x for y in start_list for x in y]



#print(new_list)


