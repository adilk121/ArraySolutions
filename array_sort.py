my_array = [64, 25, 12, 22, 11]

# Bubble sort algorithm
for i in range(len(my_array)):
    for j in range(len(my_array)-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print(my_array)  # Output: [11, 12, 22, 25, 64]
