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