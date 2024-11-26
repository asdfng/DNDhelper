import effects
# Module used for recording player information

class Character:

    ''' When an object of this class is initialized, use MaxHP, name, and DR (if any)'''
    def __init__(self, **kwargs):
        self._MaxHP = kwargs.get("MaxHP", 0)
        self._Effects = []

    @property
    def MaxHP(self):
        return self._MaxHP
    
    @MaxHP.setter
    def MaxHP(self, newHP):
        self._MaxHP = newHP

    @property
    def Effects(self):
        return self._Effects
    
    @Effects.setter
    def Effects(self, **kwargs):
        new_effect = effects.Effect(**kwargs)
        self._Effects.append(new_effect)

    def update_Effects(self):
        pass
