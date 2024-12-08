# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict, deque



        
        #1_ firt step , convert binary tree into a graph:
        
        
        graph = defaultdict(list)
        
        def buildGraph(node, parent = None):
            if not node:
                return None
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            if node.left:
                buildGraph(node.left, node)
            if node.right:
                buildGraph(node.right, node)
                
                
        buildGraph(root)
        
        #2nd step , do the BFS :
        
        queue = deque([(target.val, 0)])
        visited = set([target.val])
        result = []
        
        
        
        while queue :
            node, dist = queue.popleft()
            
            if dist == k:
                result.append(node)
            elif dist <=k:
                for neighbor in graph[node]:
                    if neighbor in visited:
                        node = neighbor
                    else:
                        visited.add(neighbor)
                        queue.append((neighbor, dist+1))
        return result