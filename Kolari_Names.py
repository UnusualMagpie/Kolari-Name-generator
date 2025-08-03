import random


word1 = ["Eagle", "Swan", "Harrier", ""]
word2 = ["talon", "beak","feather", "flight", "fall", "spots", "eye", "eagle", "song", "storm"]
root1 = ["Elm", "Birch"]
choice = ""


choice = input("For the Rootsingers?")

if choice == "y":
    print(random.choice(root1) + random.choice(word2))
else:
    print(random.choice(word1) + random.choice(word2))