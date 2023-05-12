from peewee import *

# Modify the connection parameters to match your PostgreSQL setup
db = PostgresqlDatabase('flash_cards', 
                        user='lissa', 
                        password='123',
                        host='localhost', 
                        port=5432)

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

# Add this code to create the database if it doesn't exist
if not db.connect():
    db.create_database('flash_cards')

# Call the create_tables function to create the necessary tables
create_tables()
