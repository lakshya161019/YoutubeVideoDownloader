class Fantasy:
    def __init__(self, name, team, type, iscaptin, runs, wickets):
        self.name = name
        self.team = team
        self.type = type
        self.iscaptin = iscaptin
        self.runs = runs
        self.wickets = wickets

        def calculatePoints(self, points):
            if self.iscaptin:
                return (runs + (wickets * points))*2
            else:
                return (runs + (wickets * points))


class My_dict(dict):
    def _init_(self):
        self = dict()

    def findPlayerPoints(self, fantasypoint):
        self = dict()
        self[name] = fantasypoint
        return {name: fantasypoint}


Player1 = Fantasy("Virat","RCB")