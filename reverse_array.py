my_array = [1, 2, 3, 4, 5]
# Find the length of the array
n = len(my_array)
# Loop through the first half of the array
for i in range(n // 2):
    # Swap the i-th element from the beginning
    my_array[i], my_array[n - i - 1] = my_array[n - i - 1], my_array[i]    
    # with the i-th element from the end
print(my_array)  # Output: [5, 4, 3, 2, 1]