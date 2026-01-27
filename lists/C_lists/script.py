# Write a function `lengthiest_word(sentence)` that accepts a string containing a sentence.
# The function should return the longest word in the sentence.
# If there is a tie, return the word that appears later in the sentence.

def lengthiest_word(sentence):
    words = sentence.split()
    longest_term = words[0]
    for word in words:
        if len(word) > len(longest_term):
            longest_term = word
        elif len(word) == len(longest_term):
            longest_term = word
    print(longest_term)
   

# Example:
lengthiest_word("I am pretty hungry") #-> 'hungry'
lengthiest_word("we should think outside of the box") #-> 'outside'
lengthiest_word("down the rabbit hole") #-> 'rabbit'
lengthiest_word("simmer down") #-> 'simmer'



# Write a function `alternating_caps(sentence)` that accepts a string containing a sentence.
# The function should return the sentence where words alternate between lowercase and uppercase.
def alternating_caps(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if i%2==0:
            words[i]= words[i].lower()
        else:
            words[i] = words[i].upper()
    print(" ".join(words))
    
# Example:
alternating_caps("take them to school") #-> 'take THEM to SCHOOL'
alternating_caps("What did ThEy EAT before?") #-> 'what DID they EAT before?'

# Write a function `number_range(min_val, max_val, step)` that accepts three numbers as arguments.
# The function should return a list of numbers starting from min_val to max_val (inclusive),
# incremented by step.

def number_range(min_val,max_val,step):
    new_list = []
    count = min_val
    while count <= max_val:
        new_list.append(count)
        count += step
    print(new_list)

# Example:
number_range(10, 40, 5) #-> [10, 15, 20, 25, 30, 35, 40]
number_range(14, 24, 3) #-> [14, 17, 20, 23]
number_range(8, 35, 6) #-> [8, 14, 20, 26, 32]

# Write a function `remove_short_words(sentence)` that accepts a string containing a sentence.
# The function should return a new sentence where all words shorter than 4 characters are removed.
def remove_short_words(sentence):
    words = sentence.split()
    for i in range(len(words)-1,-1,-1):
        if len(words[i]) < 4:
            del words[i]
    print(" ".join(words))


# Example:
remove_short_words("knock on the door will you") #-> 'knock door will'
remove_short_words("a terrible plan") #-> 'terrible plan'
remove_short_words("run faster that way") #-> 'faster that'





# Write a function `common_elements(arr1, arr2)` that accepts two lists as arguments.
# The function should return a new list containing the elements that are found in both input lists.
# The order of elements in the output list doesn't matter.
def common_elements(arr1,arr2):
    new_list = [word for word in arr1 if word in arr2]
    print(new_list)

# Example:
common_elements(["a", "c", "d", "b"], ["b", "a", "y"]) #-> ['a', 'b']
common_elements([4, 7], [32, 7, 1, 4]) #-> [4, 7]

