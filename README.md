# goit-algo-fp

Step-by-step guide to the final project



Task 1.
Data Structures. Sorting. Working with a Singly Linked List

To implement a singly linked list (an implementation example can be taken from the lecture notes), you need to:

Write a function that implements the reversal of a singly linked list, modifying references between nodes.
Develop a sorting algorithm for a singly linked list, such as insertion sort or merge sort.
Write a function that merges two sorted singly linked lists into one sorted list.



Task 2.
Recursion. Creating the "Pythagorean Tree" Fractal Using Recursion

You need to write a Python program that uses recursion to create the "Pythagorean Tree" fractal. The program should visualize the "Pythagorean Tree" fractal, and the user should be able to specify the recursion level.



Task 3. 
Trees, Dijkstra's Algorithm

Develop Dijkstra's algorithm to find the shortest paths in a weighted graph using a binary heap. The task includes creating a graph, using a heap to optimize the selection of vertices, and calculating the shortest paths from the initial vertex to all others.



Task 4. 
Visualization of the Heap

The following code constructs binary trees. Analyze the code to understand how it works.

import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Additional argument to store the color of the node

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.val, color=node.color)  # Saving a node color in a graph
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

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {(tree_root.val): (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]  # Collect node colors to display

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, with_labels=True, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Creating the tree
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Displaying the tree
draw_tree(root)

Using this code as a base, build a function to visualize the binary heap.



Task 5. 
Visualization of Binary Tree Traversal

Using the code from task 4 to construct a binary tree, it is necessary to create a Python program that visualizes tree traversals in-depth and breadth-first.

The program should display each step in nodes with different colors, using the RGB 16-system (example #1296F0). Depending on the traversal sequence, node colors should change from dark to light shades. Each node, when visited, should receive a unique color that visually reflects the traversal order.



Task 6: 
Greedy Algorithms and Dynamic Programming

It is necessary to write a Python program that uses two approaches — greedy algorithm and dynamic programming algorithm to solve the problem of choosing food with the highest total calorie content within a limited budget.

Each type of food has a specified cost and calorie content. Data about food is represented as a dictionary, where the key is the dish name, and the value is a dictionary with the cost and calorie content.

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

Develop a function greedy_algorithm for the greedy algorithm that selects dishes, maximizing the ratio of calories to cost without exceeding the specified budget.

To implement the dynamic programming algorithm, create a function dynamic_programming that calculates the optimal set of dishes to maximize calorie content within a given budget.



Task 7: 
Using the Monte Carlo Method

It is necessary to write a Python program that simulates a large number of dice throws, calculates the sums of numbers that appear on the dice, and determines the probability of each possible sum.

Create a simulation where two dice are thrown a large number of times. For each throw, determine the sum of the numbers that appeared on both dice. Count how many times each possible sum (from 2 to 12) appears in the simulation. Using this data, calculate the probability of each sum.

Based on the simulations, create a table or graph displaying the probabilities of each sum identified using the Monte Carlo method.

The table of probabilities of sums when throwing two dice looks as follows.

Sum	Probability
2	2.78% (1/36)
3	5.56% (2/36)
4	8.33% (3/36)
5	11.11% (4/36)
6	13.89% (5/36)
7	16.67% (6/36)
8	13.89% (5/36)
9	11.11% (4/36)
10	8.33% (3/36)
11	5.56% (2/36)
12	2.78% (1/36)
Compare the results obtained using the Monte Carlo method with the analytical calculations provided in the table above.