p1_pos = 5
p2_pos = 10

# p1_pos = 4
# p2_pos = 8

p1_score = 0
p2_score = 0

roll = list(range(1,101)) + list(range(1,101))
trncnt = 0
rllcnt = 0
while p1_score < 1000 and p2_score < 1000:
    if trncnt %2 == 0:
        p1_pos = (p1_pos + sum(roll[rllcnt:rllcnt+3]))
        while p1_pos > 10:
            p1_pos -= 10
        p1_score += p1_pos
        rllcnt += 3
        trncnt += 1
    else:
        p2_pos = (p2_pos + sum(roll[rllcnt:rllcnt + 3]))
        while p2_pos > 10:
            p2_pos -= 10
        p2_score += p2_pos
        rllcnt += 3
        trncnt += 1

    rllcnt %= 100

print(trncnt*3*min(p1_score,p2_score))


from collections import Counter

p1_pos = 5
p2_pos = 10

p1_score = 0
p2_score = 0

player_turn = 0


game_states = Counter()
finished_games = Counter()

game_states[(p1_pos,p2_pos,p1_score,p2_score,player_turn)] += 1
while len(game_states) > 0:
    next_game_states = Counter()
    for state,amt in game_states.items():
        if state[4] == 0:
            for i in range(1,4):
                for j in range(1,4):
                    for k in range(1,4):
                        next_p1_pos = state[0] + i + j + k - 1
                        next_p1_pos %= 10
                        next_p1_pos += 1
                        next_p1_score =  state[2] + next_p1_pos
                        new_state = (next_p1_pos,state[1],next_p1_score,state[3],1)
                        if next_p1_score >= 21:
                            finished_games[new_state] += amt
                        else:
                            next_game_states[new_state] += amt
        else:
            for i in range(1,4):
                for j in range(1,4):
                    for k in range(1,4):
                        next_p2_pos = state[1] + i+j+k - 1
                        next_p2_pos %= 10
                        next_p2_pos += 1
                        next_p2_score = state[3] + next_p2_pos
                        new_state = (state[0],next_p2_pos,state[2],next_p2_score,0)
                        if next_p2_score >= 21:
                            finished_games[new_state] += amt
                        else:
                            next_game_states[new_state] += amt
        game_states = next_game_states.copy()

p1_wins = 0
p2_wins = 0
for state,amt in finished_games.items():
    if state[2] >= 21:
        p1_wins += amt
    else:
        p2_wins += amt
print(max(p1_wins,p2_wins)) # 5701203369987683 wrong