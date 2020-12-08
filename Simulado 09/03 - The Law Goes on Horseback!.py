from pprint import pprint

class Vertice:
    def __init__(self):
        self.edges = set()
        self.searched = False


def get_max(policemen_horses, horse_capacity, n = 0):
    if n >= len(policemen_horses):
        return 0
    
    max_num = 0

    for horse in policemen_horses[n]:
        if horse_capacity[horse] > 0:
            horse_capacity[horse] -= 1
            max_num = max(max_num, 1 + get_max(policemen_horses, horse_capacity, n + 1))
            horse_capacity[horse] += 1
    
    max_num = max(max_num, 1 + get_max(policemen_horses, horse_capacity, n + 1))

    return max_num

class Graph: 
   
    def __init__(self,graph): 
        self.graph = graph # residual graph 
        self. ROW = len(graph) 
        #self.COL = len(gr[0]) 
          
   
    '''Returns true if there is a path from source 's' to sink 't' in 
    residual graph. Also fills parent[] to store the path '''
    def BFS(self,s, t, parent): 
  
        # Mark all the vertices as not visited 
        visited =[False]*(self.ROW) 
          
        # Create a queue for BFS 
        queue=[] 
          
        # Mark the source node as visited and enqueue it 
        queue.append(s) 
        visited[s] = True
           
         # Standard BFS Loop 
        while queue: 
  
            #Dequeue a vertex from queue and print it 
            u = queue.pop(0) 
          
            # Get all adjacent vertices of the dequeued vertex u 
            # If a adjacent has not been visited, then mark it 
            # visited and enqueue it 
            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 
  
        # If we reached sink in BFS starting from source, then return 
        # true, else false 
        return True if visited[t] else False
              
      
    # Returns tne maximum flow from s to t in the given graph 
    def FordFulkerson(self, source, sink): 
  
        # This array is filled by BFS and to store path 
        parent = [-1]*(self.ROW) 
  
        max_flow = 0 # There is no flow initially 
  
        # Augment the flow while there is path from source to sink 
        while self.BFS(source, sink, parent) : 
  
            # Find minimum residual capacity of the edges along the 
            # path filled by BFS. Or we can say find the maximum flow 
            # through the path found. 
            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
  
            # Add path flow to overall flow 
            max_flow +=  path_flow 
  
            # update residual capacities of the edges and reverse edges 
            # along the path 
            v = sink 
            while(v !=  source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 
  
        return max_flow 

def main(instancia):
    n, m, k = [int(x) for x in input().split()]

    graph = [[0 for _ in range(1 + n + m + 1)] for _ in range(1 + n + m + 1)]

    for soldier in range(m):
        graph[0][1 + soldier] = 1

    capacities = [int(x) for x in input().split()]
    for horse in range(n):
        graph[1 + m + horse][-1] = capacities[horse]

    for _ in range(k):
        horse, soldier = [int(x) - 1 for x in input().split()]
        graph[1 + soldier][1 + m + horse] = 1

    #pprint(graph)
    g = Graph(graph) 
  
    source = 0
    sink = len(graph) - 1

    print('Instancia %d' % instancia)
    print(g.FordFulkerson(source, sink))
    print()

try:
    instancia = 1
    while True:
        main(instancia)
        instancia += 1
except EOFError:
    pass