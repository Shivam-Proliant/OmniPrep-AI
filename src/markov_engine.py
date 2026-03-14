import numpy as np

class MarkovProficiencyScale:
    def __init__(self):
        # States: 0 (Beginner), 1 (Intermediate), 2 (Advanced), 3 (Mastery)
        self.states = [0, 1, 2, 3]
        
        # Transition Probabilities: [Current State][Next State]
        # P(Next | Current, Correct=True)
        self.transition_correct = np.array([
            [0.2, 0.8, 0.0, 0.0], # Beginner getting it right shifts to Intermediate
            [0.0, 0.3, 0.7, 0.0],
            [0.0, 0.0, 0.4, 0.6],
            [0.0, 0.0, 0.0, 1.0]
        ])
        
        # P(Next | Current, Correct=False)
        self.transition_incorrect = np.array([
            [1.0, 0.0, 0.0, 0.0],
            [0.6, 0.4, 0.0, 0.0], # Intermediate getting it wrong drops to Beginner
            [0.0, 0.5, 0.5, 0.0],
            [0.0, 0.0, 0.7, 0.3]
        ])

    def get_next_state(self, current_state: int, is_correct: bool) -> int:
        matrix = self.transition_correct if is_correct else self.transition_incorrect
        probabilities = matrix[current_state]
        # Probabilistic state transition based on Markov matrix
        next_state = np.random.choice(self.states, p=probabilities)
        return int(next_state)
