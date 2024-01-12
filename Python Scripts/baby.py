import random

questions = ["Why is the sky blue?: ",
             "Why is ice cold?: ",
             "Why are dogs furry?: ",
             "Why don't cats bark?: ",
             "Where are all the dinosaurs?: "
             ]

answer = input(random.choice(questions)).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()

print("Oh, okay")

