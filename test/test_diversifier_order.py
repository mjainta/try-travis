"""
Tests for the diversifier which work with the order of characters
"""

import unittest

from strdiver.diversifier import Diversifier


class TestDiversifierOrder(unittest.TestCase):
    """
    Holds test methods
    """

    def test_reverse_single_char(self):
        """
        String should stay the same if only one char
        """
        diversifier = Diversifier('x')
        self.assertEqual('x', diversifier.reverse())

    def test_reverse_three_chars(self):
        """
        String should be returned in reversed order
        """
        diversifier = Diversifier('abc')
        self.assertEqual('cba', diversifier.reverse())

    def test_reverse_same_chars(self):
        """
        String should be returned in reversed order
        Even if there are chars twice
        """
        diversifier = Diversifier('11a')
        self.assertEqual('a11', diversifier.reverse())

    def test_reverse_ten_chars(self):
        """
        String should be returned in reversed order
        Even if there are chars twice
        """
        diversifier = Diversifier('11abbb1234')
        self.assertEqual('4321bbba11', diversifier.reverse())


if __name__ == '__main__':
    unittest.main()
