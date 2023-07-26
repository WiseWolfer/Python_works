import json
from pprint import pprint

presents = {}
children = {}

#
# тип хранения
# {"id", [type,age,gender,cost]}
#

with open("map (2).json", 'r') as file:
    info = json.load(file)
    max_price_gifts = 100000
    amount_of_gifts = 5000
    amount_of_children = 1000
    group_pr_boys_mark = {}
    group_pr_girls_mark = {}
    for idx, item in enumerate(info['children']):
        children[item['id']] = [item['gender'], item['age']]
    for idx, item in enumerate(info['gifts']):
        presents[item['id']] = [item['type'], item['price']]

    for item in info['gifts']:
        if "_games" in str(item['type']):
            # ставим оценку до 10
            for i in info['children']:
                if i['age'] == 10:
                    group_pr_boys_mark[item['id']] = [item['type'], i['age'], 9, item['price']]
                    group_pr_girls_mark[item['id']] = [item['type'],i['age'], 5], item['price']
                elif i['age'] == 9:
                    group_pr_boys_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
                    group_pr_girls_mark[item['id']] = item['type'], [i['age'], 5, item['price']]
                elif i['age'] == 8:
                    group_pr_boys_mark[item['id']] = [item['type'], i['age'], 7, item['price']]
                    group_pr_girls_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
                elif i['age'] == 7:
                    group_pr_boys_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
                    group_pr_girls_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
                elif i['age'] == 6:
                    group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                    group_pr_girls_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
                elif i['age'] == 5:
                    group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                    group_pr_girls_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
                elif i['age'] == 4:
                    group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                    group_pr_girls_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
                elif i['age'] == 3:
                    group_pr_boys_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
                    group_pr_girls_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
                elif i['age'] == 2:
                    group_pr_boys_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
                    group_pr_girls_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
                elif i['age'] == 1:
                    group_pr_boys_mark[item['id']] = [item['type'], i['age'], 2, item['price']]
                    group_pr_girls_mark[item['id']] = [item['type'], i['age'], 2, item['price']]
                elif i['age'] == 0:
                    group_pr_boys_mark[item['id']] = [item['type'], i['age'], 1, item['price']]
                    group_pr_girls_mark[item['id']] = [item['type'], i['age'], 1, item['price']]
        elif item['type'] == "soft_toys":
            if i['age'] == 10:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 7, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 10, item['price']]
            elif i['age'] == 9:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 8:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 7:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 6:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 5:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 4:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 3:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 2:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 1:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 0:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
        elif item['type'] == 'dolls':
            if i['age'] == 10:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 9:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 9, item['price']]
            elif i['age'] == 8:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 9, item['price']]
            elif i['age'] == 7:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 10, item['price']]
            elif i['age'] == 6:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 10, item['price']]
            elif i['age'] == 5:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 10, item['price']]
            elif i['age'] == 4:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 7, item['price']]
            elif i['age'] == 3:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
            elif i['age'] == 2:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
            elif i['age'] == 1:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
            elif i['age'] == 0:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
        elif item['type'] == 'books':
            if i['age'] == 10:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 9:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 7, item['price']]
            elif i['age'] == 8:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
                group_pr_girls_mark[item['id']] = [i['age'], 6, item['price']]
            elif i['age'] == 7:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
            elif i['age'] == 6:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
            elif i['age'] == 5:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
            elif i['age'] == 4:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
            elif i['age'] == 3:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 0, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 0, item['price']]
            elif i['age'] == 2:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 0, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 0, item['price']]
            elif i['age'] == 1:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 0, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 0, item['price']]
            elif i['age'] == 0:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 0, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 0, item['price']]
        elif item['type'] == 'sweets':
            if i['age'] == 10:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 9:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 8:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 7:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 6:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 10, item['price']]
            elif i['age'] == 5:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 4:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 3:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
            elif i['age'] == 2:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
            elif i['age'] == 1:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
            elif i['age'] == 0:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
        elif item['type'] == 'playground':
            if i['age'] == 10:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 9, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 9, item['price']]
            elif i['age'] == 9:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 8:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 7:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 7, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 7, item['price']]
            elif i['age'] == 6:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
            elif i['age'] == 5:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
            elif i['age'] == 4:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
            elif i['age'] == 3:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
            elif i['age'] == 2:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 2, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 1, item['price']]
            elif i['age'] == 1:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 0, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 0, item['price']]
            elif i['age'] == 0:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 0, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 0, item['price']]
        elif item['type'] == 'toy_vehicles':
            if i['age'] == 10:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
            elif i['age'] == 9:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 7, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
            elif i['age'] == 8:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
            elif i['age'] == 7:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
            elif i['age'] == 6:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 7, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
            elif i['age'] == 5:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
            elif i['age'] == 4:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
            elif i['age'] == 3:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
            elif i['age'] == 2:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 1, item['price']]
            elif i['age'] == 1:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 2, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 1, item['price']]
            elif i['age'] == 0:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 1, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 0, item['price']]
        elif item['type'] == 'pet':
            if i['age'] == 10:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 9:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 8:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 7, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 7, item['price']]
            elif i['age'] == 7:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
            elif i['age'] == 6:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
            elif i['age'] == 5:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
            elif i['age'] == 4:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
            elif i['age'] == 3:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
            elif i['age'] == 2:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 2, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 2, item['price']]
            elif i['age'] == 1:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 1, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 1, item['price']]
            elif i['age'] == 0:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 1, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 1, item['price']]
        elif item['type'] == 'clothes':
            if i['age'] == 10:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 9, item['price']]
            elif i['age'] == 9:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 7, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
            elif i['age'] == 8:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 7, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 7, item['price']]
            elif i['age'] == 7:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 7, item['price']]
            elif i['age'] == 6:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
            elif i['age'] == 5:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
            elif i['age'] == 4:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
            elif i['age'] == 3:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
            elif i['age'] == 2:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 2, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 2, item['price']]
            elif i['age'] == 1:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 1, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 1, item['price']]
            elif i['age'] == 0:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 1, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 1, item['price']]
        elif item['type'] == 'radio_controlled_toys':
            if i['age'] == 10:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 8, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
            elif i['age'] == 9:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 7, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
            elif i['age'] == 8:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
            elif i['age'] == 7:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 6, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
            elif i['age'] == 6:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
            elif i['age'] == 5:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 5, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
            elif i['age'] == 4:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 4, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 2, item['price']]
            elif i['age'] == 3:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 3, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 2, item['price']]
            elif i['age'] == 2:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 2, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 1, item['price']]
            elif i['age'] == 1:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 1, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 1, item['price']]
            elif i['age'] == 0:
                group_pr_boys_mark[item['id']] = [item['type'], i['age'], 1, item['price']]
                group_pr_girls_mark[item['id']] = [item['type'], i['age'], 0, item['price']]
    pprint(group_pr_girls_mark)
    print("===================================================================================")
    pprint(group_pr_boys_mark)
