# Count number of vowels (a,o,u,e,i) in the string s
# Intput: s – string
# Output: Number of vowels = XX

def count_vowels(string_to_analyse):
    vowels = ['a', 'e', 'i', 'o', 'u']
    total = 0
    for character in string_to_analyse:
        if character in vowels:
            total += 1
    return total


s = input("Please enter a sentence: ")
number_of_vowels = count_vowels(s)

print("Number of vowels in the sentence: ", number_of_vowels)
