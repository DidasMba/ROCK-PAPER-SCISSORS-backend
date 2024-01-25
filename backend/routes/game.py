from flask import jsonify, request
from . import app
from ..services import game_service

@app.route('/play', methods=['POST'])
def play_game():
    # Implement Rock, Paper, Scissors game logic using game_service
    return jsonify({'message': 'Play game route'})
