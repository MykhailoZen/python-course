fruits = ("Apple", "Apricot", "Apple", "Apricot", "Lemon", "Apple", "Apricot", "Lemon", "Avocado", "Banana")
dict_counts = {}
for fruit in fruits:
    dict_counts.update({fruit: 1}) if fruit not in dict_counts.keys() \
        else dict_counts.update({fruit: dict_counts[fruit] + 1})
print(dict_counts)
