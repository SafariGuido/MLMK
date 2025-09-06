import json

txt = open('Scores.json', 'r')
existing_data = json.load(txt)
txt.close()
print(existing_data)
pen = open('penalties.json','r')
existing_penalty = json.load(pen)
print(existing_penalty)
pen.close()
game0 = {}
penalty0 = {}
print("What data do you want to enter?")
print("1 for scores, 2 for shot penalties, or 3 for time trials")
first = input()
if first == '1':
    print("Enter Num of Players (2-4)")
    num_plays = int(input())
    print("Enter Num of Drinking Rounds")
    num_drinks = int(input())
    beerfile = open('Beers.json', 'r')
    beerdata = json.load(beerfile)
    beerdata["Gallons of Beer Drank"] += num_drinks*num_plays*12/128
    beerfile = open('Beers.json', 'w')
    json.dump(beerdata,beerfile)
    for i in range(num_plays):
        print("Name of Player")
        name = input()
        print("Score")
        score = input()
        game0[name] = score
    existing_data.append(game0)
    txt = open('Scores.json', 'w')
    json.dump(existing_data,txt)
    txt.close()
if first == '2':
    print("Who failed their beer and took a shot penalty?")
    penalty_player = input()
    existing_penalty.append(penalty_player)
    pen = open('penalties.json','w')
    json.dump(existing_penalty,pen)
    pen.close()

if first == '3':
    print("Enter Map")
    map = input()
    print("Enter cc (200 or 150)")
    cc = input()
    print("Enter Player")
    player = input()
    print("Enter Time (seconds)")
    time = input()
    table_file = open('times.json','r')
    table = json.load(table_file)
    table.append({"map": map, "cc": cc, "player": player, "time": time})
    table_file.close()
    table_file = open('times.json','w')
    json.dump(table,table_file)
    table_file.close()
    beerfile = open('Beers.json', 'r')
    beerdata = json.load(beerfile)
    beerdata["Gallons of Beer Drank"] += 12/128
    beerfile = open('Beers.json', 'w')
    json.dump(beerdata,beerfile)