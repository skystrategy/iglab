class EnvironmentField:
    def modulate(self, state, impulse):
        return impulse

#exmaple implementation of an environment field
class RepulsionField(EnvironmentField):
    def modulate(self, state, impulse):
        return impulse + self.force_at(state.x)
