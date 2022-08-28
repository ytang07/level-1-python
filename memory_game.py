import random 
import string
from time import sleep

def play_game():
    k = 3
    loss = False
    letters = string.ascii_lowercase
    while not loss:
        term = ''.join(random.choice(letters) for i in range(k))
        print(term)
        sleep(3)
        for x in range(100):
            print("\n")
        user = input("What was the string?")
        if user == term:
            k += 1
        else:
            loss = True
            print(f"Final Score: {k-1}")

play_game()