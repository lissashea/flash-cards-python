import argparse
import random
from models import *

def create_card(front,back):
    card = FlashCard(front=front, back=back)
    card.save()
    print("Flashcard created successfully")

def review_cards(num_cards):