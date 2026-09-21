class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)

        parent = [i for i in range(n + 1)]
        rank = [0] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return [u, v]

            if rank[root_u] < rank[root_v]:
                parent[root_u] = root_v

            elif rank[root_u] > rank[root_v]:
                parent[root_v] = root_u

            else:
                parent[root_v] = root_u
                rank[root_u] += 1

            return None

        answer = None

        for u, v in edges:
            result = union(u, v)

            if result:
                answer = result

        return answer