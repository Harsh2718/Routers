# Class used to implement the graph data structure
class Graph:
    # Attributes
    # Graph- used to store the graph
    # Visited - to check if a node is visited
    # size - size of the graph
    def __init__(self,n):
        self.visited = [False]*n
        self.graph = [None]*n
        self.size =n
    def add_edge(self,edge):
        u = edge[0]
        v = edge[1]
        c = edge[2]
        if(self.graph[u]==None):
            self.graph[u]={v:c}
        elif(v in self.graph[u]) and self.graph[u][v]<c:
            self.graph[u][v]=c
        elif(self.graph[u] is not None):
            self.graph[u][v]=c
        if(self.graph[v]==None):
            self.graph[v]={u:c}
        elif(u in self.graph[v]) and self.graph[v][u]<c:
            self.graph[v][u]=c
        elif(self.graph[v] is not None):
            self.graph[v][u]=c
    def print_graph(self):
        return self.graph
# Class used to implement heap data structure which will be used to find the best possible path with max capacity
class MaxHeap:
# Attributes
# Heap- used to store the heap elements
# Size - the size of the heap
#pos_heap - the position of vertex in the heap
#cap- best capacity through which a vertex can be reached
    def __init__(self,n):
        self.heap = []
        self.size =0
        self.pos_heap = [None]*n
        self.cap=[0]*n
    def swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]
        self.pos_heap[self.heap[j][0]] = j
        self.pos_heap[self.heap[i][0]] = i
    def heap_up(self,i):
        p = int((i-1)/2)
        if p >=0:
            if (self.heap[p][1]<self.heap[i][1]):
                self.swap(p,i)
                self.heap_up(p)
    def heap_down(self,i):
        left = 2*i +1 
        right = 2*i+2
        larger = left
        if left >= self.size:
            return
        elif right>= self.size:
            larger = left
        else:
            if(self.heap[right][1]>self.heap[left][1]):
                larger = right
        if self.heap[larger][1] > self.heap[i][1]:
            self.swap(i,larger)
            self.heap_down(larger)
    def insert(self,key):
        self.heap.append(key)
        self.cap[key[0]] = key[1]
        self.pos_heap[key[0]] = self.size
        self.size+=1
        self.heap_up(self.size-1)
    def extract_root(self):
        self.swap(0,self.size-1)
        self.pos_heap[self.heap[self.size-1][0]] = None 
        x=self.heap.pop()
        self.size-=1
        if self.size > 0:
            self.heap_down(0)
        return x
    def change_key(self,key):
        pos = self.pos_heap[key[0]]
        x = self.heap[pos]
        self.heap[pos] = key
        self.cap[key[0]] = key[1]
        if key[1] > x[1]:
            self.heap_up(pos)
        elif key[1] < x[1] :
            self.heap_down(pos)
    def is_Empty(self):
        return self.size ==0
    def print_heap(self):
        return self.heap,self.pos_heap
#Main function to find the best possible path and capacity

def findMaxCapacity(n,links,s,t):
    route =[]       #Stores the path
    Cap = 0         # stores the capacity
    prev=[None]*n   #Stores the previously visited node in the path as done in BFT/BFS
    router = Graph(n)   #graph object
    for i in links:
        router.add_edge(i)
    heap = MaxHeap(n)   #Heap object
    heap.insert((s,float('inf')))
    while(not heap.is_Empty() or router.visited[t]==False):
        (x,c) = heap.extract_root()
        router.visited[x] = True
        if x==t:
            Cap=c
            break
        for j,k in router.graph[x].items():  
            if heap.pos_heap[j] is None and router.visited[j]==False:
                mini = min(c,k)
                heap.insert((j,mini))
                prev[j] = x 
            elif heap.pos_heap[j] is not None and router.visited[j] == False:
                mini = min(c,k)
                curr = heap.cap[j]
                if mini > curr:
                    heap.change_key((j,mini))
                    prev[j] = x
    route.append(t)
    k=t
    while prev[k] is not None:
        route.append(prev[k])
        k = prev[k]
    route.reverse()
    return Cap,route
print(findMaxCapacity(1,[],0,0))



            

            
        