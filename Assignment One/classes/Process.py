from classes.Draw import Draw

class Process:
    def __init__(self, initial_state, final_state):
        self.initial_state = initial_state
        self.graphing = Draw()
        self.graph = self.graphing.get_graph()
        self.final_state = final_state

    def goal_test(self, state):
        return state == self.final_state



