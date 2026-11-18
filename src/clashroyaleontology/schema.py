from owlready2 import *
from base import onto

with onto:

    # TBox
    class Card(Thing):
        pass

    class Deck(Thing):
        pass

    # Types of cards
    class AirTargetingCard(Card):
        pass

    class SpellCard(Card):
        pass

    class GroundTroopCard(Card):
        pass

    class TankCard(Card):
        pass

    class SwarmCard(Card):
        pass

    class FlyingCard(Card):
        pass

    class containsCard(ObjectProperty):
        domain = [Deck]
        range = [Card]

    class DeckWithAirCoverage(Deck):
        equivalent_to = [Deck & containsCard.some(AirTargetingCard)]
