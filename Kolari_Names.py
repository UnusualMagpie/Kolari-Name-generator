import random


word1 = ["Mist", "Storm", "Strix", "Thrush", "Ural", "Swallow", "Swift", "Eagle", "Swan", "Harrier", "Heron", "Scops", "Kite", "Gale", "Tawny", "Hawk", "Gust", "Finch"]
word2 = ["dusk","talon", "beak","feather", "flight", "fall", "spots", "eye", "eagle", "song", "storm", "dawn", "stream", "pool", "river", "wind", "wing", "sky"]
forest = ["Willow", "Bramble", "Finch", "Elm", "Birch", "Oak", "Rowan", "Yew", "Pine", "Holly", "Dawn", "Dusk", "Robin", "Thrush"]
choice = ""


choice = input("Any specific environment? ")

if choice == "Forest":
    print(random.choice(forest) + random.choice(word2))
else:
    print(random.choice(word1) + random.choice(word2))