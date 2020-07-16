"""
1. Implement a generic tree class in python: Should support methods like:
a) Finding the height of the tree
b) Adding a child node to a given node of the tree
c) Finding number of nodes in the tree
d) Deleting ith child node of a given node(you have to think about freeing memory here too!)
e) Printing nodes of the tree using pre order and post order traversal
f) Printing longest root to leaf path in the tree
g) Print the set of nodes on a given level, i
h) Searching for a given node in the tree (Assume node pointer is given)
I) Finding out the parent node of a given node pointer
J) Printing the path between two given nodes (Assume all nodes of the tree are distinct). Note this path will be unique
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addAtTail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = LinkedList()

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def add_child(self, child_node):
        child_node.set_parent(self)
        self.children.addAtTail(child_node)


class Tree:
    def __init__(self, data):
        self.root = TreeNode(data)

    def return_root(self):
        return self.root

    # def get_node_parent(self, curr_node):

    def get_tree_node(self, curr_node, value):
        if curr_node.data == value:
            return curr_node
        else:
            temp = curr_node.children.head
            while temp:
                node = self.get_tree_node(temp.value, value)
                if node:
                    return node
                else:
                    temp = temp.next
        return None

    def pre_order(self, current_node):
        print(current_node.data, end="  ")
        temp = current_node.children.head
        while temp:
            self.pre_order(temp.value)
            temp = temp.next

    def post_order(self, current_node):
        temp = current_node.children.head
        while temp:
            self.post_order(temp.value)
            temp = temp.next
        print(current_node.data, end="  ")

    def add_child_node(self, where_to_add, child_to_add):
        # where_to_add is a parent where child will be added
        new_node = TreeNode(child_to_add)
        node2 = self.get_tree_node(self.root, where_to_add)
        node2.add_child(new_node)


tree = Tree(0)
tree.add_child_node(0, 1)
tree.add_child_node(0, 2)
tree.add_child_node(0, 3)
tree.add_child_node(1, 4)
tree.add_child_node(1, 5)
tree.add_child_node(2, 6)
tree.add_child_node(3, 7)
tree.add_child_node(3, 8)
tree.add_child_node(3, 9)

#
tree.pre_order(tree.root)
print()
tree.post_order(tree.root)
print()

# print(tree.number_tree_nodes(tree.root))
