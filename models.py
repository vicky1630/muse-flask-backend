# import * means import everything from peewee

from peewee import *
import datetime

# Connect to a Postgres database.
DATABASE = PostgresqlDatabase('muse_app', host='localhost', port=5432)

class Song(Model):
    song_name = CharField()
    artist = CharField()
    release_year = IntegerField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Song], safe=True)
    print("TABLES Created")
    DATABASE.close()