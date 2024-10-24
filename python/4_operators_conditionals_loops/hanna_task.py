number_list = [7, 0, -1, -3, 5]

new_list = []

for x in number_list:
    if x > 0 and x != 7:
        new_list.append(x)

print(f"There is new list: {len(new_list)}")
