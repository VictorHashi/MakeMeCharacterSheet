import json

class Feat:

    def __init__(self, name, desc, cost, stacks, requirement):
        self.name = name
        self.desc = desc
        self.cost = cost
        self.stacks = stacks
        self.requirement = requirement if requirement else []; 

    @staticmethod
    def load_from_file(path):
        with open(path, 'r') as f:
            data = json.load(f)
        return Feat(**data)