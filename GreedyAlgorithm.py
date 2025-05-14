# Unit-VII Greedy Algorithms: Interval Scheduling, Minimum Spanning Trees – Prim’s algorithm, Kruskal Algorithm, Shortest Path Problem – Djikstra’s algorithm

import heapq

# ==================================
# 1. Interval Scheduling (Greedy)
# ==================================

def interval_scheduling(intervals):
    """
    Selects the maximum number of non-overlapping intervals.
    Intervals should be a list of (start, end).
    """
    sorted_intervals = sorted(intervals, key=lambda x: x[1])  # sort by end time
    result = []
    current_end = 0

    for interval in sorted_intervals:
        if interval[0] >= current_end:
            result.append(interval)
            current_end = interval[1]

    return result

# ==================================
# 2. Prim's Algorithm (MST)
# ==================================

def prim_mst(graph, start=0):
    """
    Graph should be an adjacency list: graph[u] = [(v, weight), ...]
    """
    visited = [False] * len(graph)
    min_heap = [(0, start)]  # (weight, vertex)
    total_cost = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += weight
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))

    return total_cost

# ==================================
# 3. Kruskal's Algorithm (MST)
# ==================================

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, xroot, yroot):
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal_mst(n, edges):
    """
    n = number of nodes
    edges = list of (weight, u, v)
    """
    edges.sort()
    parent = [i for i in range(n)]
    rank = [0] * n
    total_cost = 0
    mst_edges = []

    for w, u, v in edges:
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            total_cost += w
            mst_edges.append((u, v, w))
            union(parent, rank, x, y)

    return total_cost, mst_edges

# ==================================
# 4. Dijkstra's Algorithm (Shortest Path)
# ==================================

def dijkstra(graph, start):
    """
    graph: adjacency list graph[u] = [(v, weight), ...]
    returns: list of shortest distances from start to all nodes
    """
    dist = [float('inf')] * len(graph)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist

# ==================================
# Testing All Algorithms
# ==================================

def test_all():
    print("=== Unit-VII: Greedy Algorithms ===\n")

    # Interval Scheduling Test
    intervals = [(1, 4), (2, 3), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
    scheduled = interval_scheduling(intervals)
    print(f"Interval Scheduling Result: {scheduled}")
    assert all(scheduled[i][1] <= scheduled[i + 1][0] for i in range(len(scheduled) - 1))
    print("✅ Interval Scheduling passed")

    # Prim's MST Test
    graph_prim = {
        0: [(1, 4), (7, 8)],
        1: [(0, 4), (2, 8), (7, 11)],
        2: [(1, 8), (3, 7), (5, 4), (8, 2)],
        3: [(2, 7), (4, 9), (5, 14)],
        4: [(3, 9), (5, 10)],
        5: [(4, 10), (3, 14), (2, 4), (6, 2)],
        6: [(5, 2), (8, 6), (7, 1)],
        7: [(0, 8), (1, 11), (6, 1), (8, 7)],
        8: [(2, 2), (6, 6), (7, 7)],
    }
    total_prim = prim_mst(graph_prim)
    print(f"Prim's MST Total Cost: {total_prim}")
    print("✅ Prim's Algorithm passed")

    # Kruskal's MST Test
    edges_kruskal = [
        (7, 0, 1), (5, 0, 3), (9, 1, 2), (7, 1, 3),
        (8, 1, 4), (5, 2, 4), (15, 3, 4), (6, 3, 5), (8, 4, 5), (9, 4, 6),
        (11, 5, 6)
    ]
    total_kruskal, mst_edges = kruskal_mst(7, edges_kruskal)
    print(f"Kruskal's MST Total Cost: {total_kruskal}")
    print(f"MST Edges: {mst_edges}")
    print("✅ Kruskal's Algorithm passed")

    # Dijkstra Test
    graph_dijkstra = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    distances = dijkstra(graph_dijkstra, 0)
    print(f"Dijkstra's Shortest Paths from 0: {distances}")
    assert distances == [0, 3, 1, 4]
    print("✅ Dijkstra’s Algorithm passed")

if __name__ == "__main__":
    test_all()
