# Given a string, find its first non-repeated character.
# 1) Loop the input
# 2) If the character doesn't exist in 'letters', we append it there and set the count to 1
# 3) If it does, simply increment the count
# 4) Loop through the 'letters' list, as soon as we find a character that occurs once, return it.

letters = []
count = {}


def find_first_non_repeated(string):
    for char in string:
        if char in letters:
            count[char] += 1

        else:
            letters.append(char)
            count[char] = 1

    for char in letters:
        if count[char] == 1:
            return char


print find_first_non_repeated('geeksforgeeks')