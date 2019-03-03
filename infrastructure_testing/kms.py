"""Utility class for KMS"""


class KMS:
    """Utility class for KMS"""

    def __init__(self, client):
        """Initialise KMS Class"""
        self.client = client

    def get_keys(self):
        """
        Make an AWS call to list keys within the account

        Returns:
            keys(list): list of kms keys
        """
        keys = []
        try:
            paginator = self.client.get_paginator('list_keys')
            response_iter = paginator.paginate()

            for page in response_iter:
                for key in page['Keys']:
                    keys.append(key)
        except Exception as error:
            raise error
        return keys

    def get_key_aliases(self, key_id=''):
        """
        Make an AWS call to list key aliases' within the
        account

        Args:
            key_id(str): kms key id
        Returns:
            aliases(dict): JSON response containg key alias
        """
        aliases = []
        if key_id != '':
            if isinstance(key_id, list):
                print('Do Something')
            else:
                raise TypeError('param (key_id) type must be a list')
        return aliases
