from flask import request, session, escape
import json

from monmonmon import app
from monmonmon.model import User, Battle
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
    challenger = User.query.filter_by(username=session['username']).one()
    target = User.query.filter_by(username=request.form['target']).one()
    battle = Battle(challenger=challenger, target=target)
    elixir_session.commit()
    return json.dumps({'battle': battle.id})
