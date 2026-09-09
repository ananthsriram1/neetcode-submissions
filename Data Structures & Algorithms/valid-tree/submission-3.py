from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edges.sort()
        adj_matrix = defaultdict(list)        

        for parent, child in edges:
            adj_matrix[parent].append(child)
            adj_matrix[child].append(parent)

        queue = deque()
        queue.append(0)
        visited = set()

        while len(queue) > 0:            
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr in visited:
                    return False
                visited.add(curr)

                for neighbor in adj_matrix[curr]:
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)


        if len(visited) != n:
            return False

        return True   