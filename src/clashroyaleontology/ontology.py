from owlready2 import *

onto = get_ontology("http://example.org/clash.owl")

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

    # ABox
    musketeer = AirTargetingCard("Musketeer")
    arrows = SpellCard("Arrows")

    deck1 = Deck("MusketeerDeck")
    deck1.containsCard = [card_a]

    sync_reasoner()

print(isinstance(deck1, DeckWithAirCoverage))

onto.save(file="clash.owl", format="rdfxml")
