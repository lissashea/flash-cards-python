from peewee import *

db = SqliteDatabase('flashcards.db')

class FlashCard(Model):
    front = Charfield()
    back = CharField()
    correct_count = IntegerField(default=0)
    incorrect_count = IntegerField(default=0)
    