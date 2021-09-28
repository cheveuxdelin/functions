def dijkstra(g, s):
    from sys import maxsize as inf
    from queue import PriorityQueue

    #number of nodes
    n = len(g)
    #distances
    d = [inf] * n
    #self distance
    d[s] = 0 
    #visited
    visited = [False] * n
    #priority queue
    pq = PriorityQueue()
    #putting first node
    pq.put((0, s))
    while not pq.empty():
        #getting distance to self and current node
        (distance, v) = pq.get()
        #visiting
        visited[v] = True
        #checking adyacencies
        for i in range(n):
            #distance to self + distance to neighbor
            newcost = distance + g[v][i]
            if g[v][i] != -1 and visited[i] == False and  newcost < d[i]:
                pq.put((newcost, i))
                d[i] = newcost
    return d

def KMP(text, pattern):
    table = [0] * len(pattern)
    i = 1
    j = 0
    
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            table[i] = j + 1
            i += 1
            j += 1
        elif j != 0:
            j = table[j - 1]
        else:
            i += 1
            
    i = 0
    j = 0
    while i < len(text) and j < len(pattern):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        elif j != 0:
            j = table[j - 1]
        else:
            i += 1
        
    if j == len(pattern):
        return i - j
    else:
        return -1
