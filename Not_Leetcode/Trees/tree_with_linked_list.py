"""
1. Implement a generic tree class in python: Should support methods like:
d) Deleting ith child node of a given node(you have to think about freeing memory here too!)
f) Printing longest root to leaf path in the tree
g) Print the set of nodes on a given level, i
j) Printing the path between two given nodes (Assume all nodes of the tree are distinct). Note this path will be unique

Implemented:
b) Adding a child node to a given node of the tree
e) Printing nodes of the tree using pre order and post order traversal
h) Searching for a given node in the tree (Assume node pointer is given)
i) Finding out the parent node of a given node pointer
a) Finding the height of the tree
c) Finding number of nodes in the tree
c) Finding number of leaf nodes in the tree

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

    def get_parent(self, curr_node, value):
        node = self.get_tree_node(curr_node, value)
        return node.parent if node else None

    def get_parent_node(self, curr_node, value):
        """
        Finds parent of the tree node not using self.parent pointer
        """
        if curr_node.data is self.root.data and curr_node.data == value:
            return None
        else:
            temp = curr_node.children.head
            while temp:
                if temp.value.data == value:
                    return curr_node
                else:
                    if temp.value.children.size != 0:
                        node = self.get_parent_node(temp.value, value)
                        if node:
                            return node
                        else:
                            temp = temp.next
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
        # check if a curr_node is a leaf
        if curr_tree_node.children.size == 0:
            return 0
        else:
            height = 0  # final result
            temp = curr_tree_node.children.head
            while temp:
                h = self.height(temp.value)
                height = max(h, height)
                temp = temp.next
            height += 1
            return height

    def leaves_count(self, curr_tree_node):
        # check if a curr_node is a leaf
        if curr_tree_node.children.size == 0:
            return 1
        else:
            result = 0  # final result
            temp = curr_tree_node.children.head
            while temp:
                res = self.leaves_count(temp.value)
                result += res  # add a leaf to final result
                temp = temp.next
            return result

    def nodes_count(self, current_tree_node):
        """
        I reused code from leaves_count
        The only difference is that I return 1 + result
        For example: TreeNode(1) has 2 children: TreeNode(4) and TreeNode(5)
        the result for this subtree wil be result=2 (2 leaves)
        and with do + 1 to count a parent of these leaves
        """
        if current_tree_node.children.size == 0:
            return 1
        else:
            result = 0
            temp = current_tree_node.children.head
            while temp:
                res = self.nodes_count(temp.value)
                result += res
                temp = temp.next
            return 1 + result

    def nodes_at_level(self, curr_tree_node, level):
        """
        stack version
        or
        recursion
        """
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
tree.add_child_node(9, 10)
tree.add_child_node(9, 11)

tree.pre_order(tree.root)
print()
tree.post_order(tree.root)
print()

n = tree.get_parent_node(tree.root, 9)
print("Parent node: ", n.data)

print("Tree height:", tree.height(tree.root))
print("Number of leaves:", tree.leaves_count(tree.root))
print("Number of tree nodes:", tree.nodes_count(tree.root))

print("-*---" * 10)
tree2 = Tree(0)
tree2.add_child_node(0, 1)
tree2.add_child_node(1, 2)
tree2.add_child_node(2, 3)
tree2.add_child_node(3, 4)
tree2.add_child_node(4, 5)

tree2.pre_order(tree2.root)
print()
tree2.post_order(tree2.root)
print()

n = tree2.get_parent_node(tree2.root, 4)
print("Parent node: ", n.data)

print("Tree height:", tree2.height(tree2.root))
print("Number of leaves:", tree2.leaves_count(tree2.root))
print("Number of tree nodes:", tree2.nodes_count(tree2.root))
