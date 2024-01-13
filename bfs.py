class Queue:
   def _init_(self):
     self.items = []
   def enqueue(self, item):
     self.items.append(item)
   def dequeue(self):
      return self.items.pop(0)
   def is_empty(self):
     return len(self.items) == 0
def bfs(graph, start):
  visited = []
  queue = Queue()
  queue.enqueue(start)
  while not queue.is_empty():
    current_node = queue.dequeue()
    if current_node not in visited:
      print(current_node, end=" ")
      visited.append(current_node)
      neighbors = graph[current_node]
      for i in neighbors:
          if i not in visited:
            queue.enqueue(i)
graph = {
'A': ['B', 'D','E'],
'B': ['A', 'C', 'E'],
'C': ['B', 'F'],
'D': ['A','E','G'],

'E': ['B', 'A','G'], 'F': ['C'],
'G': ['D','E','H'],
'H': ['G','I'], 'I': ['H']
}
print("BFS Traversal:")
bfs(graph, 'A')