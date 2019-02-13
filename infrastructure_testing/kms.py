import json


class KMS:
    """ Class for testing KMS"""

    def __init__(self, key, policy):
        """ Initialise Object """
        self.key = key
        self.policy = policy
