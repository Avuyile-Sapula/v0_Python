def double_vowel(text):
    vowels = "aeiou"
    result = ""

    for char in text:
        if char in vowels:
            result += char * 2
        else:
            result += char

    return result


print(double_vowel("runner"))
# 'ruunneer'

print(double_vowel("stoplight"))
# 'stoopliight'

print(double_vowel("gardener"))
# 'gaardeeneer'


def double_vowel(word):
    vowels = "aeiou"
    result = ""

    for char in word:
        if char in vowels:
            result += char * 2
        else:
            result += char

    return result


def funny_phrase(sentence):
    words = sentence.split()
    
    for i in range(len(words)):
        if i % 2 == 1:   # every other word (2nd, 4th, 6th...)
            words[i] = double_vowel(words[i])
    
    return " ".join(words)


print(funny_phrase("she dreamed of being a runner"))
# 'she dreeaameed of beeiing a ruunneer'

print(funny_phrase("park near the stoplight"))
# 'park neeaar the stoopliight'

print(funny_phrase("we need many gardeners"))
# 'we neeeed many gaardeeneers'

def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True


print(is_prime(11))  # True
print(is_prime(8))   # False
print(is_prime(7))   # True
print(is_prime(21))  # False
print(is_prime(2))   # True
print(is_prime(15))  # False
print(is_prime(1))   # False

def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True


def pick_primes(numbers):
    primes = []

    for num in numbers:
        if is_prime(num):
            primes.append(num)

    return primes


print(pick_primes([12,3,7,18,11]))
# [3, 7, 11]

print(pick_primes([17,23,9,42]))
# [17, 23]

print(pick_primes([4,2048,100,55]))
# []