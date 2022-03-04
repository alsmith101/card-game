import random

suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
non_digit_cards = ["King", "Queen", "Jack", "Ace"]
digit_cards = list(range(2, 11))


def create_deck_of_cards():
    return [str(card) + " of " + s for s in suits for card in (non_digit_cards + digit_cards)]


def shuffle_deck(deck):
    shuffled_deck = []
    while len(deck) > 0:
        card = random.choice(deck)
        shuffled_deck.append(card)
        deck.remove(card)
    return shuffled_deck


def pick_random_card(deck):
    return random.choice(deck)


def main():
    # create a standard card deck of 52 cards
    card_deck = create_deck_of_cards()

    # shuffle the cards
    shuffled_card_deck = shuffle_deck(card_deck)

    # pick a random card from the new pack
    random_card1 = pick_random_card(shuffled_card_deck)

    # remove random card from the pack
    shuffled_card_deck.remove(random_card1)

    # pick a second random card
    random_card2 = pick_random_card(shuffled_card_deck)

    # print out the picked cards
    print(random_card1, random_card2)


if __name__ == "__main__":
    main()


