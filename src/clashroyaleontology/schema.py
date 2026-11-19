from owlready2 import *
from base import onto

with onto:

    # TBox
    class Card(Thing):
        pass

    class Deck(Thing):
        pass

    class hasElixirCost(DataProperty, FunctionalProperty):
        domain = [Card]
        range = [int]

    class hasRarity(DataProperty, FunctionalProperty):
        domain = [Card]
        range = [str]

    class LegendaryCard(Card):
        equivalent_to = [Card & hasRarity.value("Legendary")]

    # Troop cards
    class TroopCard(Card):
        pass

    class TankCard(TroopCard):
        pass

    class BigTankCard(TankCard):
        pass

    class SwarmCard(TroopCard):
        pass

    # Spell cards
    class SpellCard(Card):
        pass

    class SmallSpellCard(SpellCard):
        pass

    class MediumSpellCard(SpellCard):
        pass

    class BigSpellCard(SpellCard):
        pass

    class DamagingSpellCard(SpellCard):
        pass

    class SmallRemovalSpellCard(SmallSpellCard, DamagingSpellCard):
        pass

    # Building cards
    class BuildingCard(Card):
        pass

    class SiegeBuildingCard(BuildingCard):
        pass

    class SpawnerBuildingCard(BuildingCard):
        pass

    # A card has one base type, so an air-targeting spell cannot count as a troop.
    AllDisjoint([TroopCard, SpellCard, BuildingCard])

    # Targeting types
    class AirTargetingCard(Card):
        pass

    class GroundTargetingCard(Card):
        pass

    class BuildingTargetingCard(Card):
        pass

    class RangedAttackCard(Card):
        pass

    class MeleeAttackCard(Card):
        pass

    # special categories of cards
    class SmallSpellBaitCard(Card):
        pass

    class MediumSpellBaitCard(Card):
        pass

    class WinConditionCard(Card):
        pass

    class SiegeSupportCard(Card):
        pass

    class TankAnswerCard(Card):
        pass

    class SwarmControlCard(Card):
        pass

    class SupportTroop(TroopCard):
        pass

    class AirDefenceCard(TroopCard, AirTargetingCard):
        equivalent_to = [TroopCard & AirTargetingCard]

    class GroundDefenceCard(TroopCard, GroundTargetingCard):
        equivalent_to = [TroopCard & GroundTargetingCard]

    class CounterPushTroop(TroopCard):
        pass

    class FlyingCard(Card):
        pass

    class CycleCard(Card):
        equivalent_to = [
            Card & hasElixirCost.some(ConstrainedDatatype(int, max_inclusive=2))
        ]

    class containsCard(ObjectProperty):
        domain = [Deck]
        range = [Card]

    class hasAverageElixirCost(DataProperty, FunctionalProperty):
        domain = [Deck]
        range = [float]

    # Deck definitions
    Deck.equivalent_to = [containsCard.exactly(8)]

    class F2PFriendlyDeck(Deck):
        equivalent_to = [Deck & containsCard.max(2, LegendaryCard)]

    class DeckWithAirCoverage(Deck):
        equivalent_to = [Deck & containsCard.some(AirTargetingCard)]

    class BalancedDeck(Deck):
        equivalent_to = [
            Deck
            & containsCard.some(WinConditionCard)
            & containsCard.some(AirDefenceCard)
            & containsCard.some(GroundTargetingCard)
            & containsCard.some(TankAnswerCard)
            & containsCard.some(SwarmControlCard)
            & containsCard.some(DamagingSpellCard)
        ]

    class CycleDeck(Deck):
        equivalent_to = [
            Deck
            & containsCard.some(WinConditionCard)
            & containsCard.min(3, CycleCard)
            & hasAverageElixirCost.some(ConstrainedDatatype(float, max_inclusive=3.5))
        ]

    class BeatdownDeck(Deck):
        equivalent_to = [
            Deck
            & containsCard.some(BigTankCard & WinConditionCard)
            & containsCard.min(2, SupportTroop)
            & containsCard.some(DamagingSpellCard)
        ]

    class SmallSpellBaitDeck(Deck):
        equivalent_to = [
            Deck
            & containsCard.some(WinConditionCard)
            & containsCard.min(3, SmallSpellBaitCard)
            & containsCard.some(SmallRemovalSpellCard)
        ]

    class MediumSpellBaitDeck(Deck):
        equivalent_to = [
            Deck
            & containsCard.some(WinConditionCard)
            & containsCard.min(3, MediumSpellBaitCard)
            & containsCard.some(DamagingSpellCard)
        ]

    class SiegeDeck(Deck):
        equivalent_to = [
            Deck
            & containsCard.some(SiegeBuildingCard & WinConditionCard)
            & containsCard.min(2, SiegeSupportCard)
            & containsCard.some(DamagingSpellCard)
        ]

    class CounterPushDeck(Deck):
        equivalent_to = [
            Deck
            & containsCard.some(WinConditionCard)
            & containsCard.min(2, CounterPushTroop)
            & containsCard.some(DamagingSpellCard)
        ]

    class MetaDeck(Deck):
        equivalent_to = [
            CycleDeck
            | BeatdownDeck
            | SmallSpellBaitDeck
            | MediumSpellBaitDeck
            | SiegeDeck
            | CounterPushDeck
        ]
