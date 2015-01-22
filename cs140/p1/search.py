# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first [p 85].

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())


    """
    """
    queue = util.Stack()
    queue.push( (problem.getStartState(), [], []) )
    while not queue.isEmpty():
        node, actions, visited = queue.pop()

        for coord, direction, steps in problem.getSuccessors(node):
            if not coord in visited:
                if problem.isGoalState(coord):
                    return actions + [direction]
                queue.push((coord, actions + [direction], visited + [node] ))

    return []

    """

    stack = []
    # just get the first move
    start = problem.getSuccessors(problem.getStartState())[0]
    stack.append(start)
    #holds coordinates ONLY
    visited = []
    visited.append(problem.getStartState())
    # visited.append(start)


    while stack:
        tile = stack[len(stack)-1]
        visited.append(tile[0])
        validSuccessors = []

        # print visited

        successors = problem.getSuccessors(tile[0])

        for x in successors:
            if x[0] not in visited:
                validSuccessors.append(x)
            # visited.append(x[0])
        if validSuccessors:
            # validSuccessors.reverse()
            firstSuccessor = validSuccessors[0]
            visited.append(firstSuccessor[0])
            stack.append(firstSuccessor)
            if problem.isGoalState(firstSuccessor[0]):
                return [s[1] for s in stack]
        else:
            stack.pop()


            #############################
            # fix this so it gets correct # of nodes
            #############################



def breadthFirstSearch(problem):
    "Search the shallowest nodes in the search tree first. [p 81]"


    # follow fixed version of UCS as template

    queue = []
    queue.append((problem.getStartState(), []))
    visited = []

    while queue:
        tile = queue.pop()

        coords = tile[0]
        actions = tile[1]

        for x in problem.getSuccessors(coords):
            pos = x[0]
            dir = x[1]

            if pos not in visited:
                # check if successors are goal, not popped tile
                if problem.isGoalState(pos):
                    return actions + [dir]
                new_actions = actions + [dir]
                queue.insert(0,(pos, new_actions))
                # this time we add fringe to visited, not popped tiles
                visited.append(pos)
    return []


    # below is pretty bad but not as broken as UCS was

"""
    #just coordinates (x,y)
    visited = []
    visited.append(problem.getStartState())

    queue = problem.getSuccessors(problem.getStartState())

    # parent[child coordinates] = parent coordinates
    parent = {}
    # action[coordinates] = direction we came from to get here
    action = {}

    parent[problem.getStartState] = "nil"

    # load the first successors
    for x in queue:
        parent[x[0]] = problem.getStartState()
        action[x[0]] = x[1]

    while queue:
        foundPath = False
        tile = queue.pop()
        # print tile
        coords = tile[0]
        visited.append(coords)

        successors = []
        for x in problem.getSuccessors(coords):
            if x[0] not in visited:
                successors.append(x)
                visited.append(x[0])

        #for each child node of this node
        for x in successors:
            # keep track of the action taken to get here
            action[x[0]] = x[1]

            # and its parent
            parent[x[0]] = coords
            # if we reached the goal state
            if problem.isGoalState(x[0]):
                foundPath = True
                # create a path list and put last move on it
                path = []
                path.append(x[1])
                # pathPar = used to iterate through parents back to start state
                pathPar = coords
                # until we get there
                while pathPar != problem.getStartState():
                    # put the action of the move to get from the parent to the child on the list
                    path.insert(0,action[pathPar])
                    # go to next parent up the tree
                    pathPar = parent[pathPar]
                # path.pop()

            else:
                queue.insert(0,x)
        if foundPath == True:
            return path

