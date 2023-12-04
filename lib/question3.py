import string

def word_frequency(sentence):
    word_count = {}

    # Remove punctuation, convert to lowercase, and split the sentence into words
    sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower().split()

    # Count frequency of each word
    for word in sentence:
        # Increment word count or set it to 1 if encountering the word for the first time
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

# SAMPLE TEST CASE:
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
