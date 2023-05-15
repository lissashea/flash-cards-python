from peewee import *

db = PostgresqlDatabase('flash_cards', 
                        user='lissa', 
                        password='123',
                        host='localhost', 
                        port=5432)

db.connect()

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

db.create_tables([FlashCard])
