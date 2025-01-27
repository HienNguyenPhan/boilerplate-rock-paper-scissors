# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_opponent_play, opponent_history=[], play_order=[{}]):
    if not prev_opponent_play:
        prev_opponent_play = 'S'

    opponent_history.append(prev_opponent_play)

    last_five = "".join(opponent_history[-5:])
    if len(last_five) == 5:
        if last_five not in play_order[0]:
            play_order[0][last_five] = 0
        play_order[0][last_five] += 1

    last_four = "".join(opponent_history[-4:])
    potential_plays = {
        last_four + next_move: play_order[0].get(last_four + next_move, 0)
        for next_move in "RPS"
    }

    prediction = max(potential_plays, key=potential_plays.get)[-1:]
   
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]
