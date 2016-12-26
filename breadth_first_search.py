"""
Breadth-First Search

This searching algorithm will search through a tree going through each
node at one level before continuing to the next level of nodes.

BFS will search through the tree assigning each vertex(node) a DISTANCE
value, which is the distance from the source vertex, and a PREDECESSOR value
which is the node it came from on the path from the source.

We start the search from the source node.  All distance values are initialized
to null.  Upon visiting a node if the distance == null, it has not yet been visited.

We use a Queue object (a list) to track the nodes we visited but have not searched
from yet. 

Start from source.
Visit each node connected to source.
Enqueue these nodes, assign distance and predecssor value.
Visit first node in queue and repeat the process of visiting each
node in the same distnace from source /level and assignign distance & predecssor values.

A quick note, for this example we will represent a tree using an adjacency list.
There are 3 common forms of representing graphical structures in code:
-Edge list
-Adjacency Matrix
-Adjaceny List

This example will use an adjaceny list.  In which each element in the list is
a list of all of the nodes that particular element is connected to.  For example
element 0 will have a list of [1] which means it is only connected to node 1.  Since
this tree will be undirected then the elemnt 1 will also have [0] as well as any other
nodes it is connected to.
"""

adj_list = [
            [1, 2],
            [0, 4, 5],
            [0, 3, 4],
            [2, 6],
            [1, 2],
            [1, 6],
            [3, 5]
            ]
            
#def run_bfs(adj_list, start):
#    '''(list, int) -> list of dictionaries
#    
#    Will create a map essentially of our tree.  This function returns a list
#    of {distance: x, predecessor: x} for each node it searches through.  The
#    list index is the node index in the tree.
#    '''
#    queue = [start] #Enqueue the starting point
#    visited = [start] #Track the nodes already been to
#    tree_info = []
#    #Append source node
#    tree_info.append({'source': 'null', 'distance': 0})
#    
#    while queue:
#        current_node = queue.pop(0) #First In First Out
#        current_node_info = []
#        for adj_node in adj_list[current_node]:
#            if adj_node not in visited:
#                queue.append(adj_node)
#                print tree_info
#                current_distance = tree_info[current_node]['distance']
#                current_distance += 1
#                current_node_info.append({'source': current_node,
#                                  'distance': current_distance})
#        tree_info.append(current_node_info)
#    return tree_info
#            
            
def run_bfs(adj_list, start):
    tree_info = []
    #Intialize all nodes
    for node in adj_list:
        tree_info.append({'distance' : None, 'source' : None})
    #Create Queue
    queue = []
    #Start from Source
    tree_info[start]['distance'] = 0
    queue.append(start)
    
    #Loop through whole tree
    while queue:
        current_node = queue.pop(0) #First in, First out
        for adj_node in adj_list[current_node]:
            if tree_info[adj_node]['distance'] is None:
                tree_info[adj_node]['distance'] = tree_info[current_node]['distance'] + 1
                tree_info[adj_node]['source'] = current_node
                queue.append(adj_node)
    return tree_info
        
    
print run_bfs(adj_list, 0)