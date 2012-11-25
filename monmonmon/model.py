import datetime

from elixir import *

metadata.bind = "sqlite:///monmonmon.sqlite"
metadata.bind.echo = True

class User(Entity):
    username = Field(UnicodeText, unique=True)
    password = Field(UnicodeText)

class Battle(Entity):
    challenger = ManyToOne('User')
    target = ManyToOne('User')

# Type strings for Event entries.
BATTLE_START = "Battle Start"
STARTING_PLAYER = "Picked Starting Player"

class Event(Entity):
    battle = ManyToOne('Battle')
    type = Field(UnicodeText)
    extra_data = Field(UnicodeText)
    timestamp = Field(DateTime, default=datetime.datetime.now)
