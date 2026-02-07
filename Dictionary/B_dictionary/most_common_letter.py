def most_common_letter(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    return max(counts, key=counts.get)
print(most_common_letter("building"))
# 'i'

print(most_common_letter("shoestring"))
# 's'

print(most_common_letter("preparedness"))
# 'e'

