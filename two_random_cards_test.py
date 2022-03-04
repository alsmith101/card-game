import two_random_cards
import unittest


class TestCardGameApp(unittest.TestCase):

    def setUp(self):
        self.card_deck = two_random_cards.create_deck_of_cards()

    def test_create_deck_of_cards(self):
        self.assertEqual(len(self.card_deck), 52, "Should be 52")

    def test_create_deck_of_cards_count_jacks(self):
        jacks = [card for card in self.card_deck if "Jack" in card]
        self.assertEqual(len(jacks), 4, "Should be 4")

    def test_create_deck_of_cards_count_twos(self):
        jacks = [card for card in self.card_deck if "2" in card]
        self.assertEqual(len(jacks), 4, "Should be 4")

    # def test_shuffle_deck(self):
    #     print(self.shuffled_card_deck)
    #     self.assertEqual(len(self.shuffled_card_deck), 52, "Should be 52")
    #
    # def test_shuffle_deck_count_jacks(self):
    #     jacks = [card for card in self.shuffled_card_deck if "Jack" in card]
    #     self.assertEqual(len(jacks), 4, "Should be 4")


if __name__ == '__main__':
    unittest.main()
