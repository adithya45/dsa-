class Stack:
    def __init__(self):  # Corrected initialization method name
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

def dfs(graph, start):
    visited = []
    stack = Stack()
    stack.push(start)
    while not stack.is_empty():
        current_node = stack.pop()
        if current_node and current_node not in visited:
            print(current_node, end=" ")
            visited.append(current_node)
            neighbors = graph[current_node]  if current_node in graph else []
            for i in neighbors:
                if i not in visited:
                    stack.push(i)
                    
graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'F'],
    'D': ['A', 'E', 'G'],
    'E': ['B', 'A', 'G'],
    'F': ['C'],
    'G': ['D', 'E', 'H'],
    'H': ['G', 'I'],
    'I': ['H']
}

print("DFS Traversal:")
dfs(graph,'A')