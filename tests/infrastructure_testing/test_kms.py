import pytest
from mock import MagicMock, patch

from infrastructure_testing.kms import KMS


class TestMain:
    """ Test Suite for KMS Utility class """

    def setup_method(self):
        self.mock_client = MagicMock()
        self.mock_kms = KMS(self.mock_client)

    def test_get_keys_returns_keys(self):
        """ Test Success: Keys returned """
        fake_key_details = {'KeyId': 'test-key',
                            'KeyArn': 'test-key-arn'}

        fake_key = {'Keys': [fake_key_details]}
        fake_response = [fake_key]
        self.mock_client.get_paginator.return_value.paginate.return_value = \
            fake_response

        sut = self.mock_kms.get_keys()

        assert len(sut) == 1
        assert sut == [fake_key_details]

    def test_get_keys_raises_excpetion(self):
        """ Test Failure: Exception is raised if pagination fails """
        fake_response = '{"HttpResponseCode": 400}'
        self.mock_client.get_paginator.return_value.paginate.return_value = \
            fake_response
        with pytest.raises(TypeError) as exc_info:
            self.mock_kms.get_keys()

        assert 'TypeError' in str(exc_info)

    def test_get_key_aliases_raises_correct_exception(self):
        """ Test Failure: TypeError raised when param is not a list """
        fake_key_id = 'test-key'
        err_message = 'param (key_id) type must be a list'
        with pytest.raises(TypeError) as exc_info:
            self.mock_kms.get_key_aliases(fake_key_id)

        assert type(exc_info.value) != type(err_message)
        assert str(exc_info.value) == err_message


if __name__ == '__main__':
    pytest.main()
