import random
import sys
sys.path.append('..')

from starter_projects.generate_deck import generate_cards, face_cards

cards = generate_cards()

def split_deck(cards=cards):
    yours = random.sample(cards, 26)
    opp = [i for i in cards if i not in yours]
    random.shuffle(opp)
    return yours, opp

your_cards, opp_cards = split_deck()

def draw(cards):
    return cards.pop(0)

def play_turn(yours=your_cards, opp=opp_cards):
    your_play = draw(yours)
    opp_play = draw(opp)
    your_val = your_play.value if your_play.value not in face_cards else face_cards[your_play.value]
    opp_val = opp_play.value if opp_play.value not in face_cards else face_cards[opp_play.value]
    print(f"Your play: {your_val} {your_play.suit}")
    print(f"Opp play: {opp_val} {opp_play.suit}")
    if your_val > opp_val:
        yours.append(your_play)
        yours.append(opp_play)
    elif opp_val > your_val:
        opp.append(opp_play)
        opp.append(your_play)
    else:
        yours.append(your_play)
        opp.append(opp_play)
    return yours, opp

yours, opp = play_turn()
counter = 0
while yours and opp:
    counter += 1
    yours, opp = play_turn(yours, opp)
    print(counter)
    print(len(yours), len(opp))
    if len(yours) == 0:
        print("You Lose!")
    if len(opp) == 0:
        print("You Win!")
    