import random

# Variables
word1 = ["Mist", "Storm", "Strix", "Thrush", "Ural", "Swallow", "Swift", "Eagle", "Swan", "Harrier", "Heron", "Scops", "Kite", "Gale", "Tawny", "Hawk", "Gust", "Finch"]
word2 = ["dusk","talon", "beak","feather", "flight", "fall", "spots", "eye", "eagle", "song", "storm", "dawn", "stream", "pool", "river", "wind", "wing", "sky"]
forest = ["Willow", "Bramble", "Finch", "Elm", "Birch", "Oak", "Rowan", "Yew", "Pine", "Holly", "Dawn", "Dusk", "Robin", "Thrush"]
coast = ["Tern"]
environment = ""
name_length = ""

# Subprograms to generate name depending on length

def short_name(pName_environment):
    if pName_environment.lower() == "forest":
        return random.choice(forest)
    elif pName_environment.lower() == "coast":
        return random.choice(coast)
    else:
        return random.choice(word1)

def long_name(pName_environment):
    if pName_environment.lower() == "forest":
        return random.choice(forest) + random.choice(word2)
    elif pName_environment.lower() == "coast":
        return random.choice(coast) + random.choice(word2)
    else:
        return random.choice(word1) + random.choice(word2)




name_length = int(input("How many words (1 or 2)? "))
environment = input("Any specific environment? ")

if name_length == 2:
    print(long_name(environment))
else:
    print(short_name(environment))