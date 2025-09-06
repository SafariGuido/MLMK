import json
import copy

tempscores = open('Scores.json', 'r')
scores = json.load(tempscores)
total_score = {}
avg_score = {}
#elo_dict = {}

players = ["Jonah","Sam","Kurtis","Lance","Alex","Nathan","Noah","David","Matt","Ryley"]
#for n in range(len(players)):
    #elo_dict[players[n]] = 0

for n in range(len(players)):
    player_total = 0
    num_games = 0
    #startelo = 0
    #expectedscore = 12.5
    for i in range(len(scores)):
        indscore = scores[i].get(players[n])
        if indscore != None:
            player_total += int(indscore)
            num_games += 1
            #newelo = startelo + (int(indscore)-expectedscore)
            #startelo = copy.copy(newelo)
            #expectedscore = player_total/num_games
        total_score[players[n]] = player_total
    if num_games > 0:
        total_score[players[n]] = player_total
        avg_score[players[n]] = player_total/num_games
        #elo_dict[players[n]] = newelo
print("Total_Score")
print(total_score)
print("avg_score")
print(avg_score)
#print("Elo")
#print(elo_dict)
sorted_total_scored = dict(sorted(total_score.items(), key=lambda item: item[1], reverse=True))
final = open('total_scores.json', 'w')
json.dump(sorted_total_scored,final)
final.close()
#elo = open('Rank.json', 'w')
#json.dump(elo_dict,elo)
#elo.close()
avg = open('avg_scores.json', 'w')
json.dump(avg_score,avg)
avg.close()
   
#for n in range(len(players)):
   # for i in range(len(scores)):

pen_dict = {}
pen_file = open('penalties.json', 'r')
pen_list = json.load(pen_file)
for i in range(len(pen_list)):
    name = pen_list[i]
    num = pen_list.count(name)
    pen_dict[name] = num

pendict_file = open('pen_dict.json', 'w')
json.dump(pen_dict,pendict_file)
pendict_file.close()
