class State:
    def __init__(self, x, theta=None, s=0.0, meta=None):
        self.x = x              # position vector
        self.theta = theta      # orientation / heading
        self.s = s              # generative parameter
        self.meta = meta or {}  # optional internal state
