"""
Tests for the diversifier which work with lowercase
"""

import unittest

from strdiver.diversifier import Diversifier


class TestDiversifierLower(unittest.TestCase):
    """
    Holds test methods
    """

    def test_lc_first_with_lc_word(self):
        """
        First char should stay the same if lc already
        """
        diversifier = Diversifier('word')
        self.assertEqual('word', diversifier.lc_first())

    def test_lc_first_with_uc_word(self):
        """
        First char should get lc if uc
        """
        diversifier = Diversifier('Word')
        self.assertEqual('word', diversifier.lc_first())

    def test_lc_first_with_single_char(self):
        """
        First char should get lc if input is only a single char
        """
        diversifier = Diversifier('W')
        self.assertEqual('w', diversifier.lc_first())

    def test_lc_first_with_mixed_word(self):
        """
        First char should get lc if input has more than one lc char
        """
        diversifier = Diversifier('WoRd')
        self.assertEqual('woRd', diversifier.lc_first())

    def test_lc_all_single_char(self):
        """
        The char should get lc if input is only a single char
        """
        diversifier = Diversifier('W')
        self.assertEqual('w', diversifier.lc_all())

    def test_lc_all_multi_char(self):
        """
        The char should get lc if input is more than a single char
        """
        diversifier = Diversifier('WoRds')
        self.assertEqual('words', diversifier.lc_all())

    def test_lc_last_with_lc_char(self):
        """
        Char should stay the same if lc already
        """
        diversifier = Diversifier('w')
        self.assertEqual('w', diversifier.lc_last())

    def test_lc_last_multi_lc_word(self):
        """
        Last char of string should get lc when multiple lowercase chars are in
        """
        diversifier = Diversifier('sOmE LOng StrinG')
        self.assertEqual('sOmE LOng String', diversifier.lc_last())


if __name__ == '__main__':
    unittest.main()
