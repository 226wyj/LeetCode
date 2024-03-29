from typing import List
from collections import defaultdict, deque


class Solution:
    """ DFS """
    def get_adj(self, edges):
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        return adj

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 1

        adj = self.get_adj(edges)
        vertexes = list(range(n))
        visited = set()
        count = 0

        def dfs(vertex, visited):
            visited.add(vertex)
            for adj_vertex in adj[vertex]:
                if not adj_vertex in visited:
                    dfs(adj_vertex, visited)

        for vertex in vertexes:
            if vertex not in visited:
                dfs(vertex, visited)
                count += 1

        return count


class Solution:
    """ BFS """
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def get_graph(edges):
            graph = defaultdict(list)
            for edge in edges:
                graph[edge[0]].append(edge[1])
                graph[edge[1]].append(edge[0])
            return graph

        def bfs(graph, node, visited):
            queue = deque([node])
            while queue:
                length = len(queue)
                for _ in range(length):
                    n = queue.popleft()
                    visited.add(n)
                    for adj in graph[n]:
                        if adj not in visited:
                            queue.append(adj)

        graph = get_graph(edges)
        visited = set()
        res = 0
        for node in range(n):
            if node not in visited:
                bfs(graph, node, visited)
                res += 1
        return res


# 并查集解法
class UnionFind(object):
    def __init__(self, count):
        self.count = count
        self.parent = [0] * count
        for i in range(count):
            self.parent[i] = i
    
    def _find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, p, q):
        root_p, root_q = self._find(p), self._find(q)
        if root_p == root_q:
            return
        self.parent[root_p] = root_q
        self.count -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 并查集
        # T: O(N)
        # S: O(N)
        uf = UnionFind(n)
        for p, q in edges:
            uf.union(p, q)
        return uf.count
