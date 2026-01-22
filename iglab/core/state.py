class State:
    """
    Instantaneous IG state.

    x     : position in R^n (shape space)
    s     : generative parameter
    rho   : impulse magnitude
    theta : impulse orientation
    """

    def __init__(self, x, s=0.0, rho=1.0, theta=0.0):
        self.x = x
        self.s = s
        self.rho = rho
        self.theta = theta
