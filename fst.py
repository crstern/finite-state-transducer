import json
from pprint import pprint

class FST:
    def __init__(self, number_of_states=None, input_alphabet=None, output_alphabet=None,
                 initial_state=None, final_states=None, delta=None):
        self.number_of_states = number_of_states
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet
        self.initial_state = initial_state
        self.current_states = [initial_state]
        self.final_states = final_states
        self.delta = delta

    def read_data(self, path="transducer.json"):
        with open(path) as f:
            data = json.load(f)
        self.input_alphabet = set(data['input_alphabet'])
        self.number_of_states = data["number_of_states"]
        self.output_alphabet = set(data["output_alphabet"])
        self.initial_state = (data["initial_state"], "")
        self.current_states = [(data["initial_state"], "")] # un tuplu format din starea curenta si cuvantul obtinut
                                                            # pana la acel moment
        self.final_states = set(data["final_states"])
        self.delta = {}
        for transition in data["delta"].items(): # creez functia de tranzitie sub forma unui dictionar
            key = tuple(transition[0].split())
            self.delta[key] = [tuple(s.split()) for s in transition[1]]

    def __str__(self):
        pprint(self.__dict__)
        return ""

    def status(self):
        pprint(self.current_states)

    def reset(self):
        self.current_states = [self.initial_state]

    def move(self, char):
        new_current_states = []
        for state, word in self.current_states:
            try:
                state_char_list = self.delta[(str(state), char)]
            except KeyError:
                continue

            for state_char_tulpe in state_char_list:
                new_state, new_char = state_char_tulpe
                new_current_states.append((new_state, word + new_char))
        self.current_states = new_current_states



