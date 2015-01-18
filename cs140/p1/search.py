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


    stack = []
    # just get the first move
    start = problem.getSuccessors(problem.getStartState())[0]
    stack.append(start)
    #holds coordinates ONLY
    visited = []
    visited.append(problem.getStartState())


    while stack:
        tile = stack.pop()
        visited.append(tile[0])
        validSuccessors = []

        # print visited

        for x in problem.getSuccessors(tile[0]):
            if x[0] not in visited:
                validSuccessors.append(x)

        # print "valid successors are ", validSuccessors

        ##########################
        # makes it run faster on tiny,medium,bigMazes
        ##########################
        validSuccessors.reverse()

        if validSuccessors:
            stack.append(tile)

            firstSuccessor = validSuccessors[0]
            # print "firstSuccessor: ", firstSuccessor

            if problem.isGoalState(firstSuccessor[0]):
                stack.append(firstSuccessor)
                return [s[1] for s in stack]
            else:
                stack.append(firstSuccessor)


    #  awwwww YISSSSSSSSSSSSSSSSSSSS


def breadthFirstSearch(problem):
    "Search the shallowest nodes in the search tree first. [p 81]"
    "*** YOUR CODE HERE ***"

    visited = []
    visited.append(problem.getStartState())


    # list of 2-tuples
    #   first element is 3 tuple of current step:
    #       ((x,y),(direction),(cost))
    #   second element is list of actions taken to get here:
    #       [(direction)]
    queue = []

    # have a tuple that has (step just taken to get here, all steps taken to get there)
    for x in problem.getSuccessors(problem.getStartState()):
        pathList = []
        pathList.append(x[1])
        queue.append((x,pathList))

    while queue:
        tile = queue.pop()
        #first element of first tuple's first element -> (x,y)
        coords = tile[0][0]
        visited.append(coords)

        #has just ((x,y),(direction),(1))
        successors = []

        for x in problem.getSuccessors(coords):
            if x[0] not in visited:
                successors.append(x)

        for x in successors:
            #to make sure we don't add more than one action
            newTile = tile
            #put add the new action to the list of actions
            newTile[1].append(x[1])
            #print newTile
            if problem.isGoalState(x[0]):
                print newTile[1]
                return newTile[1]
            else:
                queue.insert(0,(x,newTile[1]))
                visited.append(x[0])





"""
    queue = problem.getSuccessors(problem.getStartState())

    # holds coordinates ONLY - doesn't matter if we treat as queue or stack
    visited = []
    visited.append(problem.getStartState())
    parTile = problem.getStartState()



    while queue:
        tile = queue.pop()
        pathSoFar = []

        #get second item in overall tuple which should be list up until this point
        prevPath = tile.[1]
        pathSoFar.append(prevPath)

        visited.append(tile[0])
        validSuccessors = []


        # print visited

        for x in problem.getSuccessors(tile[0]):
            if x[0] not in visited:

                validSuccessors.append(x)

        print "valid successors are ", validSuccessors

        ##########################
        # makes it run faster on tiny,medium,bigMazes
        ##########################
        #validSuccessors.reverse()

        for x in validSuccessors:
            queue.insert(0,x)

            if problem.isGoalState(x[0]):
                print queue
                return [s[1] for s in queue]

"""

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