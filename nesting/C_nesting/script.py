# Write a function `remove_dupes(lst)` that accepts a list and returns a new list
# where each element appears only once.
def remove_dupes(lst):
    new_list = []
    for el in lst:
        if el not in new_list:
            new_list.append(el)
    return new_list

# Example usage:
print(remove_dupes(["x", "y", "y", "x", "z"]))  # ['x', 'y', 'z']
print(remove_dupes([False, False, True, False]))  # [False, True]
print(remove_dupes([42, 5, 7, 42, 7, 3, 7, 7]))  # [42, 5, 7, 3]

# Write a function `remove_vowels(s)` that accepts a string and returns a new string
# with all vowels removed (a, e, i, o, u).
def remove_vowels(s):
    new_str = ""
    for i in range(len(s)):
        if s[i] not in "aeiou":
            new_str += s[i]
    return new_str


# Example usage:
print(remove_vowels("jello"))  # 'jll'
print(remove_vowels("sensitivity"))  # 'snstvty'
print(remove_vowels("cellar door"))  # 'cllr dr'


# Write a function `spam(pairs)` that accepts a 2D list. Each inner list contains
# a word and a number. The function returns a string with each word repeated
# the specified number of times, separated by spaces.
def spam(pairs):
    result = ""
    for pair in pairs:
        word = pair[0]
        count = pair[1]
        for _ in range(count): 
            result += word + " "
    
    return result.strip()

# Example usage:
array1 = [["hi", 3], ["bye", 2]]
print(spam(array1))  # 'hi hi hi bye bye'

array2 = [["cat", 1], ["dog", 2], ["bird", 4]]
print(spam(array2))  # 'cat dog dog bird bird bird bird'

# Write a function `remove_first_vowel(s)` that accepts a string and returns the string
# with its first vowel removed.
def remove_first_vowel(s):
    vowels = "aeiou"
    for i, ch in enumerate(s):
        if ch in vowels:
            return s[:i] + s[i+1:]
    return s

# Example usage:
print(remove_first_vowel("volcano"))  # 'vlcano'
print(remove_first_vowel("celery"))  # 'clery'
print(remove_first_vowel("juice"))  # 'jice'

# Write a function `shorten_long_words(sentence)` that accepts a string and returns
# the same sentence where words longer than 4 characters have their vowels removed.
def remove_vowels(s):
    new_str = ""
    for i in range(len(s)):
        if s[i] not in "aeiou":
            new_str += s[i]
    return new_str

def shorten_long_words(sentence):
    words = sentence.split()
    new_words = []
    for word in words:
        # Remove vowels if word length > 4
        if len(word) > 4:
            new_words.append(remove_vowels(word))
        else:
            new_words.append(word)
    return " ".join(new_words)

# Example usage:
print(shorten_long_words("they are very noble people"))  # 'they are very nbl ppl'
print(shorten_long_words("stick with it"))  # 'stck with it'
print(shorten_long_words("ballerina, you must have seen her"))  # 'bllrna, you must have seen her'
