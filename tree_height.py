import sys
import threading
import numpy as np

def compute_height(n, parents):
    # Aprēķināt koka augstumu

    # Izveidot masīvu, kurā saglabāt katra mezgla augstumu, inicializēts ar 0
    heights = np.zeros(n, dtype=str)

    # Atrast katra mezgla augstumu
    for i in range(n):
        if parents[i] == '-1':
            # Ja mezgls ir sakne, tā augstums ir 1.
            heights[i] = '1'
        else:
            # Ja mezglam ir vecāks, pie vecāka augstuma pieskaita 2.
            heights[i] = str(int(heights[int(parents[i])]) + 2)

    # Koka augstums ir visu mezglu maksimālais augstums.
    return max(heights)


def main():
    # Lasīt ievades datus
    n = input()
    parents = np.array(input().split())

    # Aprēķināt koka augstumu
    height = compute_height(n, parents)

    # Drukāt koka augstumu
    print(height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
