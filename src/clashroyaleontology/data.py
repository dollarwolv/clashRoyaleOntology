from base import onto
from schema import *


def create_card(name, *categories, **attributes):
    card = Card(name, **attributes)
    card.is_a.extend(categories)
    return card


with onto:
    # ABox: one example deck using costs and rarities from the group catalogue.
    musketeer = create_card(
        "Musketeer",
        TroopCard,
        AirTargetingCard,
        SupportTroop,
        MediumSpellBaitCard,
        hasElixirCost=3,
        hasRarity="Rare",
    )

    arrows = create_card(
        "Arrows",
        SmallRemovalSpellCard,
        AirTargetingCard,
        SwarmControlCard,
        hasElixirCost=3,
        hasRarity="Common",
    )

    hog_rider = create_card(
        "HogRider", TroopCard, WinConditionCard, hasElixirCost=4, hasRarity="Rare"
    )

    cannon = create_card(
        "Cannon",
        BuildingCard,
        TankAnswerCard,
        hasElixirCost=3,
        hasRarity="Common",
    )

    skeletons = create_card("Skeletons", SwarmCard, hasElixirCost=1, hasRarity="Common")
    ice_spirit = create_card(
        "IceSpirit", TroopCard, hasElixirCost=1, hasRarity="Common"
    )
    ice_golem = create_card("IceGolem", TankCard, hasElixirCost=2, hasRarity="Rare")
    mini_pekka = create_card(
        "MiniPEKKA", TankCard, TankAnswerCard, hasElixirCost=4, hasRarity="Rare"
    )

    cards = [
        musketeer,
        arrows,
        hog_rider,
        cannon,
        skeletons,
        ice_spirit,
        ice_golem,
        mini_pekka,
    ]

    AllDifferent(cards)
    deck1 = Deck("MusketeerDeck", containsCard=cards)

    # OWL checks the average against 3.5. Python calculates it from the card costs.
    costs = [card.hasElixirCost for card in cards]
    deck1.hasAverageElixirCost = sum(costs) / len(costs)
