import numpy as np
from matplotlib import pyplot as plt

def show(find_Queen, find_myKing, find_OtherKing):
    x = [find_Queen[0], find_myKing[0], find_OtherKing[0]]
    y = [find_Queen[1], find_myKing[1], find_OtherKing[1]]
    colors = np.array(["red", "green", "blue"])

    plt.xlim(0, 8)
    plt.ylim(0, 8)  

    plt.scatter(np.array(x) + 0.5, np.array(y) + 0.5, c=colors)
    plt.grid(True)

    plt.show()