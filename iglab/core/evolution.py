import numpy as np


class EvolutionStep:
    """
    One causal IG evolution step:
    - evaluate impulses
    - apply environments
    - integrate
    """

    def __init__(self, impulses, environments, integrator):
        self.impulses = impulses
        self.environments = environments
        self.integrator = integrator

    def advance(self, state, dt):
        # 1. evaluate impulses at current state
        impulse = np.zeros_like(state.x)
        for impulse_fn in self.impulses:
            impulse += impulse_fn(state)

        # 2. apply environments (none yet)
        for env in self.environments:
            impulse = env.modulate(state, impulse)

        # 3. integrate
        return self.integrator.step(state, impulse, dt)
