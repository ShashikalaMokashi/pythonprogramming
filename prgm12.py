#read word and print no of  letters ,vowles in world
word = input("enter a word:")
letter_count = 0
vowel_count = 0

for char in word:
    if char.isalpha():
        letter_count += 1
    if char.lower() in "aeiou":
        vowel_count += 1

print("no of letters:", letter_count)
print("no of vowels=", vowel_count)