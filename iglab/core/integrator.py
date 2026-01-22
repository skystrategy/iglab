from iglab.core.state import State
import numpy as np

class EulerIntegrator(Integrator):
    def step(self, state, impulse, dt):
        """
        impulse is a tuple: (rho, kappa)
        """
        rho, kappa = impulse

        x_new = state.x + dt * rho * np.array([
            np.cos(state.theta),
            np.sin(state.theta)
        ])

        theta_new = state.theta + dt * kappa

        return State(
            x=x_new,
            s=state.s + dt,
            rho=rho,
            theta=theta_new
        )
