import argparse
import random
from models import *


def create_capital_cards():
    capitals = [
        {"front": "France", "back": "Paris"},
        {"front": "Germany", "back": "Berlin"},
        {"front": "Italy", "back": "Rome"},
        {"front": "United Kingdom", "back": "London"},
        {"front": "Spain", "back": "Madrid"},
        {"front": "Russia", "back": "Moscow"},
        {"front": "Canada", "back": "Ottawa"},
        {"front": "United States", "back": "Washington, D.C."},
        {"front": "Australia", "back": "Canberra"},
        {"front": "China", "back": "Beijing"},
        {"front": "India", "back": "New Delhi"},
        {"front": "Brazil", "back": "Brasília"},
        {"front": "South Africa", "back": "Pretoria"},
        {"front": "Mexico", "back": "Mexico City"},
        {"front": "Japan", "back": "Tokyo"}
    ]

    for capital in capitals:
        create_card(capital["front"], capital["back"])

def create_card(front, back):
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

def parse_arguments():
    parser = argparse.ArgumentParser(description="Flash Cards Application")
    subparsers = parser.add_subparsers(dest="command")

    create_parser = subparsers.add_parser("create", help="Create a new flash card")
    create_parser.add_argument("front", help="Front side of the flash card")
    create_parser.add_argument("back", help="Back side of the flash card")

    create_capitals_parser = subparsers.add_parser("create_capitals", help="Create flash cards for international capitals")

    review_parser = subparsers.add_parser("review", help="Set up a training session and review flash cards")
    review_parser.add_argument("num_cards", type=int, help="Number of flash cards to review")

    return parser.parse_args()

if __name__ == "__main__":
    create_tables()

    args = parse_arguments()

    if args.command == "create":
        create_card(args.front, args.back)
    elif args.command == "create_capitals":
        create_capital_cards()
    elif args.command == "review":
        review_cards(args.num_cards)
    else:
        print("Invalid command")
