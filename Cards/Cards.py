# Jaxon Snow
# 12/20
# Card starting module

import random

class Card(object):
    RANK = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUIT = ["♥", "♦", "♣", "♠"]



    def __init__(self, RANK, SUIT):
        self.rank = RANK
        self.suit = SUIT

    def __str__(self):
        rep = str.format(""""
        +----------+
        | {0:<2}{1}      |
        |          |
        |          |
        |          |
        |       {1}{0:>2}|
        +----------+
        """,self.rank,self.suit)
        return rep
class Hand(object):
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card)
        else:
            rep = "<  Empty  >"

        return rep
    def clear(self):
        self.cards = []
    def add(self,card):
        self.cards.append(card)



    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self,handsList,per_hand = 1):
        for rounds in range(per_hand):
            for hand in handsList:
                if self.cards:
                    topcard = self.cards[0]
                    self.give(topcard, hand)
                else:
                    print("out of cards")
                    for hand in handsList:
                        hand.clear()
                    self.clear()
                    self.populate()
                    self.shuffle()
                    self.deal(handsList,per_hand)

    def populate(self):
        for suit in Card.SUIT:
            for rank in Card.RANK:
                self.add(Card(rank,suit))


class Pos_card(Card):

    def __init__(self, rank, suit, face_up=True):
        super(Pos_card, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = str.format(""""
            +----------+
            | {0:<2}{1}      |
            |          |
            |          |
            |          |
            |       {1}{0:>2}|
            +----------+
            """, self.rank, self.suit)
            return rep
        else:
            rep = str.format("""
            +----------+
            |++++++++++|
            |++++++++++|
            |++++++++++|
            |++++++++++|
            |++++++++++|
            +----------+
            """, self.rank, self.suit)
        return rep
    def flip(self):
        self.is_face_up = not self.is_face_up



if __name__ == "__Main__":
    print("this is a module for playing cards. not ment to be ran an its own")
    input("\n\nPress the enter key to exit.")

