class Frogs():
    all = []

    def __init__(self, name, type):
        self._name = name
        self._type = type
        self.save()

    def save(self):
        all.append(self)

