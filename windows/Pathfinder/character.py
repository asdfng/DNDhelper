# Module used for recording player information

class Character:

    ''' When an object of this class is initialized, use MaxHP, name, and DR (if any)'''
    def __init__(self, **kwargs):
        self.MaxHP = kwargs.get("MaxHP", 0)
        self.DR = kwargs.get("DR", 0)
        self.Buffs = None

    @property
    def MaxHP(self):
        return self._MaxHP
    
    @MaxHP.setter
    def MaxHP(self, newHP):
        self._MaxHP = newHP

    @property
    def DR(self):
        return self._DR
    
    @DR.setter
    def DR(self, newDR):
        self._DR = newDR