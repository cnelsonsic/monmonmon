from flask import request, session, escape, jsonify, json
import random

from monmonmon import app
from monmonmon.model import User, Battle, Event, BATTLE_START, STARTING_PLAYER
from monmonmon.model import session as elixir_session

@app.route('/users/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user:
        return "Username already registered.", 403

    User(username=username, password=password)
    elixir_session.commit()
    return "registered successfully."

@app.route('/users/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username, password=password).one()
    session['username'] = user.username
    return "Logged in successfully."

@app.route('/battle/start', methods=['POST'])
def start_battle():
    challenger = get_current_user()
    target = User.query.filter_by(username=request.form['target']).one()
    battle = Battle(challenger=challenger, target=target)
    start = Event(battle=battle, type=BATTLE_START)
    firstplayer = Event(battle=battle, type=STARTING_PLAYER, extra_data=json.dumps(dict(player=random.choice([challenger.id, target.id]))))
    elixir_session.commit()
    return jsonify(battle=battle.id)

@app.route('/battle/current_player/<int:battle_id>')
def get_current_player(battle_id):
    battle = get_battle(battle_id)
    me = get_current_user()
    from sqlalchemy import desc
    events = Event.query.filter_by(battle=battle)\
                        .order_by(desc(Event.timestamp))\
                        .all()
    for event in events:
        if event.type in (STARTING_PLAYER,):
            return get_user(json.loads(event.extra_data)['player'])

def get_battle(battle_id):
    return Battle.query.filter_by(id=battle_id).first()

def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

def get_current_user():
    return User.query.filter_by(username=session['username']).one()

@app.route('/battle/menu/<int:battle_id>')
def get_menu(battle_id):
    battle = get_battle(battle_id)
    me = get_current_user()
    current_player = get_current_player(battle_id)
    if current_player == me:
        # Our turn, so show a menu.
        return jsonify(menu=['Fight', 'Monsters', 'Items', 'Run'])
    else:
        # Waiting on the other player...
        return jsonify(message="Waiting for other player to act...")
