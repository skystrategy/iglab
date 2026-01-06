class Integrator:
    def step(self, state, impulse, dt):
        raise NotImplementedError

# example implementation of an integrator
class EulerIntegrator(Integrator):
    def step(self, state, impulse, dt):
        new_x = state.x + impulse * dt
        return State(new_x, s=state.s + dt)
