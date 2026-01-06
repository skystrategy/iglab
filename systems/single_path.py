from iglab.core.state import State
from iglab.core.impulse_field import ImpulseField
from iglab.core.integrator import Integrator
from iglab.core.evolution_step import EvolutionStep

class SinglePathSystem:
    """
    Implements the impulse-driven single trajectory
    defined in Section X of the foundational paper.
    """

    def __init__(self, initial_state, impulses, integrator, dt):
        self.state = initial_state
        self.step = EvolutionStep(
            impulses=impulses,
            environments=[],
            integrator=integrator
        )
        self.dt = dt
        self.history = []

    def advance(self, n_steps=1):
        for _ in range(n_steps):
            self.history.append(self.state)
            self.state = self.step.advance(self.state, self.dt)

    def trajectory(self):
        return [s.x for s in self.history]
