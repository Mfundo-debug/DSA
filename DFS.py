""" 
Depth First Search:
One of the Graph search algorithms
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
                self.DFS(neighbour, visited)
                
g = Graph([[], [2,3], [1,4], [1,4], [2,4]])
visited = [False]*(len(g.graph))
g.DFS(0, visited)