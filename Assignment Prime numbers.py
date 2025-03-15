# Even Numbers, odd numbers from the given List
# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]


even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Printing the results
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)

# To Find out the prime number and to form a prime number list
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

    # # Given list
    # # numbers = [10, 501, 22, 37, 100, 999, 87, 351]
# #
# # # Creating a list of prime numbers
prime_numbers = [num for num in numbers if is_prime(num)]
# #
# Counting the prime numbers
prime_count = len(prime_numbers)
# #
# # # Printing results
print("Prime Numbers:", prime_numbers)
print("Total Count of Prime Numbers:", prime_count)

# To find the list of happy numbers from the given list

def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1
#
# # Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
#
# # Finding happy numbers
happy_numbers = [num for num in numbers if is_happy(num)]
#
print("Happy Numbers:", happy_numbers)

# To find the sum of first and last numbers of a list
def sum_first_last(n):
    n = abs(n)  # Handle negative numbers
    num_str = str(n)
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    return first_digit + last_digit
#
# # Example usage
num = int(input("Enter an integer: "))
print("Sum of first and last digit:", sum_first_last(num))

#python program to find all the ways to make rupees 10 using rupees 1, rupees 2, rupees 5 and rupees 10 coins
#
def find_combinations(target, coins, combination=[], index=0):
    if target == 0:
        print(combination)
        return
    if target < 0 or index >= len(coins):
        return

    # # Include the current coin
    find_combinations(target - coins[index], coins, combination + [coins[index]], index)
    #
    # # Exclude the current coin and move to the next
    find_combinations(target, coins, combination, index + 1)


# Given coins
coins = [10, 5, 2, 1]
#
# print("Ways to make ₹10 using ₹1, ₹2, ₹5, and ₹10 coins:")
find_combinations(10, coins)

#Python Program to find the first non repeating elements in a given list of integers
def first_non_repeating(lst):
    count = {}  # Dictionary to store frequency of each element

    # Count occurrences of each element
    for num in lst:
        count[num] = count.get(num, 0) + 1

    # Find the first element with count 1
    for num in lst:
        if count[num] == 1:
            return num

    return None  # If no non-repeating element is found

numbers = [4, 5, 1, 2, 0, 4, 5, 1, 2]
result = first_non_repeating(numbers)
print("First non-repeating element:", result)

#write a python program to find the first non repeating elements in a given list of integers

def first_non_repeating(lst):
    frequency = {}

    # Count occurrences of each element
    for num in lst:
        frequency[num] = frequency.get(num, 0) + 1

    # Find the first element with frequency 1
    for num in lst:
        if frequency[num] == 1:
            return num

    return None  # Return None if no non-repeating element is found

numbers = [4, 5, 1, 2, 0, 4, 5, 1, 2]
result = first_non_repeating(numbers)
print("First non-repeating element:", result)

#Triplet number

def find_triplet(arr, target):
    n = len(arr)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    return arr[i], arr[j], arr[k]
    return None

arr = [10, 20, 30, 9]
target = 59

triplet = find_triplet(arr, target)
if triplet:
    print("Triplet found:", triplet)
else:
    print("No triplet found")

# Sum Sblist is equals to zero
def find_sublist_with_zero_sum(arr):
    n = len(arr)
    for i in range(n):
        sum_so_far = 0
        for j in range(i, n):
            sum_so_far += arr[j]
            if sum_so_far == 0:
                return arr[i:j+1]
    return None

arr = [4, 2, -3, 1, 6]

sublist = find_sublist_with_zero_sum(arr)
if sublist:
    print("Sublist with sum zero found:", sublist)
else:
    print("No sublist with sum zero found")




