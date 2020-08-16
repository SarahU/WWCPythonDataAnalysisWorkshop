# Write a function which will return how many times a word (symbols separated with space, coma and dot) meet in the string
# Input: s – string
# Output: word1 = number, word2 = number
#
# Example:
# Input: s= “Tom eats and eats”
# Output: Tom = 1, eats = 2, and = 1

separators = [' ', ',', '.']


def count_words(sentence):
    sentence = sentence.replace(separators[1], separators[0])
    sentence = sentence.replace(separators[2], separators[0])

    print('New Sentence: ', sentence)

    words = sentence.split(separators[0])
    word_map = {}
    for word in words:
        if word != '':
            if word not in word_map:
                word_map[word] = 1
            else:
                word_map[word] = word_map[word]+1

    return word_map


# sen = "The quick brown fox jumped. They jumped over the other fox, who also brown and lazy, but was not that quick."
sen = input('Type a sentence: ')
result = count_words(sen)
print(result)
