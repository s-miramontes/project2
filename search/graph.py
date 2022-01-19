################
#



import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object which serves as a container for 
        methods to load data and 
        
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node, just return a list with the order of traversal
        * If there is an end node and a path exists, return a list of the shortest path
        * If there is an end node and a path does not exist, return None

        """
        # edge cases
        if start not in self.graph.nodes():
            raise ValueError("Please a start node that is included in the graph!")

        elif end not in self.graph.nodes():
            raise ValueError("Please enter an end node that is included in the graph!")

        elif start == end and self.graph.nodes():
            return [start]


        # keep track of visited nodes, start queue
        been_there = []
        my_queue = []

        # fill queue
        my_queue.append(start)
        been_there.append(start)

        # parent tracking
        my_parents = dict()
        my_parents[start] = None

        # not path founds yet @ start
        path = False

        # while not empty
        while my_queue:
            # dequeue
            curr_ = my_queue.pop(0) 

            # if end_node
            if end:
                # reached the end, bye
                if curr_ == end:
                    path = True
                    break

            # traverse
            for neighbor in self.graph[curr_]:

                if neighbor not in been_there:
                    queue.append(neighbor)
                    my_parents[neighbor] = curr_
                    been_there.append(neighbor)

        
        # pathfinder, end node exists
        if end and path:
            the_path = []

            if path:
                end_node = end
                the_path.append(end_node)

                while my_parents[end_node] is not None:
                    the_path.append(my_parents[end_node])
                    end_node = my_parents[end_node]

                the_path.reverse()
            return the_path

        elif end and not path:
            return None

        else:
            return been_there




