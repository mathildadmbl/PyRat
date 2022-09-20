##############################################################
# The turn function should always return a move to indicate where to go
# The four possibilities are defined here
##############################################################

MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'



##############################################################
# Please put your code here (imports, variables, functions...)

# Import of random module
import random

# Global variables 
visited_locations = []
moves_to_perform = []


# FUNCTIONS 

#INPUTS: two locations : source_location, target_location 
#OUTPUT: the move it takes to go from source_location to target_location 
#if the move is not feasible, exception raised
def move_from_locations (source_location, target_location) : 
    difference = (target_location[0] - source_location[0], target_location[1] - source_location[1])
    if difference == (0, -1) :
        return MOVE_DOWN
    elif difference == (0, 1) :
        return MOVE_UP
    elif difference == (1, 0) :
        return MOVE_RIGHT
    elif difference == (-1, 0) :
        return MOVE_LEFT
    else :
        raise Exception("Impossible move")
 
    
def neighbors(location, graph):
    
    # Returns the neighbors of a location in a graph
    neighbors = [l for l in graph[location].keys()]
    return neighbors


def create_structure(): 
    # Creates an empty FIFO
    
    return []

def push_to_structure(structure, element): 
    # Add an element to the FIFO 
    
    res = structure.append(element) 
    return res 

def pop_from_structure(structure): 
    # Extract an element from the FIFO 
    
    elt = structure.pop(0)
    return elt 


def traversal(start_vertex, graph):
    # BFS traversal 
    #INPUTS: a graph, and a vertex from which to start the graph traversal using queuing structure 
    #OUTPUT: the list of explored_vertices, and a routing table to navigate through the graph 

    queuing_structure = create_structure() #create the FIFO
    
    queuing_structure.append((start_vertex, None))  #add the first vertex 
    
    explored_vertices = []
    routing_table = {}
    
    while(len(queuing_structure)) > 0: #while the queue is not empty 
        (current_vertex, parent) = pop_from_structure(queuing_structure) 
        
        if current_vertex not in explored_vertices: 
            explored_vertices.append(current_vertex) 
            routing_table[current_vertex] = parent 
        
        list_of_neighbors = neighbors(current_vertex, graph) 
        for neighbor in list_of_neighbors: 
            if neighbor not in explored_vertices: 
                queuing_structure.append((neighbor, current_vertex))
     
    return explored_vertices, routing_table


def find_route (routing_table, source_location, target_location) :
    # Use the routing table to find the sequence of locations from source to target
    # INPUTS: the routing table, and a two locations btw which we have to find a path 
    
    path = [target_location] #starting from the target 
    current_location = target_location 
    
    while(current_location != source_location): 
        parent = routing_table[current_location]
        path.append(parent) 
        current_location = parent 
        
    return path


def moves_from_locations (locations) :
    # Transform a series of locations into corresponding moves to realize it
    
    seq_of_locations = locations[::-1] #on retourne la liste pour avoir un chemin de src --> tgt 
    seq_of_moves = []
    
    for i in range(len(seq_of_locations)-1):  
        move = move_from_locations(seq_of_locations[i], seq_of_locations[i+1] )
        seq_of_moves.append(move) 
    
    return seq_of_moves 

##############################################################


##############################################################
# The preprocessing function is called at the start of a game
# It can be used to perform intensive computations that can be
# used later to move the player in the maze.
# ------------------------------------------------------------
# maze_map : dict(pair(int, int), dict(pair(int, int), int))
# maze_width : int
# maze_height : int
# player_location : pair(int, int)
# opponent_location : pair(int,int)
# pieces_of_cheese : list(pair(int, int))
# time_allowed : float
##############################################################

def preprocessing (maze_map, maze_width, maze_height, player_location, opponent_location, pieces_of_cheese, time_allowed) :
    global moves_to_perform 
    
    explored_vertices, routing_table = traversal(player_location, maze_map) 
    path = find_route(routing_table, player_location, pieces_of_cheese[0]) 
    moves_to_perform = moves_from_locations(path) 



##############################################################
# The turn function is called each time the game is waiting
# for the player to make a decision (a move).
# ------------------------------------------------------------
# maze_map : dict(pair(int, int), dict(pair(int, int), int))
# maze_width : int
# maze_height : int
# player_location : pair(int, int)
# opponent_location : pair(int,int)
# player_score : float
# opponent_score : float
# pieces_of_cheese : list(pair(int, int))
# time_allowed : float
##############################################################

def turn (maze_map, maze_width, maze_height, player_location, opponent_location, player_score, opponent_score, pieces_of_cheese, time_allowed) :
    
    return moves_to_perform.pop(0)
    
    



