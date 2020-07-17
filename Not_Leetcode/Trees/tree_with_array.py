class TreeNode:

    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, child):
        if child in self.children:
            return None
        child.parent = self
        self.children.append(child)

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return self.children == []

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 2
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.value)
        if self.children:
            for child in self.children:
                child.print_tree()


def print_all_leaves(tree):
    if not tree.children:
        return tree.value
    else:
        return [print_all_leaves(child) for child in tree.children]


def post_order(tree):
    if not tree:
        return
    for child in tree.children:
        post_order(child)
    print(tree.value, end=", ")


def leaf_count(tree):
    if len(tree.children) == 0:
        return 1
    else:
        return sum([leaf_count(c) for c in tree.children])


def tree_height(tree):
    if len(tree.children) == 0:
        return 1
    else:
        return 1 + max([tree_height(c) for c in tree.children])


def nodes_number(tree):
    if len(tree.children) == 0:
        return 1
    else:
        return 1 + sum([nodes_number(c) for c in tree.children])


def node_degree(tree):
    # the number of its children
    if len(tree.children) == 0:
        return 0
    else:
        return max([len(tree.children)]+[node_degree(n) for n in tree.children])


"""
                1
            /   |   \
           2    3    4
        /    \     / | \
       5      6   7  8  9
    /  |  \
   10 11  12
"""
root = TreeNode("1")
tree1 = TreeNode("2")
tree4 = TreeNode("5")
tree4.add_child(TreeNode("10"))
tree4.add_child(TreeNode("11"))
# there cannot be duplicates in this tree
t = TreeNode("12")
tree4.add_child(t)
tree4.add_child(t)

tree1.add_child(tree4)
tree1.add_child(TreeNode("6"))
tree2 = TreeNode("3")
tree3 = TreeNode("4")
tree3.add_child(TreeNode("7"))
tree3.add_child(TreeNode("8"))
tree3.add_child(TreeNode("9"))

root.add_child(tree1)
root.add_child(tree2)
root.add_child(tree3)

root.print_tree()
print("Level number of tree4: ", tree4.get_level())
print("Tree height: ", tree_hight(root))
print("Nodes number: ", nodes_number(root))
print("Node degree (root)", node_degree(root))
print("Leaf count: ", leaf_count(root))
print("Tree leaves: ", print_all_leaves(root))
print("Post order: ")
print(post_order(root))
