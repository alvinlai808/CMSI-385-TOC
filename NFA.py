import re

class State:
    def __init__(self, name, is_accept = False):
        self.name = name
        self.is_accept = is_accept
        self.transitions = {}

    def add_transition(self, alphabet, next_state):
        self.transitions[alphabet] = next_state

    def get_transition(self, alphabet):
        return self.transitions.get(alphabet)

class Automata:
    def __init__(self, start_state, accept_states, transitions):
        self.start_state = State(name = start_state, is_accept = start_state in accept_states)
        self.states = {start_state : self.start_state}
        for transition in transitions:
            current_state, alphabet, next_state = transition

            if current_state not in self.states.keys():
                self.states[current_state] = State(name = current_state, is_accept = current_state in accept_states)

            if next_state not in self.states.keys():
                self.states[next_state] = State(name = next_state, is_accept = next_state in accept_states)

            self.states[current_state].add_transition(alphabet, self.states[next_state])

    def is_accept(self, string):
        current_state = self.start_state
        # TODO: check if necessary to follow all lambdas even with empty strings
        if len(string) == 0 and current_state.is_accept: 
            return True
        
        for char in string:
            checked_states = []
            while current_state.get_transition(char) is None:
                if current_state.get_transition(None) is None:
                    return False
                else:
                    next_state = current_state.get_transition(None)
                    if next_state in checked_states:
                        return False

                    checked_states.append(current_state)
                    current_state = next_state

            next_state = current_state.get_transition(char)
            if next_state is None:
                return False
            else:
                current_state = next_state

        checked_states = []
        while current_state.get_transition(None) is not None:
            next_state = current_state.get_transition(None)
            checked_states.append(current_state)
            current_state = next_state

        return current_state.is_accept

if __name__ == "__main__":
    while True:
        print('Enter the name of the start state in the form of a capital letter (ex. A)')
        start_state = input('ENTER START STATE NAME: ')
        if len(start_state) != 1 or not start_state.isalpha():
            print('Invalid state name')

        break

    print('\n')

    while True:
        print('Enter the name(s) of the accept state(s) in the form of a capital letter separated ' \
            'by spaces (ex. B C D)')
        accept_states = input('ENTER ACCEPT STATE NAME(S): ')
        if len(accept_states) == 0 or any(char.isdigit() for char in accept_states):
            print('Invalid state names')

        accept_states = list("".join(accept_states.split()))
        print(accept_states)
        
        break

    print('\n')

    while True:
        print('Enter transitions as 3-tuples. \n'
            'Every line represents a 3-tuple, and elements of the tuples are separated by spaces. \n'
            'Element 1 = current state name, element 2 = alphabet symbol, element 3 = next state name. \n'
            'Insert a blank line to mark the end of input.')
        transitions_list = []
        transitions = input('ENTER THE LIST OF 3-TUPLES: \n')
        while(transitions != ''):
            transitions_list.append(tuple(transitions.split()))
            transitions = input()

        break

    print('\n')

    print('Enter the string to test with the NFA')
    string_to_test = input('ENTER STRING: ')
    
    nfa = Automata(start_state = start_state, accept_states = accept_states, transitions = transitions_list)

    if nfa.is_accept(string_to_test):
        print('\nThe string was accepted by the NFA')
    else:
        print('\nThe string was rejected by the NFA')
    
    # nfa = Automata("A", ["A", "B"], [("A", "0", "B"), ("A", "1", "A"), ("B", "1", "A")])
    # print(nfa.is_accept("1001"))
    # print(nfa.is_accept("1"))
    # print(nfa.is_accept("0"))
    # print(nfa.is_accept("00"))
    # print(nfa.is_accept(""))

    # nfa = Automata("A", ["B"], [("A", "0", "B")])
    # print(nfa.is_accept(""))
    # print(nfa.is_accept("1001"))
    # print(nfa.is_accept("1"))
    # print(nfa.is_accept("0"))
    # print(nfa.is_accept("00"))

