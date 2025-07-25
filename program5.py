from collections import Counter


my_list = [1, 2, 2, 3, 4, 4, 4, 5]


counts = Counter(my_list)


unique_list = list(dict.fromkeys(my_list))


print("Element counts:")
for element, count in counts.items():
    print(f"{element}: {count}")


print("\nList without duplicates:")
print(unique_list)
