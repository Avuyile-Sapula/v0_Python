# Write a function `total(numbers)` that accepts a list of numbers as an argument.
# The function should return the sum of all elements in the list.
def total(numbers):
    sum = 0
    for num in numbers:
        sum += num
    print(sum)

# Example:
total([3, 2, 8]) #-> 13
total([-5, 7, 4, 6]) #-> 12
total([7]) #-> 7
total([]) #-> 0

# Write a function `stay_positive(numbers)` that accepts a list of numbers.
# The function should return a new list containing only the positive numbers.
def stay_positive(numbers):
    new_list = []
    for num in numbers:
        if num > 0:
            new_list.append(num)
    print(new_list)
# Example:
stay_positive([10, -4, 3, 6]) #-> [10, 3, 6]
stay_positive([-5, 11, -40, 30.3, -2]) #-> [11, 30.3]
stay_positive([-11, -30]) #-> []

# Write a function `bleep_vowels(text)` that accepts a string and returns
# a new string where all vowels (a, e, i, o, u) are replaced with '*'.
def bleep_vowels(text):
    new_text = ''
    for char in text:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            new_text += '*'
        else:
            new_text += char
    print(new_text)

# Example:
bleep_vowels("skateboard") #-> 'sk*t*b**rd'
bleep_vowels("slipper") #-> 'sl*pp*r'
bleep_vowels("range") #-> 'r*ng*'
bleep_vowels("brisk morning") #-> 'br*sk m*rn*ng'

# Write a function `filter_long_words(words)` that accepts a list of strings.
# The function should return a new list containing only the words that have
# less than 5 characters.
def filter_long_words(words):
    new_list = []
    for word in words:
        if len(word) < 5:
            new_list.append(word)
    print(new_list)

# Example:
filter_long_words(["kale", "cat", "retro", "axe", "heirloom"]) #-> ['kale', 'cat', 'axe']
filter_long_words(["disrupt", "pour", "trade", "pic"]) #-> ['pour', 'pic']


# Write a function `num_odds(numbers)` that accepts a list of numbers.
# The function should return the count of odd numbers in the list.
def num_odds(numbers):
    odd_nums = 0
    for num in numbers:
        if num%2 !=0:
            odd_nums +=1
    print(odd_nums)

# Example:
num_odds([4, 7, 2, 5, 9]) #-> 3
num_odds([11, 31, 58, 99, 21, 60]) #-> 4
num_odds([100, 40, 4]) #-> 0


# Write a function `strings_to_lengths(strings)` that accepts a list of strings.
# The function should return a new list containing the lengths of each string.

def strings_to_lengths(strings):
    nums = []
    for str in strings:
        word_len = len(str)
        nums.append(word_len)
    print(nums)

# Example:
strings_to_lengths(["belly", "echo", "irony", "pickled"]) #-> [5, 4, 5, 7]
strings_to_lengths(["on", "off", "handmade"]) #-> [2, 3, 8]



# Write a function `divisors(num)` that accepts a number.
# The function should return a list containing all positive numbers that divide num exactly.

def divisors(num):
    nums = []
    for i in range(1,num+1):
        if num % i == 0:
            nums.append(i)
    print(nums)

# Example:
divisors(15) #-> [1, 3, 5, 15]
divisors(7) #-> [1, 7]
divisors(24) #-> [1, 2, 3, 4, 6, 8, 12, 24]

