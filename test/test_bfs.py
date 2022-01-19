# write tests for bfs
import pytest
from search import graph

@pytest.fixture # what is this


def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    # generage dummy network, from lecture notes
    a_graph = graph.Graph("data/dummy.adjlist")

    # traverse at different start nodes
    traverse_B = a_graph.bfs('B')
    traverse_A = a_Graph.bfs('A')

    assert traverse_B == ['B', 'C', 'D', 'E', 'F', 'G']
    assert len(traverse_B) == 6

    assert traverse_A == ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    assert len(traverse_A) == 7
    

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    # generate dummy network 
    a_graph = graph.Graph("data/dummy.adjlist")

    # path non existent
    traverse_BC = a_graph.bfs('B', 'C')
    traverse_DG = a_graph.bfs('D', 'G')

    # shortest paths
    traverse_AD = a_graph.bfs('A', 'D')
    traverse_AG = a_graph.bfs('A', 'G')

    # test non existing paths
    assert traverse_BC == None
    assert traverse_DG == None
    # test shortest paths 
    assert traverse_AD == ['A', 'B', 'D']
    assert traverse_AG == ['A', 'C', 'G']
    