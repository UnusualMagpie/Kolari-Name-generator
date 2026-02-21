import random


# Names dictionary
names = {"forest":["Willow", "Bramble", "Elm", "Birch", "Oak", "Rowan", "Yew", "Pine", "Holly", "Thrush", "Briar", "Hazel", "Apple"],
 "coast":["Tern", "Gull", "Tide", "Puffin", "Godwhit", "Knot", "Scoter", "Dunlin", "Whimbrel"],
 "mountain": ["Stone", "Rock"],
 "default": []}



# Variables
default = ["Mist", "Storm", "Strix", "Thrush", "Ural", "Swallow", "Swift", "Eagle", "Swan", "Harrier", "Heron", "Scops", "Kite", "Gale", "Tawny", "Hawk", "Gust", "Finch", "Dawn", "Dusk", "Cinder", "Crow", "Raven", "Quail", "Robin", "Linnet", "Lark", "Shrike", "Sky", "Wind", "Breeze", "Feather", "Plume", "Cloud", "Wisp", "Gyr", "Peregrin", "Sparrow", "Raven", "Osprey", "Martin", ]
word2 = ["dusk","talon", "beak","feather", "flight", "fall", "spots", "eye", "eagle", "song", "storm", "dawn", "stream", "pool", "river", "wind", "wing", "sky"]

environment = ""
name_length = ""
quantity = ""

affinities = ["Rain", "Mist", "Smoke", "Sand", "Mud", "Fireflies", "Wind", "Freshwater", "Clouds", "Rock", "Plants", "Ice", "Wood", "Growth", "Butterfly", "Metal", "Sunlight", "Amber", "Heat", "Embers", "Fire", "Dust", "Crystal", "Lightning", "Snow", "Frost", "Aurora", "Ripples", "Gold", "Ash", "Underwater light", "Stars", "Tar", "Waterfall", "Sea foam", "Night sky", "Fungi", "Pollen", "Sunset clouds", "Scree", "Moonlight", "Thunder", "Dawn", "Bone", "Constellations", "Tides", "Waves", "Clay"]

# Subprograms to generate name depending on length

def short_name(pName_environment):
    options = names[pName_environment.lower()] + default # Adding default and environment lists together
    return random.choice(options)


def long_name(pName_environment):
    options = names[pName_environment.lower()] + default # Adding default and environment lists together
    return random.choice(options) + random.choice(word2)


# Main program

name_length = int(input("How many words (1 or 2)? "))
environment = input("Any specific environment? ")
quantity = int(input("How many names? "))

while quantity > 0:
    if name_length == 2:
        print(long_name(environment))
        print(random.choice(affinities))
    else:
        print(short_name(environment))
        print(random.choice(affinities))
    quantity = quantity - 1
