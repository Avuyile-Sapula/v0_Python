def word_replace(sentence, replacements):
    words = sentence.split()
    new_words = []

    for word in words:
        if word in replacements:
            new_words.append(replacements[word])
        else:
            new_words.append(word)

    return " ".join(new_words)
print(word_replace(
"I never take naps during the day",
    {"never":"always","day":"weekend" }
))
# 'I always take naps during the weekend'

print(word_replace(
"the park is closed",
    {"closed":"open","the":"a" }
))
# 'a park is open'

print(word_replace(
"I do what I want",
    {"I":"we","cat":"dog" }
))
# 'we do what we want'

