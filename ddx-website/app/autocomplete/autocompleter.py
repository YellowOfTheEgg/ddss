from typing import List


class Autocompleter:
    """Implements a simple auto complete functionality based on the provided data.
    """

    def __init__(self, options: List[str]):
        self.options = options

    def complete(self, term):
        """Returns a list of strings that contain the provided term from data."""
        if not term:
            return self.options

        matches = [string for string in self.options if term.lower() in string]

        return matches
