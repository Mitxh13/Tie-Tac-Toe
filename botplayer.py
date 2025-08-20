
import math
winning_moves = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9),
    (1, 4, 7), (2, 5, 8), (3, 6, 9),
    (1, 5, 9), (3, 5, 7)
]

def check_winner(dict_moves):
    for combo in winning_moves:
        if all(dict_moves.get(pos) == "X" for pos in combo):
            return "X"
        elif all(dict_moves.get(pos) == "O" for pos in combo):
            return "O"
    return None

def minimax(dict_moves, used_moves, is_maximizing):
    winner = check_winner(dict_moves)
    if winner == "X":
        return 1
    elif winner == "O":
        return -1
    elif len(used_moves) == 9:
        return 0

    if is_maximizing:  # AI MOVE
        best_score = -math.inf
        for move in range(1, 10):
            if move not in used_moves:
                dict_moves[move] = "O"
                used_moves.append(move)
                score = minimax(dict_moves, used_moves, False)
                used_moves.remove(move)
                del dict_moves[move]
                best_score = max(best_score, score)
        return best_score
    else:  #Player Move
        best_score = math.inf
        for move in range(1, 10):
            if move not in used_moves:
                dict_moves[move] = "X"
                used_moves.append(move)
                score = minimax(dict_moves, used_moves, True)
                used_moves.remove(move)
                del dict_moves[move]
                best_score = min(best_score, score)
        return best_score

def system_move(used_moves, dict_moves):
    for move in range(1, 10):
        if move not in used_moves:
            dict_moves[move] = "O"
            if check_winner(dict_moves) == "O": 
                used_moves.append(move)
                return move
            del dict_moves[move]

    #Check if Player is winning then the Bot will block the player move
    for move in range(1, 10):
        if move not in used_moves:
            dict_moves[move] = "X"
            if check_winner(dict_moves) == "X":  # Player has chance to win
                dict_moves[move] = "O"  #Bot gonna block it 
                used_moves.append(move)
                return move
            del dict_moves[move]
    best_score = -math.inf
    best_move = None
    for move in range(1, 10):
        if move not in used_moves:
            dict_moves[move] = "O"
            used_moves.append(move)
            score = minimax(dict_moves, used_moves, False)
            used_moves.remove(move)
            del dict_moves[move]
            if score > best_score:
                best_score = score
                best_move = move
    used_moves.append(best_move)
    return best_move
