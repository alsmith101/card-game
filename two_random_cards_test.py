import two_random_cards
import unittest


class TestCardGameApp(unittest.TestCase):

    def test_create_deck_of_cards(self):
        card_deck_output = two_random_cards.create_deck_of_cards()
        self.assertEqual(len(card_deck_output), 52, "Should be 52")


if __name__ == '__main__':
    unittest.main()
