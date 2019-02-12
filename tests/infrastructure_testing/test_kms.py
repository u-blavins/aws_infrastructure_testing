import pytest
from mock import MagicMock
from infrastructure_testing.main import *


class TestMain:
    """ Test Suite for main.py """

    def setup_method(self):
        self.policy = {
            'Test': 'test'
        }
