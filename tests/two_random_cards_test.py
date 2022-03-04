import src.two_random_cards
import unittest


class TestCardGameApp1(unittest.TestCase):

    def setUp(self):
        self.card_deck = two_random_cards.create_deck_of_cards()

    def test_create_deck_of_cards(self):
        self.assertEqual(len(self.card_deck), 52, "Should be 52")

    # ensure that we get 4 jack cards one for each suit
    def test_create_deck_of_cards_count_jacks(self):
        jacks = [card for card in self.card_deck if "Jack" in card]
        self.assertEqual(len(jacks), 4, "Should be 4")

    # ensure that we get 4 "two" cards one for each suit
    def test_create_deck_of_cards_count_twos(self):
        jacks = [card for card in self.card_deck if "2" in card]
        self.assertEqual(len(jacks), 4, "Should be 4")


class TestCardGameApp2(unittest.TestCase):

    def setUp(self):
        self.card_deck = [i for i in range(52)]
        self.shuffled_card_deck = two_random_cards.shuffle_deck(self.card_deck)

    # ensure that we get 52 cards back from the shuffling
    def test_shuffle_deck(self):
        self.assertEqual(len(self.shuffled_card_deck), 52, "Should be 52")


if __name__ == '__main__':
    unittest.main()
