from Classes import *


##Setup
#Create Players
player_one = Player("Percy")
player_two = Player("Johnny")

#Create (& Shuffle) Deck
new_deck = Deck()
new_deck.shuffle()

#Split Deck
for n in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

#The Biggest Threat in the History of Humanity: global game_over
game_over = False