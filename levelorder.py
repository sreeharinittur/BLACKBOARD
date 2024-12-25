import collections
class TreeNode:
    def __init__(self,val,left,right):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def levelorder(self,root:TreeNode):
        res=[]
        q=collections.deque()
        q.append(root)
        while q:
            qlen=len(q)
            level=[]
            for i in range(qlen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
t=TreeNode(2,None,None)
t1=TreeNode(1,None,None)
t2=TreeNode(3,None,None)
t3=TreeNode(4,None,None)
t4=TreeNode(5,None,None)
t.left=t1
t.right=t2
t2.right=t3
t3.right=t4
s=Solution()
print(s.levelorder(t))

        