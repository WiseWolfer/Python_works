import matplotlib.pyplot as plt
from matplotlib import collections as mc


def drawlattice(n,name):
    for i in range(1, n+1):
        for j in range(1, n+1):
            plt.plot(i, j, 'o',c='black')
            plt.savefig(name)
    plt.show()


def drawgame(n,name,game):
    color2 = []
    for k in range(0, len(game)):
        if k % 2 == 0:
            color2.append('red')
        else:
            color2.append('blue')
            lc = mc.LineCollection(game, color=color2, linewidths=2)
            fig, ax = plt.subplots()
            for i in range(1, n+1):
                for j in range(1, n+1):
                    plt.plot(i, j, 'o', c='black')
                    ax.add_collection(lc)
                    ax.autoscale()
                    ax.margins(0.1)
                    plt.savefig(name)
    plt.show()


def squarefinder(game):
    countofsquares=0
    for line in game:
        parallel = False
        left = False
        right = False
        if line[0][1] == line[1][1]:
            if [(line[0][0], line[0][1]-1, (line[1][0], line[1][1]-1))] in game:
                parallel = True
            if [(line[0][0], line[0][1], (line[1][0]-1, line[1][1]-1))] in game:
                left = True
            if [(line[0][0]+1, line[0][1], (line[1][0], line[1][1]-1))] in game:
                right = True
            if parallel and left and right:
                countofsquares += 1

    return(countofsquares)

drawlattice(5,'lattice.png')
game=[[(1,2),(1,1)],[(3,3),(4,3)],[(1,5),(2,5)],[(1,2),(2,2)],[(2,2),(2,1)],
[(1,1),(2,1)],[(3,4),(3,3)],[(3,4),(4,4)]]
drawgame(5, 'lattice.png', game)
print(squarefinder(game))
