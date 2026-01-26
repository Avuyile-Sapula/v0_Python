# Write a function `make_acronym(sentence)` that accepts a string containing a sentence.
# The function should return a string containing the first character of each word in the sentence.

def make_acronym(sentence):
    acc = ""
    for word in sentence.split():
        acc += word[0].upper()
    print(acc)
        


# Example:
make_acronym("New York") #-> 'NY'
make_acronym("same stuff different day") #-> 'SSDD'
make_acronym("Laugh out loud") #-> 'LOL'
make_acronym("don't over think stuff") #-> 'DOTS'

# Write a function `reverse_array(arr)` that accepts a list as an argument.
# The function should return a list containing the elements of the original list in reverse order.

def reverse_array(arr):
    new_arr = []
    for i in range(len(arr)-1,-1,-1):
        new_arr.append(arr[i])
    print(new_arr)

# Example:
reverse_array(["zero", "one", "two", "three"]) #-> ['three', 'two', 'one', 'zero']
reverse_array([7, 1, 8]) #-> [8, 1, 7]



# Write a function `your_average_function(numbers)` that accepts a list of numbers.
# The function should return the average of all elements in the list.
# If the list is empty, the function should return None.

def your_average_function(numbers):
    ans = 0
    lens = len(numbers)
    for i in numbers:
        ans += i
    if lens == 0:
        print("divison by 0")
    else:
        print(ans/lens)
    
   

# Example:
your_average_function([5, 2, 7, 24]) #-> 9.5
your_average_function([100, 6]) #-> 53
your_average_function([31, 32, 40, 12, 33]) #-> 29.6
your_average_function([]) #-> None



# Write a function `choose_divisibles(numbers, target)` that accepts a list of numbers and a target number.
# The function should return a new list containing only the elements divisible by the target.
def choose_divisibles(numbers,target):
    new_arr = []
    for i in numbers:
        if i%target == 0:
            new_arr.append(i)
    print(new_arr)


# Example:
choose_divisibles([40, 7, 22, 20, 24], 4) #-> [40, 20, 24]
choose_divisibles([9, 33, 8, 17], 3) #-> [9, 33]
choose_divisibles([4, 25, 1000], 10) #-> [1000]




# Write a function `maximum(numbers)` that accepts a list of numbers.
# The function should return the largest number in the list.
# If the list is empty, return None.

def maximum(numbers):
    if len(numbers) == 0: 
        print("None")
    else:
        max_num = numbers[0]
        for i in numbers:
            if i > max_num:
                max_num = i
        print(max_num)


# Example:
maximum([5, 6, 3, 7]) #-> 7
maximum([17, 15, 19, 11, 2]) #-> 19
maximum([]) #-> None


# Write a function `word_count(sentence, target_words)` that accepts a sentence string and a list of target words.
# The function should return a count of how many words in the sentence are also in target_words.
def word_count(sentence,target_words):
    words = sentence.split()
    count = 0 
    for word in words:
        if word in target_words:
            count += 1
    print(count)
    
# Example:
word_count("open the window please", ["please", "open", "sorry"]) #-> 2
word_count("drive to the cinema", ["the", "driver"]) #-> 1
word_count("can I have that can", ["can", "I"]) #-> 3
