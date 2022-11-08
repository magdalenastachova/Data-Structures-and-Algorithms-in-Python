class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
            return True
        temp=self.root
        while True:
            if new_node.value==temp.value: return False
            if new_node.value<temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp=temp.right

    def contains(self,value):
        temp=self.root
        while temp:
            if value == temp.value: return True
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def min_value_node(self,current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node

    def BFS(self):  # breadth first search
        my_queue =[]
        results=[]
        if self.root: my_queue.append(self.root)
        while len(my_queue)>0:
            results.append(my_queue[0].value)
            if my_queue[0].left: my_queue.append(my_queue[0].left)
            if my_queue[0].right: my_queue.append(my_queue[0].right)
            my_queue.pop(0)
        return results

    def DFS_preorder(self): #depth first search: Preorder
        results=[]
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left: traverse(current_node.left)
            if current_node.right: traverse(current_node.right)
        if self.root: traverse(self.root)
        return results

    def DFS_postorder(self):
        results=[]
        def traverse(current_node):
            if current_node.left: traverse(current_node.left)
            if current_node.right: traverse(current_node.right)
            results.append(current_node.value)
        if self.root: traverse(self.root)
        return results

    def DFS_inorder(self):
        results=[]
        def traverse(current_node):
            if current_node.left: traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right: traverse(current_node.right)
        if self.root: traverse(self.root)
        return results

my_tree=BinarySearchTree()
my_list=[47,21,76,27,18,82,52]
for item in my_list:
    my_tree.insert(item)
print(my_tree.contains(27))
print(my_tree.contains(17))
print(my_tree.min_value_node(my_tree.root))
print(my_tree.min_value_node(my_tree.root.right))
print(my_tree.BFS())
print(my_tree.DFS_preorder())
print(my_tree.DFS_postorder())
print(my_tree.DFS_inorder())

