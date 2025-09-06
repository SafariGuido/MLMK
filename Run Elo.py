import json
import copy
import pandas as pd


tempscores = open('Scores.json', 'r')
scores = json.load(tempscores)
tempscores.close()

#generate elo list
elo = {}
dict_points = {}


for i in range(len(scores)):
    for j in range(len(scores[i])):
        elo[list(scores[i])[j]]=100
        dict_points[list(scores[i])[j]]=0


for i in range(len(scores)):
    current_scores = scores[i]
    updated_elo = []
    for j in range(len(current_scores)):
        names = copy.deepcopy(list(current_scores))
        current_player = names[j]
        player_points = float(current_scores[current_player])
        dict_points[current_player] += player_points
        current_elo = elo[current_player]
        opponents = copy.deepcopy(names)
        opponents.remove(current_player)
        avg_opp_elo_running = 0
        total_points = 0
        for l in range(len(names)):
            total_points += float(current_scores[names[l]])
        player_score1 = player_points/total_points
        for k in range(len(opponents)):
            avg_opp_elo_running += (float(elo[names[k]])/len(opponents))
        if len(names) == 4:
            exp_score = 1/(1+10**((current_elo-avg_opp_elo_running)/400)) 
            playerscore2 = player_score1*2.2
            player_score = (player_score1-(4/44))/((20/44)-(4/44))
            elo_adj = total_points*(player_score - exp_score)
            updated_elo.append(elo_adj)
        if len(names) == 3:
            exp_score = 1/(1+10**((current_elo-avg_opp_elo_running)/400))
            playerscore2 = player_score1*1.75
            player_score = (player_score1-(4/28))/(16/28-(4/28))
            elo_adj = total_points*(player_score - exp_score)
            updated_elo.append(elo_adj)
        if len(names) == 2:
            exp_score = 1/(1+10**((current_elo-avg_opp_elo_running)/400))
            playerscore2 = player_score1*2.2
            player_score = (player_score1-.333333)/(1-.33333)
            elo_adj = total_points*(player_score - exp_score)
            updated_elo.append(elo_adj)

    for l in range(len(updated_elo)):
        elo[names[l]] += updated_elo[l]

sorted_elo =  dict(sorted(elo.items(), key=lambda item: item[1], reverse=True))

with open('Rank.json', 'w') as file:
    json.dump(sorted_elo, file)

sorted_dict_points =  dict(sorted(dict_points.items(), key=lambda item: item[1], reverse=True))

with open('total_scores.json', 'w') as file:
    json.dump(sorted_dict_points, file)

pen_dict = {}
pen_file = open('penalties.json', 'r')
pen_list = json.load(pen_file)
for i in range(len(pen_list)):
    name = pen_list[i]
    num = pen_list.count(name)
    pen_dict[name] = num


sorted_pen_dict =  dict(sorted(pen_dict.items(), key=lambda item: item[1], reverse=True))    

pendict_file = open('pen_dict.json', 'w')
json.dump(sorted_pen_dict,pendict_file)
pendict_file.close()