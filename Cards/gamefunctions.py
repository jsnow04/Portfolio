def ask_number (question,low,high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high) :
        response = int(input(question))
    return response
def ask_yes_no(question):
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response


class Player(object):
    def __init__(self,name):
        self.name = name
        self.score = Score()
        self.isAlive = True
        self.lifes = 3


class Score(object):
    def __init__(self):
        self.score = 0


    def add_to_score(self,points):
        self.score += points


    def Take_points(self,points):
        self.score -= points
        if self.points <0:
            self.score = 0


if __name__ == "__Main__":
    print("you ran this module directly(and did not 'import' it).")
    input("\n\nPress the enter key to exit.")