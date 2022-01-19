# Project 2
Breadth-first search

Breadth-First-Search (BFS) is the process of traversing each node of a graph, which traverses each vertex (layer after layer before moving on to the next) and then determinining whether or not a vertex or node has been visited beforehand. 

One keeps track of nodes to visit using a queue data structure, which could be a list, or an actual queue from the collections package included in Python. 
It is important to note that a queue is a linear data structure that stores items in a first-in-first-out (FIFO) manner. That is, with a queue, the least recently added item is removed first. 
This translates to adding to the queue (previously unvisited nodes), or enqueueing (removing from queue, popping in list) during the graph's traversal.

Note also that this package utilizes lists to store previously visited and current nodes. A dictionary is utilized to keep track of parent nodes for the returning of a traversed path when given a `start_node` and an `end_node`. 

Traversing in this implementation stops once `start_node` equals `end_node`, meaning we've reached the end during our traversal, and the shortest path is outputted. 
It is also worth noting that the graphs utilized in this implementation are unweighted. 
