import random


# Names dictionary
names = {"forest":["Willow", "Bramble", "Elm", "Birch", "Oak", "Rowan", "Yew", "Pine", "Holly", "Thrush", "Briar", "Hazel"],
 "coast":["Tern", "Gull"],
 "mountain": ["Stone", "Rock"],
 "default": []}



# Variables
default = ["Mist", "Storm", "Strix", "Thrush", "Ural", "Swallow", "Swift", "Eagle", "Swan", "Harrier", "Heron", "Scops", "Kite", "Gale", "Tawny", "Hawk", "Gust", "Finch", "Dawn", "Dusk", "Cinder", "Crow", "Raven", "Quail", "Robin", "Linnet", "Lark"]
word2 = ["dusk","talon", "beak","feather", "flight", "fall", "spots", "eye", "eagle", "song", "storm", "dawn", "stream", "pool", "river", "wind", "wing", "sky"]
environment = ""
name_length = ""

# Subprograms to generate name depending on length

def short_name(pName_environment):
    options = names[pName_environment.lower()] + default
    return random.choice(options)


def long_name(pName_environment):
    options = names[pName_environment.lower()] + default
    return random.choice(options) + random.choice(word2)




name_length = int(input("How many words (1 or 2)? "))
environment = input("Any specific environment? ")

if name_length == 2:
    print(long_name(environment))
else:
    print(short_name(environment))