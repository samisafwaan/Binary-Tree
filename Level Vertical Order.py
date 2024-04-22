class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def level_order(root):
    queue = [root]
    while len(queue) > 0:
        l = []
        for _ in range(len(queue)):
            element = queue.pop(0)
            print(element.data, end=" ")
            l.append(element)
        print()
        for i in l:
            if i.left:
                queue.append(i.left)
            if i.right:
                queue.append(i.right)

def vertical_order(root):
    if not root:
        return
    vertical_order_dict = {}
    queue = [(root, 0)]
    while queue:
        node, hd = queue.pop(0)
        if hd not in vertical_order_dict:
            vertical_order_dict[hd] = []
        
        vertical_order_dict[hd].append(node.data)
        
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    
    for key in sorted(vertical_order_dict):
        for data in vertical_order_dict[key]:
            print(data, end=" ")
        print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Level Order Traversal:")
level_order(root)

print("\nVertical Order Traversal:")
vertical_order(root)
    
            
