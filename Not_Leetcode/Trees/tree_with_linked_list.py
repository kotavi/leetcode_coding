"""
1. Implement a generic tree class in python: Should support methods like:
a) Finding the height of the tree
c) Finding number of nodes in the tree
d) Deleting ith child node of a given node(you have to think about freeing memory here too!)
f) Printing longest root to leaf path in the tree
g) Print the set of nodes on a given level, i
j) Printing the path between two given nodes (Assume all nodes of the tree are distinct). Note this path will be unique

Implemented:
b) Adding a child node to a given node of the tree
e) Printing nodes of the tree using pre order and post order traversal
h) Searching for a given node in the tree (Assume node pointer is given)
i) Finding out the parent node of a given node pointer

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

    def print_linked_list(self):
        curr = self.head
        if not curr:
            print("LinkedList is empty")
            return
        while curr:
            print("{}".format(curr.value), end=" --> ")
            curr = curr.next
        print()


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

    def get_parent_node(self, curr_node, value):
        if curr_node.data == value:
            return curr_node.parent
        else:
            temp = curr_node.children.head
            while temp:
                node = self.get_tree_node(temp.value, value)
                if node:
                    return node.parent
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

    def add_child_node(self, where_to_add, value):
        # where_to_add is a parent where child will be added
        new_tree_node = TreeNode(value)
        parent_node = self.get_tree_node(self.root, where_to_add)
        parent_node.add_child(new_tree_node)

    def height(self, curr_tree_node):
        pass

    def nodes_number(self, curr_tree_node):
        """
        sum of all curr_tree_node.children.size
        then result + 1 to count root node
        """
        pass

    def nodes_at_level(self, curr_tree_node, level):
        pass

    def delete_child_node(self, curr_tree_node, value):
        pass

    def longest_path(self, root_node):
        pass

    def longest_path_between_nodes(self, tree_node1, tree_node2):
        pass


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

tree.pre_order(tree.root)
print()
tree.post_order(tree.root)
print()
p = tree.get_parent_node(tree.root, 9)
print(p.data)
p.children.print_linked_list()
