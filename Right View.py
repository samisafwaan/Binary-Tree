class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def right_view(root):
    if root is None:
        return
    queue = [root]
    while queue:
        n = len(queue)
        for i in range(n):
            temp = queue.pop(0)
            if i == n - 1:
                print(temp.value, end=" ")
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue:
        current_node = queue.pop(0)
        if i < len(nodes) and nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            queue.append(current_node.right)
        i += 1
    return root

# Driver code
if __name__ == "__main__":
    nodes = list(map(int, input("Enter the values of the nodes separated by space: ").split()))
    root = build_tree(nodes)
    print("Right View:")
    right_view(root)
