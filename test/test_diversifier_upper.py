"""
Tests for the diversifier which work with uppercase
"""

import unittest

from strdiver.diversifier import Diversifier


class TestDiversifierUpper(unittest.TestCase):
    """
    Holds test methods
    """

    def test_uc_first_with_uc_word(self):
        """
        First char should stay the same if uc already
        """
        diversifier = Diversifier('Word')
        self.assertEqual('Word', diversifier.uc_first())

    def test_uc_first_with_lc_word(self):
        """
        First char should get uc if lc
        """
        diversifier = Diversifier('word')
        self.assertEqual('Word', diversifier.uc_first())

    def test_uc_first_with_single_char(self):
        """
        First char should get uc if input is only a single char
        """
        diversifier = Diversifier('w')
        self.assertEqual('W', diversifier.uc_first())

    def test_uc_first_with_mixed_word(self):
        """
        First char should get uc if input has more than one uc char
        """
        diversifier = Diversifier('woRd')
        self.assertEqual('WoRd', diversifier.uc_first())

    def test_uc_all_single_char(self):
        """
        The char should get uc if input is only a single char
        """
        diversifier = Diversifier('w')
        self.assertEqual('W', diversifier.uc_all())

    def test_uc_all_multi_char(self):
        """
        The chars should get uc if input is more than a single char
        """
        diversifier = Diversifier('woRds')
        self.assertEqual('WORDS', diversifier.uc_all())

    def test_uc_last_with_uc_char(self):
        """
        Char should stay the same if uc already
        """
        diversifier = Diversifier('W')
        self.assertEqual('W', diversifier.uc_last())

    def test_uc_last_with_uc_word(self):
        """
        Last char of word should get uc
        """
        diversifier = Diversifier('word')
        self.assertEqual('worD', diversifier.uc_last())

    def test_uc_last_multi_uc_str(self):
        """
        Last char of string should get uc when multiple uppercase chars are in
        """
        diversifier = Diversifier('SoMe long stRing')
        self.assertEqual('SoMe long stRinG', diversifier.uc_last())


if __name__ == '__main__':
    unittest.main()
