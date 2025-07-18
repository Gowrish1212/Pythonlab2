numbers = []
print("Enter 5 integers:")
for i in range(5):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)


print("\nFirst element:", numbers[0])
print("Last element:", numbers[-1])


print("\nAll elements in the list:")
for num in numbers:
    print(num, end=' ')
print()


numbers.reverse()
print("\nReversed list:")
for num in numbers:
    print(num, end=' ')
print()
