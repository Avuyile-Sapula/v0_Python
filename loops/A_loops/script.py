# Write a function `starts_with_r` that accepts a string as an argument.
# The function should return True if the string starts with 'r' or 'R'.
# Otherwise, return False.

def starts_with_r(str):
    if str[0] == "r" or str[0] == "R":
        return True
    else:
        return False
    
print(starts_with_r("roger that"))        # True
print(starts_with_r("Row, row, row your boat"))  # True
print(starts_with_r("slip"))              # False
print(starts_with_r("Taxicab"))           # False


# Write a function `parity` that accepts a number.
# Return the string "even" if the number is even.
# Return the string "odd" if the number is odd.

def parity(num):
    if num%2==0:
        return "even"
    else:
        return "odd"

print(parity(5))       # "odd"
print(parity(7))       # "odd"
print(parity(13))      # "odd"
print(parity(32))      # "even"
print(parity(10))      # "even"
print(parity(602348))  # "even"



# Write a function `longer` that accepts two strings.
# Return the string that is longer.
# If both strings have the same length, return the first string.

def longer(str1,str2):
    len1 = len(str1)
    len2 = len(str2)

    if len1 > len2:
        return str1
    elif len1 == len2:
        return str1
    else:
        return str2
    
print(longer("drum", "piranha"))       # "piranha"
print(longer("basket", "fork"))        # "basket"
print(longer("flannel", "sustainable"))# "sustainable"
print(longer("disrupt", "ability"))    # "disrupt"
print(longer("bird", "shoe"))          # "bird"

# Write a function `one_or_none` that accepts two boolean values.
# Return True if EXACTLY ONE of them is True.
# Return False if both are True OR both are False.

def one_or_none(Bool1,Bool2):
    if Bool1 == True and Bool2 == False:
        return True
    elif Bool2 == True and Bool1== False:
        return True
    else: 
        return False;
    

print(one_or_none(False, False))   # False
print(one_or_none(True, False))    # True
print(one_or_none(False, True))    # True
print(one_or_none(True, True))     # False



# Write a function `ends_in_ly` that accepts a string.
# Return True if the string ends with "ly".
# Otherwise, return False.

def ends_in_ly(str):
    if str[-1] == "y" and str[-2] == "l":
        return True
    else:
        return False

print(ends_in_ly("pretty"))      # False
print(ends_in_ly("instant"))     # False
print(ends_in_ly("analytic"))    # False
print(ends_in_ly("timidly"))     # True
print(ends_in_ly("fly"))         # True
print(ends_in_ly("gallantly"))   # True



# Write a function `funny_sound` that accepts two strings.
# Return a new string made from:
# - the first three characters of the first string
# - the first three characters of the second string
#
# You may assume both strings are at least 3 characters long.

def funny_sound(str1, str2):
    new_str1 = str1[0:3]
    new_str2 = str2[0:3]
    final_str = new_str1 + new_str2
    return final_str

print(funny_sound("tiger", "spoon"))       # "tigspo"
print(funny_sound("computer", "phone"))    # "compho"
print(funny_sound("skate", "bottle"))      # "skabot"
print(funny_sound("frog", "ashtray"))      # "froash"


# Write a function `string_size` that accepts a string.
# Return:
#   "small"  → if length < 5
#   "medium" → if length == 5
#   "large"  → if length > 5'

def string_size(str):
    str_len = len(str)
    if str_len < 5:
        return "small"
    elif str_len == 5:
        return "medium"
    else:
        return "large"
    

print(string_size("cat"))          # "small"
print(string_size("bell"))         # "small"
print(string_size("ready"))        # "medium"
print(string_size("shirt"))        # "medium"
print(string_size("shallow"))      # "large"
print(string_size("intelligence")) # "large"

