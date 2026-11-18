from base import onto
from schema import *

with onto:
    arrows = SpellCard("Arrows")
    # ABox
    musketeer = AirTargetingCard("Musketeer")
    arrows = SpellCard("Arrows")

    deck1 = Deck("MusketeerDeck")
    deck1.containsCard = [musketeer]
