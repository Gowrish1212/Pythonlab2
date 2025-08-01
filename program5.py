def count_and_remove_duplicates(lst):
   
    count_dict = {}

  
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1


    print("Element occurrences:")
    for item, count in count_dict.items():
        print(f"{item}: {count}")

   
    unique_elements = list(count_dict.keys())

    print("\nList after removing duplicates:")
    print(unique_elements)


my_list = [4, 2, 7, 4, 2, 4, 5, 7, 1]
count_and_remove_duplicates(my_list)
