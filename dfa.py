"""
Deterministic Finite Automata

Example from Stanford online automata theory course by Jeff Ullman:

strings of {0,1} that do not contain consecutive 1's

>>> states = [
...     {'name': 'A', 'accepting': True, 'transitions': {'0': 'A', '1': 'B'}},
...     {'name': 'B', 'accepting': True, 'transitions': {'0': 'A', '1': 'dead'}},
...     {'name': 'dead', 'accepting': False, 'transitions': {'0': 'dead', '1': 'dead'}}
... ]

>>> g = make_graph(states)

>>> start = g['A']

>>> transition(start, '0000100111000')
<State name=dead accepting=False>

>>> transition(start,'1000000')
<State name=A accepting=True>

>>> transition(start,'1000001')
<State name=B accepting=True>

"""


class Node(object):
    def __init__(self, name, accepting=True, adjacent=None):
        self.name = name
        self.accepting = accepting
        
        if adjacent is None:
            self.adjacent = {}
            
    def __repr__(self):
        return '<State name={} accepting={}>'.format(self.name, self.accepting)


def make_graph(states):
    state_registry = {}
    
    for state in states:
        name = state['name']
        accepting = state['accepting']
        state_registry[name] = Node(name, accepting=accepting)
            
    for state in states:
        transitions = state['transitions']
        node = state_registry[state['name']]

        for letter in transitions:
            node.adjacent[letter] = state_registry[transitions[letter]]
            
    return state_registry


def transition(state, string):
    for letter in string:
        state = state.adjacent[letter]
        
    return state
