# Jaxon Snow
# Blackjack
# 1/21

import random
import Cards as m_cards
import gamefunctions as gf

class BJ_Cards(m_cards.Pos_card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Cards.RANK.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v
class BJ_Deck(m_cards.Deck):
    def populate(self):
        for suit in BJ_Cards.SUIT:
            for rank in BJ_Cards.RANK:
                self.cards.append(BJ_Cards(rank, suit))


class BJ_Hand(m_cards.Hand):
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name
    def __str__(self):
        rep = ""
        for i in range(len(self.cards)):
            print(self.cards[i])
        rep = self.name + ":\n" + "Total: " + str(self.total)
        return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        t = 0
        for card in self.cards:
            t += card.value
        ace_in_hand = False

        for card in self.cards:
            if card.value == BJ_Cards.ACE_VALUE:
                    ace_in_hand = True
        if ace_in_hand and t <= 11:
            t += 10
        return t

    def is_busted(self):
        return self.total > 21


class BJ_Player(BJ_Hand):
    def is_Hitting(self):
        response = gf.ask_yes_no(self.name+ "so you want a hit? (Y/N):")
        return response == "y"
    def bust(self):
        print(self.name, "busts.")
        self.lose()
    def lose(self):
        print(self.name, "loses.")
    def win(self):
        print(self.name, "wins")
    def push(self):
        print(self.name, "pushes.")

class BJ_Dealer(BJ_Hand):
    def is_Hitting(self):
        return self.total < 17
    def bust(self):
        print(self.name, "busts.")
    def flip_first_card(self):
        self.cards[0].flip()

class BJ_Game(object):
    def __init__(self,names):
        self.players = []
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
        self.dealer = BJ_Dealer("Dealer")
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)


    @property
    def still_playing(self):
        sp = []
        for player in self.players():
         if not player.is_busted():
             sp.append(player)
        return sp
    def __additional_cards(self,player):
        while not player.is_busted() and player.is_Hitting():
            self.deck.deal([player], 1)
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)

        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()
        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)
            if self.dealer.is_busted():
                for player in self.still_playing:
                    player.win()
            else:
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
            for player in self.players:
                player.clear()
            self.dealer.clear()


def main():
    print("\t\tWelcome to Blackjack!\n")



    names = []
    number = gf.ask_number("how many players? (1-7): " , low = 1, high = 8)
    for i in range(number):
        name = input("Enter players name: ")
        names.append(name)

    game = BJ_Game(names)
    again = None
    while again != "n":
        game.play()
        again= gf.ask_yes_no(("\n Do you want to keep playing?"))
main()











