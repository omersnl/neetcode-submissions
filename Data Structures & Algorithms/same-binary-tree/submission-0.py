# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        qp = deque([p])
        qq = deque([q])

        while qp and qq:
            for _ in range(len(qp)):
                node_p = qp.popleft()
                node_q = qq.popleft()

                if node_p is None and node_q is None:
                    continue
                if node_p is None or node_q is None or node_p.val != node_q.val:
                    return False
                
                qp.append(node_p.left)
                qp.append(node_p.right)
                qq.append(node_q.left)
                qq.append(node_q.right)
        
        return True
