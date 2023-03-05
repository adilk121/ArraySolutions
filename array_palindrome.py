def is_palindrome(arr):
    """
    Check if an array is a palindrome
    """
    n = len(arr)
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            return False
    return True

# Example usage
arr1 = [1, 2, 3, 4, 3, 2, 1]
arr2 = [1, 2, 3, 4, 5, 6, 7]
print(is_palindrome(arr1))  # Output: True
print(is_palindrome(arr2))  # Output: False
