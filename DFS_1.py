"""
Version 2, allows the user to enter values, and the starting vertex

"""
class Graph:
    def __init__(self,graph):
        self.graph = graph 
        self.V = len(graph)

    def DFS(self,v,visited):
        visited[v] = True
        print(v)
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                self.DFS(neighbour,visited)

graph = input("Enter the graph:")
graph = [list(map(int, x.split())) for x in graph.split('\n')]
visited = [False]*(len(graph))
g = Graph(graph)
start = int(input("Enter the starting vertex:"))
g.DFS(start,visited)
