class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
        self.hd=0
        self.level=0
def level_vertical_order(root,order):
    result_H={}
    result_V={}
    q=[(root,0,0)]
    while q:
        node,hd,lvl=q.pop(0)
        if lvl not in result_H:
            result_H[lvl]=[]
        if hd not in result_V:
            result_V[hd]=[]
        result_V[hd].append(node.data)
        result_H[lvl].append(node.data)
        if node.left:
            node.left.level=lvl+1
            node.left.hd=hd-1
            q.append((node.left,hd-1,lvl+1))
        if node.right:
            node.right.level=lvl+1
            node.right.hd=hd+1
            q.append((node.right,hd+1,lvl+1))
    if order=='H':
        for lvl in sorted(result_H.keys(),reverse=True):
            print(result_H[lvl],end=",")
    if order=='V':
        for hd in sorted(result_V.keys(),reverse=True):
            print(result_V[hd],end=",")
       
       

#driver code
root=Node(2)
root.left=Node(7)
root.right=Node(5)
root.left.left=Node(2)
root.left.right=Node(6)
root.left.right.left=Node(5)
root.left.right.right=Node(11)
root.right.right=Node(9)
root.right.right.left=Node(4)
print("\nLevel order traversal/Horizontal traversal : ")
level_vertical_order(root,'H')
print("\nVertical traversal : ")
level_vertical_order(root,'V')
