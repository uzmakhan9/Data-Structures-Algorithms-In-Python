# Creating a Node Class
class node:
    def __init__(self,val):
        self.childleft=None
        self.childright=None
        self.nodedata=val

# Creating an instance of the node class to construct the tree
root=node(1)
root.childleft=node(2)
root.childright=node(3)
root.childleft.childleft=node(4)
root.childleft.childright=node(5)

# creating inorder,preorder,postorder functions using recursion
def inorder(root1):
    if root1:
        inorder(root1.childleft)
        print(root1.nodedata)
        inorder(root1.childright)
print("inorder")
inorder(root)

def preorder(root2):
    if root2:
        print(root2.nodedata)
        preorder(root2.childleft)
        preorder(root2.childright)
print("preorder")
preorder(root)

def postorder(root3):
    if root3:
        postorder(root3.childleft)
        postorder(root3.childright)
        print(root3.nodedata)
print("postorder")
postorder(root)