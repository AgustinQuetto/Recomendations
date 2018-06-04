import json

with open('db.json') as f:
    dataset = json.load(f)

#decisions = []
decisions = ['Comedy', 'Fantasy', 'Beetlejuice']
"""
for i in range(0,3):
    decisions.append(input('Escribi algo: '))

for i in range(0,len(decisions)):
    print("You selected: %s" % decisions[i])

for data in dataset['movies']:
    print(data)
"""
selections = []
minScore = 2

for target_list in dataset['movies']:
    matching = 0
    for decision in decisions:
        if target_list['title'] in decision:
            matching += 1

    for genres in target_list['genres']:
        for decision in decisions:
            if genres == decision:
                matching += 1

    if minScore <= matching:
        selections.append(target_list)
        print("Match")
    else:
        print("Not match")

print(selections)
