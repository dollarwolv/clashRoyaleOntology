from owlready2 import *

onto = get_ontology("http://example.org/clash.owl")

with onto:

    class Card(Thing):
        pass

    class AirTargetingCard(Card):
        pass

    class Deck(Thing):
        pass

    class containsCard(ObjectProperty):
        domain = [Deck]
        range = [Card]

    class DeckWithAirCoverage(Deck):
        equivalent_to = [Deck & containsCard.some(AirTargetingCard)]

    card_a = AirTargetingCard("Musketeer")
    deck1 = Deck("MusketeerDeck")
    deck1.containsCard = [card_a]

    sync_reasoner()

print(isinstance(deck1, DeckWithAirCoverage))

onto.save(file="clash.owl", format="rdfxml")
