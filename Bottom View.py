class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.hd = 0

def bottom_view(root):
    if root is None:
        return
    queue = []
    hd_dict = {}
    root.hd = 0
    queue.append(root)
    while queue:
        temp = queue.pop(0)
        hd = temp.hd
        hd_dict[hd] = temp.value
        if temp.left:
            temp.left.hd = hd - 1
            queue.append(temp.left)
        if temp.right:
            temp.right.hd = hd + 1
            queue.append(temp.right)
    for key in sorted(hd_dict.keys()):
        print(hd_dict[key], end=" ")

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
    print("Bottom View:")
    bottom_view(root)
