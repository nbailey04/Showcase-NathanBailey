class Graph:                                                                # Makes a class called 'Graph'

    def __init__(self):                                                     # Defines an initializing sequence
        self.graph = {}                                                     # Makes a empty dictionary
        self.edge_count = 0                                                 # Initializes a variable that will keep track of the number of edges made

    def add_edge(self, vertex, neighbor):                                   # Defines a function called 'add_edge' that will compile using 2 given variables (vertex and neighbor)
        if vertex not in self.graph:                                        # This checks to see if the vertex is not already in the 'self.graph' dictionary
            self.graph[vertex] = []                                         # If it is not , then it will make an empty set to serve as the spot where the vertex is supposed to be filled
        self.graph[vertex].append(neighbor)                                 # This adds the neighbor value to the empty spot previously made to fill in the empty spot now with the new neighbor value
        self.edge_count += 1                                                # This increases the count value by 1

    def dfs(self, start, visited=None):                                     # This defines the punction called 'def' that will do the Depth-First Search starting at the given 'start' value and predefining the variable 'visited' as None
        if visited is None:                                                 # This checks if the 'visited' is still None
            visited = set()                                                 # If it is, then it will make 'visited' equal to the empty set ( set() )
        stack = [start]                                                     # This makes 'stack' variable equal the start parameter

        while stack:                                                        # This will run for as long as the 'stack' variable exists
            current_vertex = stack.pop()                                    # This will do a pop on the stack and store the returned value as 'current_vertex'
            if current_vertex not in visited:                               # This checks to see if the 'current_vertex' variable is in 'visited'
                print(current_vertex, end=' ')                              # This will print the current vertex on the same line and seperate the values by a space ' '
                visited.add(current_vertex)                                 # This uses 'add' to add 'current_vertex' to 'visited' (add does not add it if it is already in visited
                neighbors = reversed(self.graph.get(current_vertex, []))    # This stores the the reversed, iterated value from 'self.graph' to allow a true Depth-First Search
                for neighbor in neighbors:                                  # This will repeat for every element in 'neighbors'
                    if neighbor not in visited:                             # This checks to see if the current element 'neighbor' is in ' visited'
                        stack.append(neighbor)                              # If it is not, then it will add 'neigbor' to 'stack'
    def count(self):                                                        # This defines a function called 'count' that returns the 'self.edge_count' value
        return self.edge_count                                              # Returns the 'self.edge_count' value

"DRIVER CODE BELOW"
g = Graph()                                         # Initializes g in the 'Graph' class
g.add_edge(0, 1)                                    # This adds the edge that connects the vertexes 0 and 1
g.add_edge(0, 2)                                    # This adds the edge that connects the vertexes 0 and 2
g.add_edge(2, 3)                                    # This adds the edge that connects the vertexes 2 and 3
g.add_edge(2, 4)                                    # This adds the edge that connects the vertexes 2 and 4
g.add_edge(4, 5)                                    # This adds the edge that connects the vertexes 4 and 5
g.add_edge(1, 3)                                    # This adds the edge that connects the vertexes 1 and 3
g.add_edge(3, 5)                                    # This adds the edge that connects the vertexes 3 and 5


# THIS IS WHERE THE TEST CASES WOULD GO TO WORK BEST
#assert g.count() != 0, "There are no elements."         TEST CASE 1
#assert g.count() != 1, "There are only 2 nodes with 1 edge connecting them."

print("Depth-First Search starting from vertex 0:")
g.dfs(0)                                # Sets where to start the DFS from ( from 0 )


"TEST CASES BELOW"
'What happens when there is no elements/nodes in the graph'
#assert g.count() != 0, "There are no elements"

'What happens if there is only one node in the graph'
#This wont happen because they are added in doubles

'What happens if the graph only has 2 nodes'
#assert g.count() != 1, "There are only 2 nodes with 1 edge connecting them"
