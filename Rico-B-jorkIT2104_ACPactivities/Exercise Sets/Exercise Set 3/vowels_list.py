wordstring = input("Enter a string: ")
vowels = "aAeEiIoOuU"
vowel_in_a_list = []

for char in wordstring:
    if char in vowels:
        vowel_in_a_list.append(char)

print(vowel_in_a_list)