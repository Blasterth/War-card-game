import CONSTANTS


#Card Class
class Card():
    #Attributes
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = CONSTANTS.VALUE_DICTIONARY[rank]
        #Check if cards are okay
        if self.rank not in CONSTANTS.RANK_LIST:
            raise Exception("ranks are based on the letters/numbers on the top right of real cards.")
        elif self.suit not in CONSTANTS.SUIT_LIST:
            raise Exception("We don't have such a suit\nCheck the sppelling/Casing.")
    #Name of the card
    def __str__(self):
        return f"{self.rank} of {self.suit}"


#Deck Class
class Deck():
    #Attributes
    def __init__(self):
        self.contents = []
        for suit in CONSTANTS.SUIT_LIST:
            for rank in CONSTANTS.RANK_LIST:
                self.contents.append(Card(rank,suit))
    #Number of Cards Remaining
    def number_of_cards_remaining(self):
        return f"{len(self.contents)} cards remaining."
    #Shuffle
    def shuffle(self):
        self.contents = set(self.contents)
        self.contents = list(self.contents)
    #Cards Remaining
    def __str__(self):
        return str(self.contents)


#Player Deck Class
class PlayerDeck(Deck):
    #Attributes
    def __init__(self):
        self.deck_contents = Deck.contents[0:26]
    #Battle: Draw a card and play it against CPU
    def battle(self):
        self.contents.remove(0)
    #War: Wager 3 cards when both players play cards with equal values
    def war(self):
        self.contents.remove(0),self.contents.remove(1),self.contents.remove(2)
    #Cards Remaining
    def __str__(self):
        return self.deck_contents

parsa_deck = Deck()
parsa_deck.shuffle()
print(parsa_deck.contents[0])