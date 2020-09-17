
class Horse:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name

reiji = Rider("SUZUKI REIJI")
horse = Horse("reiji", reiji)

horse.owner.name
