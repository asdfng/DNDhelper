import modifiers
import duration

class Effect:

    '''This class is just a container for Duration and Modifiers, as of writing this it shouldn't have anything\
        else.'''
    
    def __init__(self, **kwargs):
        self._duration = None
        self._modifier = None

    @property
    def duration(self):
        return self._duration