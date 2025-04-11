# Time Complexity : O(n), where n is the number of nodes in the tree
# Space Complexity : 2*O(h) + couple extra nodes which will be present in the queue while traversing the tree
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach:
# We will use BFS to traverse the tree level by level.
# At each level we will check if the two nodes x and y are present.
# To do this we will maintain 2 queues to keep track of the nodes as well as their parents at the current level.
# If we find a node, we will set a flag to True and store the parent and level of that node.
# Finally we will check if both nodes are found and if they are at the same level but have different parents.
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root, x: int, y: int):
        # Initialize two queues, 1 for the nodes and 1 for the parents
        q, q_parent = deque(), deque()
        # If the root is present, add it to the queue
        # Also add None as the parent of the root
        if root:
            q.append(root)
            q_parent.append(None)
        # Initialize flags to check if the nodes are found
        found_x = found_y = False
        level = -1

        # Perform BFS
        while q:
            # Take a snapshot of the current level. We will process all the nodes at this level in 1 iteration
            size = len(q)
            # Increment the level
            level += 1
            for i in range(size):
                # Pop the first node from the queue
                node = q.popleft()
                # Pop the first parent from the queue
                node_parent = q_parent.popleft()
                
                # Check if the node is one of the nodes we are looking for
                # If we find a node, we will set the flag to True and store the parent and level of that node
                if node.val == x:
                    found_x = True
                    x_parent = node_parent
                    x_level = level
                if node.val == y:
                    found_y = True
                    y_parent = node_parent
                    y_level = level

                # We will add the left and right children of the node to the queue
                # Also add the current node as the parent of the left and right children
                if node.left:
                    q.append(node.left)
                    q_parent.append(node)
                if node.right:
                    q.append(node.right)
                    q_parent.append(node)

        # After processing all the nodes at this level, we will check if both nodes are found
        if not found_x or not found_y:
            return False
        # If both nodes are found, we will check if they are at the same level but have different parents and return the result
        else:
            return x_parent != y_parent and x_level == y_level