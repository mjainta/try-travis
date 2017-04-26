"""
Holds Diviersifier
"""

import json

class Diversifier(object):
    """
    Holds functions for diversify a string in various ways
    """

    def __init__(self, value):
        self.value = value

    def uc_first(self):
        """
        Returns the value with first letter upper case
        """
        val_list = list(self.value)
        val_list[0] = val_list[0].upper()

        return "".join(val_list)

    def lc_first(self):
        """
        Returns the value with first letter lower case
        """
        val_list = list(self.value)
        val_list[0] = val_list[0].lower()

        return "".join(val_list)

    def reverse(self):
        """
        Reverses the value and returns it
        """

        return "".join(reversed(list(self.value)))

    def uc_all(self):
        """
        Returns the value in upper case
        """

        return self.value.upper()

    def lc_all(self):
        """
        Returns the value in lower case
        """

        return self.value.lower()

    def uc_last(self):
        """
        Returns the value with last letter upper case
        """
        val_list = list(self.value)
        index = len(val_list) - 1
        val_list[index] = val_list[index].upper()

        return "".join(val_list)

    def lc_last(self):
        """
        Returns the value with last letter upper case
        """
        val_list = list(self.value)
        index = len(val_list) - 1
        val_list[index] = val_list[index].lower()

        return "".join(val_list)

    def aggregate(self):
        """
        Aggregates the string conversions into one json-string.
        """
        result = {
            "input": self.value,
            "uc_first": self.uc_first(),
            "lc_first": self.lc_first(),
            "reverse": self.reverse(),
            "uc_all": self.uc_all(),
            "lc_all": self.lc_all(),
            "uc_last": self.uc_last(),
            "lc_last": self.lc_last(),
        }

        return json.dumps(result, indent=4)
