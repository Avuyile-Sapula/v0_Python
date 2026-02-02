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
