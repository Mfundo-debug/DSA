"""
Version 3 of DFS,
in this case  counts number of visits
"""
class Graph:
    def __init__(self,graph):
        self.graph = graph 
        self.V = len(graph)

    def DFS(self,v,visited, count):
        visited[v] = True
        count += 1
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                count = self.DFS(neighbour,visited,count)
        return count

graph = input("Enter the graph:")
graph = [list(map(int, x.split())) for x in graph.split('\n')]
visited = [False]*(len(graph))
g = Graph(graph)
start = int(input("Enter the starting vertex:"))
count = 0
print("Number of visits:",g.DFS(start,visited,count))
