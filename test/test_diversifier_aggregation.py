"""
Tests for the aggregation of the diversifier functions
"""

import unittest
import json

from strdiver.diversifier import Diversifier


class TestDiversifierAggregation(unittest.TestCase):
    """
    Holds test methods
    """

    def test_is_json_object(self):
        """
        The aggregation should return a strig which can be converted to valid json
        """
        diversifier = Diversifier('sample')

        try:
            json.loads(diversifier.aggregate())
        except json.JSONDecodeError:
            self.fail('No valid JSON was returned.')

    def test_correct_json(self):
        """
        The aggregation should return a strig which can be converted to valid json
        """
        diversifier = Diversifier('saMple')
        result = json.loads(diversifier.aggregate())
        expected = {
            "input": "saMple",
            "uc_first": "SaMple",
            "lc_first": "saMple",
            "reverse": "elpMas",
            "uc_all": "SAMPLE",
            "lc_all": "sample",
            "uc_last": "saMplE",
            "lc_last": "saMple",
        }

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
