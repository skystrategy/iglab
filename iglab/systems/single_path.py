import copy

from iglab.core.evolution import EvolutionStep
from iglab.core.integrator import EulerIntegrator


class SinglePathSystem:
    """
    Single impulse-driven trajectory in R^n.
    """

    def __init__(self, initial_state, impulse_fn, dt=0.01):
        self.state = initial_state
        self.dt = dt

        self.evolution = EvolutionStep(
            impulses=[impulse_fn],
            environments=[],
            integrator=EulerIntegrator()
        )

        self.history = []

    def step(self):
        # IMPORTANT: snapshot state
        self.history.append(copy.deepcopy(self.state))
        self.state = self.evolution.advance(self.state, self.dt)

    def run(self, n_steps):
        for _ in range(n_steps):
            self.step()

    def trajectory(self):
        return [s.x for s in self.history]
