"""
Graph Data Structure for Freshers
================================
A graph is a collection of nodes (vertices) connected by edges.

Real-life examples:
- Social media friends
- Cities connected by roads
- Internet links
- Network connections

Important terms:
1. Vertex / Node: a point in the graph
2. Edge: connection between two nodes
3. Undirected graph: A -- B means both ways
4. Directed graph: A -> B means only one direction
5. Weighted graph: edges have cost or distance
6. Unweighted graph: edges have no cost

Graph representation in Python:
- Adjacency list (easy and commonly used)
- Adjacency matrix (2D list)
This example uses adjacency list.

class Graph:
    def __init__(self):
        self.graph = {}
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    def add_edge(self, u, v, directed=False):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)

    def remove_edge(self, u, v, directed=False):
        if u in self.graph and v in self.graph:
            if v in self.graph[u]:
                self.graph[u].remove(v)
            if not directed and u in self.graph[v]:
                self.graph[v].remove(u)

    def remove_vertex(self, vertex):
        if vertex not in self.graph:
            return

        del self.graph[vertex]

        for key in self.graph:
            if vertex in self.graph[key]:
                self.graph[key].remove(vertex)

    def remove(self, vertex):
        self.remove_vertex(vertex)

    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

    def bfs(self, start):
        Breadth-First Search: visit level by level.
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            current = queue.pop(0)
            print(current, end=" ")
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()
    def dfs(self, start, visited=None):
        #Depth-First Search: go deep before going wide.
        if visited is None:
            visited = set()
        if start in visited:
            return
        visited.add(start)
        print(start, end=" ")
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
        print()
# Example graph
G = Graph()
# Vertices
for vertex in ["A", "B", "C", "D", "E"]:
    G.add_vertex(vertex)
G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("B", "D")
G.add_edge("C", "E")
G.add_edge("D", "E")
print("Graph adjacency list:")
G.display()

print("\nRemove vertex B:")
G.remove("B")
G.display()

print("\nBFS from A:")
G.bfs("A")

print("\nDFS from A:")
G.dfs("A")

Interview-friendly explanation:

- BFS uses queue and is useful for shortest path in unweighted graphs.
- DFS uses stack (or recursion) and is useful for cycle detection and connected components.
- Time complexity for BFS/DFS on adjacency list: O(V + E)
- Space complexity: O(V)

Note:
- Graphs are used in many advanced problems like shortest path, connectivity, topological sorting, etc.
""

def fib(a, b):
    if a <= 1:
        return a
    if b[a] != -1:
        return b[a]
    b[a] = fib(a-1, b) + fib(a-2, b)
    return b[a]
n = 6
b = [-1] * (n + 1)
print(fib(n, b))
"""
def fib(n):
    dp=[0]*(n+1)
    dp[0]=0
    if n>=1:
        dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
a=10
print(fib(a))



















































