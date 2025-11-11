import random

subjects = [
    "shahrukh khan",
    "virat koli",
    "salman khan",
    "Hrithik Roshan",
    "A group of dog",
    "Prime Minister Imran Khan",
    "Auto Rickshaw Driver from Faisalabad",
    "Mia khalifa"
]
actions = [
    "play football",
    "Sex with",
    "dance with",
    "eats",
    "fuck",
    "celebrates",
]
places_or_things = [
    "Faisalabad",
    "Train of Multan",
    "toy of rubber",
    "inside the school",
    "during sex",
    "with dog",
    "Jhony sins"
]
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEW: {subject} {action} {place_or_thing}"
    print("\n" + headline)
    user = input("Do you want another headline (yes/no): ").strip().lower()
    if user == "no":
        break

print("\n Thanks for using Fake Headline Generator")