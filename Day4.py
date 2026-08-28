'''class TreeNode:
    def __init__(self,data):
        self.val=data
        self.children=[]

class Tree:
    def __init__(self):
        self.root=None

    def add(self,data,parent=None):
        new=TreeNode(data)

        if self.root is None:
            self.root=new
            return

        parent=self.find(self.root,parent)
        parent.children.append(new)

    def find(self,current,data):
        if current.val==data:
            return current

        for child in current.children:
            found=self.find(child,data)
            if found:
                return found

        return None

    def findParent(self,current,data):
        for child in current.children:
            if child.val==data:
                return current

            found=self.findParent(child,data)

            if found:
                return found

        return None
    def display(self,current,depth=0):
        print("  "*depth,current.val)

        for child in current.children:
            self.display(child,depth+1)


tree=Tree()

tree.add(10)
tree.add(20,10)
tree.add(30,10)
tree.add(40,20)
print(tree.findParent(tree.root,40).val)


tree.display(tree.root)''
class BinaryTreeNode:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None


class BinaryTree:
    def __init__(self):
        self.root=None

    def add(self,data):
        new=BinaryTreeNode(data)

        if self.root is None:
            self.root=new
            return

        self.recursiveAdd(self.root,new)

    def recursiveAdd(self,current,new):
        if current.left is None:
            current.left=new
            return

        if current.right is None:
            current.right=new
            return

        self.recursiveAdd(current.left,new)
        self.recursiveAdd(current.right,new)
    def preorder(self,current):
        if current is None:
            return

        print(current.val,end=" ")
        self.preorder(current.left)
        self.preorder(current.right)

    def inorder(self,current):
        if current is None:
            return

        self.inorder(current.left)
        print(current.val,end=" ")
        self.inorder(current.right)

    def postorder(self,current):
        if current is None:
            return

        self.postorder(current.left)
        self.postorder(current.right)
        print(current.val,end=" ")

    def display(self,current,depth=0):
        if current is None:
            return

        print("  "*depth,current.val)
        self.display(current.left,depth+1)
        self.display(current.right,depth+1)

    def findMin(self,current):
        if current is None:
            return None

        minimum=current.val

        left_min=self.findMin(current.left)
        right_min=self.findMin(current.right)

        if left_min is not None and left_min < minimum:
            minimum=left_min

        if right_min is not None and right_min < minimum:
            minimum=right_min

        return minimum

    def findMax(self,current):
        if current is None:
            return None

        maximum=current.val

        left_max=self.findMax(current.left)
        right_max=self.findMax(current.right)

        if left_max is not None and left_max > maximum:
            maximum=left_max

        if right_max is not None and right_max > maximum:
            maximum=right_max

        return maximum


tree=BinaryTree()

tree.add(10)
tree.add(20)
tree.add(5)
tree.add(40)
tree.add(2)
tree.add(30)

print("Tree:")
tree.display(tree.root)

print("\nPreorder:")
tree.preorder(tree.root)

print("\nInorder:")
tree.inorder(tree.root)

print("\nPostorder:")
tree.postorder(tree.root)

print("\n\nMinimum:",tree.findMin(tree.root))
print("Maximum:",tree.findMax(tree.root))'''



class BinaryTreeNode:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None


class BinaryTree:
    def __init__(self):
        self.root=None

    def add(self,data):
        new=BinaryTreeNode(data)

        if self.root is None:
            self.root=new
            return

        self.recursiveAdd(self.root,new)

    def recursiveAdd(self,current,new):
        if current.left is None:
            current.left=new
            return

        if current.right is None:
            current.right=new
            return

        self.recursiveAdd(current.left,new)

    def preorder(self,current):
        if current is None:
            return

        print(current.val,end=" ")
        self.preorder(current.left)
        self.preorder(current.right)

    def inorder(self,current):
        if current is None:
            return

        self.inorder(current.left)
        print(current.val,end=" ")
        self.inorder(current.right)

    def postorder(self,current):
        if current is None:
            return

        self.postorder(current.left)
        self.postorder(current.right)
        print(current.val,end=" ")

    def remove(self,data):
        if self.root is None:
            return

        if self.root.val == data:
            self.root=None
            return

        queue=[self.root]
        target=None
        last=None
        parent=None

        while queue:
            current=queue.pop(0)

            if current.val == data:
                target=current

            if current.left:
                parent=current
                queue.append(current.left)

            if current.right:
                parent=current
                queue.append(current.right)

            last=current

        if target is None:
            print("Value not found")
            return

        target.val=last.val

        if parent.right == last:
            parent.right=None
        else:
            parent.left=None

    def display(self,current,depth=0):
        if current is None:
            return

        print("  "*depth,current.val)
        self.display(current.left,depth+1)
        self.display(current.right,depth+1)

    def findMin(self,current):
        if current is None:
            return None

        minimum=current.val

        left_min=self.findMin(current.left)
        right_min=self.findMin(current.right)

        if left_min is not None and left_min < minimum:
            minimum=left_min

        if right_min is not None and right_min < minimum:
            minimum=right_min

        return minimum

    def findMax(self,current):
        if current is None:
            return None

        maximum=current.val

        left_max=self.findMax(current.left)
        right_max=self.findMax(current.right)

        if left_max is not None and left_max > maximum:
            maximum=left_max

        if right_max is not None and right_max > maximum:
            maximum=right_max

        return maximum


tree=BinaryTree()

tree.add(10)
tree.add(20)
tree.add(5)
tree.add(40)
tree.add(2)
tree.add(30)

print("Before Remove:")
tree.display(tree.root)

tree.remove(20)

print("\nAfter Remove:")
tree.display(tree.root)

print("\nPreorder:")
tree.preorder(tree.root)

print("\nInorder:")
tree.inorder(tree.root)

print("\nPostorder:")
tree.postorder(tree.root)