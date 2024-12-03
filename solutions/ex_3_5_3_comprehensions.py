# Write a list comprehension that creates a list of numbers from 1 to 20 that
# are divisible by 3.
div_by_3 = [i for i in range(1, 21) if i % 3 == 0]
print(div_by_3)

# Write a list comprehension that creates a list of all the words in a given
# string that have more than 3 letters.
text = "Write a list comprehension that transforms all strings"
long_words = [word for word in text.split() if len(word) > 3]
print(long_words)

# Create a dict {"a": 97, "b": 98, ... } using comprehension. Use ord built-in
# to obtain ASCII code and string.ascii_lowercase to get all letters.
import string

ascii_dict = {char: ord(char) for char in string.ascii_lowercase}
print(ascii_dict)

# Using the dictionary generated above, create another one where you swap keys
# and values.
swapped_dict = {value: key for key, value in ascii_dict.items()}
print(swapped_dict)

# Write a set comprehension to get all lowercase words in a text.
text = "Write a set comprehension to get all lowercase words in a text"
words = {word.lower() for word in text.split()}
print(words)
