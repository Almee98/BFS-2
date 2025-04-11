# Time Complexity : O(n), where n is the number of nodes in the tree
# Space Complexity : O(h) + couple extra nodes which will be present in the queue while traversing the tree
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach:
# We will use BFS to traverse the tree level by level.
# We will maintain a queue to keep track of the nodes at the current level.
# For each level, we will add the last node of that level to the result list, giving us the rightmost node.
# We will also keep track of the size of the queue at each level to know when we have reached the last node.

# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):
        # Initialize a queue to perform BFS
        q = deque()
        # If the root is not None, add it to the queue
        if root: q.append(root)
        # Initialize a list to store the result
        res = []

        # Perform BFS
        while q:
            # Take a snapshot of the current level. We will process all the nodes at this level in 1 iteration
            size = len(q)
            for i in range(size):
                # Pop the first node from the queue
                node = q.popleft()
                # We will add the left and right children of the node to the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # After processing all the nodes at this level, we will add the last node to the result list
            # The last node in the queue will be the rightmost node at this level
            res.append(node.val)
        # After processing all the nodes in the queue, the resultant list will contain the rightmost nodes at each level
        return res
    
# Approach:
# We will use DFS to traverse the tree.
# We will do a pre-order traversal of the tree - root-right-left
# We will maintain a list to store the result, and keep track of the current level.
# If we are at a new level, we will add the node to the result list. This will ensure that we only add the rightmost node at each level.

# Time Complexity : O(n), where n is the number of nodes in the tree
# Space Complexity : O(h), where h is the height of the tree

class Solution:
    def rightSideView(self, root):
        # Initialize a list to store the result
        res = []
        # Perform DFS
        def dfs(node, level):
            # If the node is null, it means we have reached a leaf node, so we return
            if not node:
                return

            # If we are at a new level, we will add the node to the result list
            # This will ensure that we only add the rightmost node at each level, and don't add any duplicates
            if len(res) == level:
                res.append(node.val)

            # We will do a pre-order traversal of the tree - root-right-left
            dfs(node.right, level+1)
            dfs(node.left, level+1)

        dfs(root, 0)
        # After processing all the nodes in the tree, the resultant list will contain the rightmost nodes at each level
        # We will return the resultant list
        return res
    
# Approach:
# We will use DFS to traverse the tree.
# The approcah is similar to the previous one, but we will use a different approach of traversal.
# We will do a pre-order traversal of the tree - root-left-right
# This means that we will start storing the leftmost node at each level first, so we will have to keep updating the result list with the rightmost node at each level.
# TC and SC will be the same as the previous approach.
class Solution:
    def rightSideView(self, root):
        # Initialize a list to store the result
        res = []

        # Perform DFS
        def dfs(node, level):
            # If the node is null, it means we have reached a leaf node, so we return
            if not node:
                return

            # If we are at a new level, we will add the node to the result list
            if len(res) == level:
                res.append(node.val)
            # Else, we have already visited this leavel, so we will update the result list with the rightmost node at this level
            else:
                res[level] = node.val

            # We will do a pre-order traversal of the tree - root-left-right
            dfs(node.left, level+1)
            dfs(node.right, level+1)

        dfs(root, 0)
        # After processing all the nodes in the tree, the resultant list will contain the rightmost nodes at each level
        # We will return the resultant list
        return res