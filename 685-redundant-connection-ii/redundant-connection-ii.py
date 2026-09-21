class Solution:
    def findRedundantDirectedConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)

        parent = [i for i in range(n + 1)]

        node_parent = [0] * (n + 1)

        first_edge = None
        second_edge = None

        for u, v in edges:
            if node_parent[v] == 0:
                node_parent[v] = u

            else:
                first_edge = [node_parent[v], v]
                second_edge = [u, v]

        # DSU find
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # DSU union
        def union(u, v):

            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return [u,v]

            parent[root_v] = root_u
            return None

        for u, v in edges:
            if second_edge == [u, v]:
                continue

            edge = union(u,v)

            if edge is not None:
                if first_edge is not None:
                    return first_edge
                return edge

        return second_edge
        