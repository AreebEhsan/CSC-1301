# Taking a sentence as input from the user
sentence = input("Enter the sentence: ")

# Converting the words into lower case
case_lower = sentence.lower()

# Taking out all the words from the sentence and storing them in an array
words = case_lower.split()
print("--------   Word  Frequencies   -------")
# Using the for loop for printing out the distinct words from the set along with their frequencies using the count method
for i in set(words):
    print(i,"|", words.count(i))
