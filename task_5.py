import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class Node:
    def __init__(self, key, color="#000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.val, color=node.color)
        if node.left:
            graph.add_edge(node.val, node.left.val)
            l = x - 1 / 2 ** layer
            pos[node.left.val] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.val, node.right.val)
            r = x + 1 / 2 ** layer
            pos[node.right.val] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, node_colors):
    tree = nx.DiGraph()
    pos = {(tree_root.val): (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node_colors[node] for node in tree.nodes()]

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, with_labels=True, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def dfs(root, node_colors, color_palette):
    stack = [root]
    color_index = 0
    while stack:
        node = stack.pop()
        node_colors[node.val] = color_palette[color_index]
        color_index += 1
        draw_tree(root, node_colors)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def bfs(root, node_colors, color_palette):
    queue = [root]
    color_index = 0
    while queue:
        node = queue.pop(0)
        node_colors[node.val] = color_palette[color_index]
        color_index += 1
        draw_tree(root, node_colors)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def color_gen_1(num_colors):
    base_color = mcolors.to_rgb('#410152')  # Dark base color
    target_color = mcolors.to_rgb('#e39ff5')  # Light target color
    gradient = [
        mcolors.to_hex([
            base_color[j] + (target_color[j] - base_color[j]) * i / (num_colors - 1)
            for j in range(3)
        ])
        for i in range(num_colors)
    ]
    return gradient

def color_gen_2(num_colors):
    base_color = mcolors.to_rgb('#013b21')  # Dark base color
    target_color = mcolors.to_rgb('#9ff5ce')  # Light target color
    gradient = [
        mcolors.to_hex([
            base_color[j] + (target_color[j] - base_color[j]) * i / (num_colors - 1)
            for j in range(3)
        ])
        for i in range(num_colors)
    ]
    return gradient

# Creating the tree
root = Node(0)
root.left = Node(5)
root.left.left = Node(6)
root.left.right = Node(11)
root.right = Node(2)
root.right.left = Node(4)
root.right.right = Node(99)

# Generating color palette for traversal
num_nodes = 7  # Total number of nodes in the tree
color_palette_1 = color_gen_1(num_nodes)
color_palette_2 = color_gen_2(num_nodes)


# Initialize node colors
node_colors = {0: "#000", 5: "#000", 6: "#000", 11: "#000", 2: "#000", 4: "#000", 99: "#000"}

# Displaying the tree with DFS traversal
print("DFS Traversal:")
dfs(root, node_colors, color_palette_1)

# Reset node colors for BFS traversal
node_colors = {0: "#000", 5: "#000", 6: "#000", 11: "#000", 2: "#000", 4: "#000", 99: "#000"}

# Displaying the tree with BFS traversal
print("BFS Traversal:")
bfs(root, node_colors, color_palette_2)

#For use - please close the pop-up window for to go to the next step.