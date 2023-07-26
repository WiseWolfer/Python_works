import random


def earn_money(p, n, s=0):
    counter = 0
    for _ in range(n):
        r = random.random()
        if r >= p:
            print(f'|№ испытания {counter+1} {r} - не брак, получаем прибыль |')
            s += 7
            counter += 1
        else:
            print(f'|№ испытнания {counter+1} {r} - брак, получаем убыток |')
            s -= 5
            counter += 1
    # средняя прибыль
    return s/n


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Средняя выручка/прибыль предприятия от выпуска строительного материала: ", earn_money(0.63, 100000))

