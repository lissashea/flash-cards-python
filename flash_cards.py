import argparse
import random
from models import *

def create_card(front,back):
    card = FlashCard(front=front, back=back)
    card.save()
    print("Flashcard created successfully")

def review_cards(num_cards):
    cards = list(FlashCard.select())
    random.shuffle(cards)
    review_count = min(num_cards, len(cards))

    for i in range(review_count):
        card = cards[i]
        print(f"Front: {card.front}")
        input("Press Enter to see the back...")
        print(f"Back: {card.back}")

        answer = input("Did you answer correctly? (y/n): ")
        if answer.lower() == 'y':
            card.correct_count += 1
        else:
            card.incorrect_count += 1
        card.save()