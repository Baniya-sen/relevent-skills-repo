from flask import Flask, request, jsonify, render_template, session
import tictactoe as ttt

app = Flask(__name__)
# Set the secret key for the Flask application
app.secret_key = 'your_secrey-key-text'
# Set the SESSION_COOKIE_SECURE option to True
app.config['SESSION_COOKIE_SECURE'] = True


def new_game():
    session['board'] = ttt.initial_state()

@app.route("/")
def index():
    new_game()
    return render_template("index.html")

# Endpoint to retrieve the current board state and player turn
@app.route('/board', methods=['GET'])
def get_board():
    return jsonify({
        'board': session.get('board', ttt.initial_state()),
    })

# Endpoint to submit the user move
@app.route('/move', methods=['POST'])
def move():
    try:
        move = request.get_json()
        x, y = move['x'], move['y']

        if session['board'][x][y] is None:
            session['board'] = ttt.result(session['board'], (x, y))
            winner = ttt.winner(session['board'])
            if winner is not None:
                return jsonify({    
                    'board': session['board'],
                    'winner': winner
                })
            elif ttt.terminal(session['board']):
                return jsonify({
                    'board': session['board'],
                    'winner': 'draw'
                })
            else:
                return jsonify({
                    'board': session['board']
                })
        else:
            return jsonify({
                'error': 'Invalid move'
            }), 400
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

# Endpoint to get and submit the AI move
@app.route('/aiplay', methods=['POST'])
def ai_move():
    try:
        session['board'] = request.json['boardState']
        move = ttt.minimax(session['board'])
        session['board'] = ttt.result(session['board'], (move))
        winner = ttt.winner(session['board'])
        if winner is not None:
            return jsonify({
                'board': session['board'],
                'winner': winner
            })
        elif ttt.terminal(session['board']):
            return jsonify({
                'board': session['board'],
                'winner': 'draw'
            })
        else:
            return jsonify({
                'board': session['board']
            })
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

# Endpoint to reset the game
@app.route('/reset', methods=['GET'])
def reset():
    new_game()
    return jsonify({
        'board': session['board']
    })

if __name__ == '__main__':
    app.run(debug=True)