"""

def uniformCostSearch(problem):
    "Search the node of least total cost first. "


    ##################
    #rewrite checking goal state right after queue pop, instead of after getSuccessor()
    #########################


    # queue will hold the list of ((coordinates,[actions])
    queue = util.PriorityQueue()
    queue.push( (problem.getStartState(), []), 0)
    # visited is list of coordinates
    visited = []

    while not queue.isEmpty():
        tile = queue.pop()

        coords = tile[0]
        actions = tile[1]

        # print node, actions

        if problem.isGoalState(coords):
            # if we're already on the tile
            # the actions are what we want
            return actions

        visited.append(coords)

        # NOW check successors
        for x in problem.getSuccessors(coords):

            pos = x[0]
            dir = x[1]
            # no x[2], cost is trivial, 1

            if pos not in visited:

                new_actions = actions + [dir]

                # getCostOfActions = calculate list of action's cost
                queue.push((pos, new_actions), problem.getCostOfActions(new_actions))

    # if goal state never reached
    return []


    # below this is crap, rewrite

"""
    #just coordinates (x,y)
    visited = []
    visited.append(problem.getStartState())

    # parent[child coordinates] = parent coordinates
    parent = {}
    # action[coordinates] = direction we came from to get here
    action = {}
    # cost[coordinates] = cost of visiting this tile
    cost = {}

    parent[problem.getStartState] = "nil"

    queue = util.PriorityQueue()
    # load the first successors
    for x in problem.getSuccessors(problem.getStartState()):
        parent[x[0]] = problem.getStartState()
        action[x[0]] = x[1]
        cost[x[0]] = x[2]
        queue.push(x[0],x[2])


    while not queue.isEmpty():
        foundPath = False
        #tile just has coordinates
        tile = queue.pop()
        visited.append(tile)

        # print tile

        successors = []
        for x in problem.getSuccessors(tile):
            if x[0] not in visited:
                successors.append(x)
                visited.append(x[0])

        #for each child node of this node
        for x in successors:
            # keep track of the action taken to get here
            action[x[0]] = x[1]
            # and its parent
            parent[x[0]] = tile
            # and the tile cost + cost of parents
            cost[x[0]] = x[2] + cost[tile]
            if not problem.isGoalState(x[0]):
                # coordinates and cost
                queue.push(x[0],x[2] + cost[tile])

            # if we reached the goal state
            else:
                foundPath = True
                # create a path list and put last move on it
                path = []
                path.append(x[1])
                # pathPar = used to iterate through parents back to start state
                pathPar = tile
                # until we get there
                while pathPar is not problem.getStartState():
                    # put the action of the move to get from the parent to the child on the list
                    path.insert(0,action[pathPar])
                    # go to next parent up the tree
                    pathPar = parent[pathPar]

                path.append(action[problem.getStartState()])

        if foundPath == True:
            return path


"""

    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."

    #just coordinates (x,y)
    visited = []
    visited.append(problem.getStartState())

    # parent[child coordinates] = parent coordinates
    parent = {}
    # action[coordinates] = direction we came from to get here
    action = {}
    # cost[coordinates] = cost of visiting this tile
    cost = {}

    parent[problem.getStartState] = "nil"

    queue = util.PriorityQueue()
    # load the first successors
    for x in problem.getSuccessors(problem.getStartState()):
        parent[x[0]] = problem.getStartState()
        action[x[0]] = x[1]
        cost[x[0]] = x[2]
        queue.push(x[0],cost[x[0]])


    while not queue.isEmpty():
        #tile just has coordinates
        tile = queue.pop()
        visited.append(tile)

        # take heuristic cost off before we calculate cost of successors
        # we want to add up the accumulated path costs, but not the heuristic costs
        # but while it's in the queue, we want both the total path cost and tile heuristic cost
        cost[tile] = cost[tile] - heuristic(tile,problem)

        # print tile

        successors = []
        for x in problem.getSuccessors(tile):
            if x[0] not in visited:
                successors.append(x)
                visited.append(x[0])

        #for each child node of this node
        for x in successors:
            # keep track of the action taken to get here
            action[x[0]] = x[1]
            # and its parent
            parent[x[0]] = tile
            # and tile cost + path so far cost + heuristic cost
            cost[x[0]] = x[2] + cost[tile] + heuristic(x[0], problem)
            # print x[0], heuristic(x[0], problem), cost[x[0]], x[2]
            if not problem.isGoalState(x[0]):
                # coordinates and cost
                queue.push(x[0], cost[x[0]])

            # if we reached the goal state
            else:
                # create a path list and put last move on it
                path = []
                path.append(x[1])
                # pathPar = used to iterate through parents back to start state
                pathPar = tile
                # until we get there
                while pathPar != problem.getStartState():
                    # put the action of the move to get from the parent to the child on the list
                    path.insert(0,action[pathPar])
                    # go to next parent up the tree
                    pathPar = parent[pathPar]

                return path


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch