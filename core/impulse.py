class ImpulseField:
    def evaluate(self, state):
        raise NotImplementedError

#example implementation of an impulse field
class CurvatureImpulse(ImpulseField):
    def __init__(self, kappa_fn):
        self.kappa_fn = kappa_fn

    def evaluate(self, state):
        return self.kappa_fn(state.s)
