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
    "*** YOUR CODE HERE ***"

    # let's start over

    stack = []          # holds coordinates we need to finish
    visited = []        # holds coordinates of everywhere we've been
    path = []           # holds directions to get to coordinates (1 less than stack)
    # path.append("null")

    # start at the start
    stack.append(problem.getStartState())

    while stack:
        tile = stack.pop()

        if path:
            action = path.pop()
        else:
            action = "null"

        if tile not in visited:
            visited.append(tile)
            print "popping ", tile

            validSuccessors = []

            for x in problem.getSuccessors(tile):
                if x[0] not in visited:
                    validSuccessors.append(x)

            print "valid successors of ", tile, " are ", validSuccessors

            for x in validSuccessors:

                if problem.isGoalState(x[0]):
                    stack.append(x[0])
                    path.append(x[1])
                    print "visited:", visited
                    print "stack:", stack
                    print path
                    return path

                elif x[0] not in visited:

                    stack.append(x[0])
                    path.append(x[1])

            # put tile back on stack if we had successors
            if validSuccessors:
                stack.append(tile)
                if action is not "null":
                    path.append(action)

            print stack









        # if tile not in visited:
        #     visited.append(tile)
        #     stack.extend([s[0] for s in problem.getSuccessors(tile)])
        #     path.extend([s[1] for s in problem.getSuccessors(tile)])
        #     #print stack
        #     #print path
        #
        # if problem.isGoalState(tile):
        #     path.append(curdir)
        #     stack.append(tile)
        #     #print stack
        #     #print path
        #     return path



    '''
    #add coordinates of start state to list of visited states
    #and coords for checking successors - ones we still have to check
    #path (directions) to keep track of list of actions
    visited = []
    coords = []
    path = []

    #[0] gives the coordinates, [1] is the direction, [2] is cost of action
    #self python note: append is pushing, top of list at back
    startCoords = problem.getStartState()
    visited.append(startCoords)
    coords.append(startCoords)

    #loop until coords is empty = no more options to move left
    while coords is not []:

        tile = coords.pop()

        if tile not in visited:
            visited.append(tile)

        if path:
            curdir = path.pop()
        else:
            curdir = "null"

        print "Current tile: ", tile
        #gives a list of tuples for tiles(x,y) we can move to next
        fringeTiles = problem.getSuccessors(tile)
        #fringeCoords = [seq[0] for seq in problem.getSuccessors(tile)]
        #fringepath = [seq[1] for seq in problem.getSuccessors(tile)]
        #put all on coords
        for x in fringeTiles:
            #but only if we haven't visited it
            if x[0] not in visited:
                #we need to check these coords AND keep track of path
                coords.append(x[0])
                path.append(x[1])
                print "coords on stack: ", coords
                print "current direction list: ", path
                #because we just want the first node
                break

        if problem.isGoalState(tile):
            path.append(curdir)
            print "final path:", path
            return path
    '''
def breadthFirstSearch(problem):
    "Search the shallowest nodes in the search tree first. [p 81]"
    "*** YOUR CODE HERE ***"



    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"



    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"



    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch