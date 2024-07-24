# In this input format, the input will be a 2D array. Each element of the array will be in the form [x, y], which indicates that there is an edge between x and y. The problem may have a story for these edges - using the cities example, the story would be something like "[x, y] means there is a highway connecting city x and city y"

edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [1, 4],
    [2, 5],
    [3, 6],
    [3, 7],
    [4, 7],
    [5, 8],
    [6, 9],
    [7, 10],
    [8, 11],
    [9, 11],
    [10, 11],
    [2, 4],
    [4, 8]
]

# To simplify the edges input we can create a HashMap based on the edges
from collections import defaultdict
def build_graph(edges):
    graph=defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        # uncomment the following line in the graph is undirected
        # graph[y].append(x)
    
    return graph

graph=build_graph(edges)

print(graph)