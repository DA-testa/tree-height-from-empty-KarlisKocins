# python3
#Autors Kārlis Kociņš 16.Grupa
import sys
import threading
import numpy as np

def compute_height(n, parents):
    # Convert parents array to numpy array for easy indexing
    parents = np.array(parents)

    # Initialize an array to store the depth of each node
    depths = np.zeros(n, dtype=int)

    # Define a helper function to recursively compute the depth of each node
    def compute_depth(node):
        # If this node's depth has already been computed, return it
        if depths[node] != 0:
            return depths[node]

        # Compute the depth of the parent node recursively
        if parents[node] == -1:
            depths[node] = 1
        else:
            depths[node] = 1 + compute_depth(parents[node])

        return depths[node]

    # Compute the depth of each node
    for i in range(n):
        compute_depth(i)

    # Return the maximum depth
    return np.max(depths)

def main():
    choice = input("F or I: ")

    if "I" in choice or "i" in choice:
        # Lasīt ievades datus
        n = int(input("Count: "))
        parents = list(map(int, input("Nodes: ").split()))
        # Aprēķināt koka augstumu
        height = compute_height(n, parents)

    elif "F" in choice or "f" in choice:
        test_numurs = input("Ievadi testa numuru no 1 - 25: ")
        with open(f"test/{test_numurs}", "r") as file:
            n = int(file.readline().strip())
            parents = list(map(int, file.readline().strip().split()))
            height = compute_height(n, parents)

    # Drukāt koka augstumu
    print(height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
