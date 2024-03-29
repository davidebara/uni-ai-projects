# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import Stack, Queue, PriorityQueue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    "util.raiseNotDefined()"

    # REZOLVARE
    # 1. Definirea variabilelor
    """
    ● noduri_vizitate:
        folosim un set deoarece nodurile sunt unice si la final nu ne intereseaza
        ordinea in care le-am vizitat, intrucat avem aceasta informatie in cale
    ● noduri:
        contine nodurile pe care trebuie sa le traversam pornind de la o stare initiala
        obtinuta prin functia getStartState()
    ● cai:
        contine caile pana la noduri, prima cale fiind o lista goala deoarece nu am mers
        la niciun nod
    """

    noduri_vizitate = set()
    noduri = Stack()
    cai = Stack()
    noduri.push(problem.getStartState())
    cai.push([])

    # 2. Parcurgerea nodurilor din graf si gasirea drumului pana la nodul Goal
    """
    ● daca avem noduri in graf le scoatem si stocam cele doua informatii despre ele
      (nodul si calea pana la el) in doua variabile
        ● in cazul in care am ajuns la nodul Goal returnam calea pana la el
        ● altfel daca nodul respectiv nu a fost vizitat il adaugam in set si realizam
          actiunile necesare pentru parcurgerea sa corecta:
            ● il adaugam in set-ul nodurilor vizitate
            ● functia getSuccesors(nod_curent) va returna un triplu cu succesorul
              (urmatoarul nod), actiune (actiunea pe care trebuie sa o facem
              pentru a ajunge la el) si cost_actiune (cat ne va costa aceasta actiune)
            ● stocam aceste elemente in 3 variabile
            ● pentru fiecare succesor care nu a fost vizitat facem push in stivele
              noastre, unde adaugam elementul respectiv si calea pana la el (cale
              este calea pana la punctul in care am ajuns + actiune care este
              actiunea pe care trebuie sa o facem pentru a ajunge acolo)
    """
    while not noduri.isEmpty():
        nod_curent = noduri.pop()
        cale = cai.pop()

        if problem.isGoalState(nod_curent):
            return cale

        if nod_curent not in noduri_vizitate:
            noduri_vizitate.add(nod_curent)
            for succesor, actiune, cost_actiune in problem.getSuccessors(nod_curent):
                if succesor not in noduri_vizitate:
                    noduri.push(succesor)
                    cai.push(cale + [actiune])
    return []


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    "util.raiseNotDefined()"

    # REZOLVARE
    # 1. Definirea variabilelor
    """
    ● noduri_vizitate:
        folosim un set deoarece nodurile sunt unice si la final nu ne intereseaza
        ordinea in care le-am vizitat, intrucat avem aceasta informatie in cale
    ● noduri:
        contine nodurile pe care trebuie sa le traversam pornind de la o stare initiala
        obtinuta prin functia getStartState()
    ● cai:
        contine caile pana la noduri, prima cale fiind o lista goala deoarece nu am mers
        la niciun nod
    """

    noduri_vizitate = []
    noduri = Queue()
    cai = Queue()
    noduri.push(problem.getStartState())
    cai.push([])

    # 2. Parcurgerea nodurilor din graf si gasirea drumului pana la nodul Goal
    """
    ● daca avem noduri in graf le scoatem si stocam cele doua informatii despre ele
      (nodul si calea pana la el) in doua variabile
        ● in cazul in care am ajuns la nodul Goal returnam calea pana la el
        ● altfel daca nodul respectiv nu a fost vizitat il adaugam in set si realizam
          actiunile necesare pentru parcurgerea sa corecta:
            ● il adaugam in set-ul nodurilor vizitate
            ● functia getSuccesors(nod_curent) va returna un triplu cu succesorul
              (urmatoarul nod), actiune (actiunea pe care trebuie sa o facem
              pentru a ajunge la el) si cost_actiune (cat ne va costa aceasta actiune)
            ● stocam aceste elemente in 3 variabile
            ● pentru fiecare succesor care nu a fost vizitat facem push in stivele
              noastre, unde adaugam elementul respectiv si calea pana la el (cale
              este calea pana la punctul in care am ajuns + actiune care este
              actiunea pe care trebuie sa o facem pentru a ajunge acolo)
    """
    while not noduri.isEmpty():
        nod_curent = noduri.pop()
        cale = cai.pop()

        if problem.isGoalState(nod_curent):
            return cale

        if nod_curent not in noduri_vizitate:
            noduri_vizitate.add(nod_curent)
            for succesor, actiune, cost_actiune in problem.getSuccessors(nod_curent):
                if succesor not in noduri_vizitate:
                    noduri.push(succesor)
                    cai.push(cale + [actiune])
    return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # REZOLVARE
    # 1. Definirea variabilelor
    """
    ● noduri_vizitate:
        folosim un set deoarece nodurile sunt unice si la final nu ne intereseaza
        ordinea in care le-am vizitat, intrucat avem aceasta informatie in cale
    ● noduri:
        contine nodurile pe care trebuie sa le traversam pornind de la o stare initiala
        obtinuta prin functia getStartState()
        fiind un Priority Queue trebuie sa specificam si elementul in functie de care
        ordonam lista, acesta fiind costul pana la un anumit nod (acesta este 0 pentru
        nodul de inceput)
    ● cai:
        contine caile pana la noduri, prima cale fiind o lista goala deoarece nu am mers
        la niciun nod
    """

    noduri_vizitate = []
    noduri = PriorityQueue()
    cai = PriorityQueue()
    noduri.push(problem.getStartState(), 0)
    cai.push([], 0)

    # 2. Parcurgerea nodurilor din graf si gasirea drumului pana la nodul Goal
    """
    ● daca avem noduri in graf le scoatem si stocam cele doua informatii despre ele
      (nodul si calea pana la el) in doua variabile
        ● in cazul in care am ajuns la nodul Goal returnam calea pana la el
        ● altfel daca nodul respectiv nu a fost vizitat il adaugam in set si realizam
          actiunile necesare pentru parcurgerea sa corecta:
            ● il adaugam in set-ul nodurilor vizitate
            ● functia getSuccesors(nod_curent) va returna un triplu cu succesorul
              (urmatoarul nod), actiune (actiunea pe care trebuie sa o facem
              pentru a ajunge la el) si cost_actiune (cat ne va costa aceasta actiune)
            ● stocam aceste elemente in 3 variabile
            ● pentru fiecare succesor care nu a fost vizitat:
                ● calculam costul pentru calea pana la nodul respectiv
                ● facem push in stivele noastre, unde adaugam elementul respectiv si
                  calea pana la el (cale este calea pana la punctul in care am ajuns
                  + actiune care este actiunea pe care trebuie sa o facem pentru a
                  ajunge acolo)
                ● asa cum am spus, intrucat folosim un Priority Queue trebuie sa
                  mentionam si elementul in functie de care ordonam coada, acesta
                  fiind costul pana la notul nedescoperit
    """
    while not noduri.isEmpty():
        nod_curent = noduri.pop()
        cale = cai.pop()

        if problem.isGoalState(nod_curent):
            return cale

        if nod_curent not in noduri_vizitate:
            noduri_vizitate.add(nod_curent)
            for succesor, actiune, cost_actiune in problem.getSuccessors(nod_curent):
                if succesor not in noduri_vizitate:
                    cale_noua = cale + [actiune]
                    cost_total = problem.getCostOfActions(cale_noua)
                    noduri.push(succesor, cost_total)
                    cai.push(cale_noua, cost_total)
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem. This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # REZOLVARE
    # 1. Definirea variabilelor
    """
    ● noduri_vizitate:
        folosim un set deoarece nodurile sunt unice si la final nu ne intereseaza
        ordinea in care le-am vizitat, intrucat avem aceasta informatie in cale
    ● noduri:
        contine nodurile pe care trebuie sa le traversam pornind de la o stare initiala
        obtinuta prin functia getStartState()
        fiind un Priority Queue trebuie sa specificam si elementul in functie de care
        ordonam lista, acesta fiind costul pana la un anumit nod (acesta este 0 pentru
        nodul de inceput)
    ● cai:
        contine caile pana la noduri, prima cale fiind o lista goala deoarece nu am mers
        la niciun nod
    """
    noduri_vizitate = []
    noduri = PriorityQueue()
    cai = PriorityQueue()
    noduri.push(problem.getStartState(), 0)
    cai.push([], 0)


    # 2. Parcurgerea nodurilor din graf si gasirea drumului pana la nodul Goal
    """
    ● daca avem noduri in graf le scoatem si stocam cele doua informatii despre ele
      (nodul si calea pana la el) in doua variabile
        ● in cazul in care am ajuns la nodul Goal returnam calea pana la el
        ● altfel daca nodul respectiv nu a fost vizitat il adaugam in set si realizam
          actiunile necesare pentru parcurgerea sa corecta:
            ● il adaugam in set-ul nodurilor vizitate
            ● functia getSuccesors(nod_curent) va returna un triplu cu succesorul
              (urmatoarul nod), actiune (actiunea pe care trebuie sa o facem
              pentru a ajunge la el) si cost_actiune (cat ne va costa aceasta actiune)
            ● stocam aceste elemente in 3 variabile
            ● pentru fiecare succesor care nu a fost vizitat:
                ● calculam costul pentru calea pana la nodul respectiv, de data aceasta
                  adaugand si euristica utilizata
                ● facem push in stivele noastre, unde adaugam elementul respectiv si
                  calea pana la el (cale este calea pana la punctul in care am ajuns
                  + actiune care este actiunea pe care trebuie sa o facem pentru a
                  ajunge acolo)
                ● asa cum am spus, intrucat folosim un Priority Queue trebuie sa
                  mentionam si elementul in functie de care ordonam coada, acesta
                  fiind costul pana la notul nedescoperit
    """
    while not noduri.isEmpty():
        nod_curent = noduri.pop()
        cale = cai.pop()

        if problem.isGoalState(nod_curent):
            return cale

        if nod_curent not in noduri_vizitate:
            noduri_vizitate.add(nod_curent)
            for succesor, actiune, cost_actiune in problem.getSuccessors(nod_curent):
                if succesor not in noduri_vizitate:
                    cale_noua = cale + [actiune]
                    cost_total = problem.getCostOfActions(cale_noua) + heuristic(succesor, problem)
                    noduri.push(succesor, cost_total)
                    cai.push(cale_noua, cost_total)
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch