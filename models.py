from peewee import *

db = SqliteDatabase('flashcards.db')

class FlashCard(Model):
    front = CharField()
    back = CharField()
    correct_count = IntegerField(default=0)
    incorrect_count = IntegerField(default=0)

    class Meta:
        database = db

def create_tables():
    with db: 
        db.create_tables([FlashCard])
