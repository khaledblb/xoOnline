from flask import Flask, render_template, request

app = Flask(__name__)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    winner = None

    while not winner and not is_board_full(board):
        row = int(request.form['row'])
        col = int(request.form['col'])

        if board[row][col] == ' ':
            board[row][col] = player
            if check_winner(board, player):
                winner = player
            player = 'O' if player == 'X' else 'X'

    return render_template('result.html', board=board, winner=winner)

if __name__ == '__main__':
    app.run(debug=True)