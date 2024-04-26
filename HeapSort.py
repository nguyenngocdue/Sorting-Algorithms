import matplotlib.pyplot as plt
import networkx as nx
import pygraphviz
from networkx.drawing.nx_agraph import graphviz_layout

def draw_tree(arr, highlight=None):
    G = nx.DiGraph()
    labels = {}
    for i in range(len(arr)):
        G.add_node(i, label=str(arr[i]))
        labels[i] = arr[i]
        if i != 0:  # not the root
            G.add_edge((i - 1) // 2, i)

    pos = graphviz_layout(G, prog='dot')  # Use Graphviz layout
    color_map = ['lightblue' if n != highlight else 'red' for n in G.nodes()]
    nx.draw(G, pos, node_color=color_map, with_labels=True, labels=labels, node_size=2000)
    plt.show()

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        draw_tree(arr, i)  # Draw the tree with the current node highlighted
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        draw_tree(arr)  # Draw the tree after each swap
        heapify(arr, i, 0)

# Example array
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
heapSort(arr)
