from elixir import *

metadata.bind = "sqlite:///monmonmon.sqlite"
metadata.bind.echo = True

class User(Entity):
    username = Field(UnicodeText, unique=True)
    password = Field(UnicodeText)

class Battle(Entity):
    challenger = ManyToOne('User')
    target = ManyToOne('User')
