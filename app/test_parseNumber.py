from command_handler import parseNumber
import pytest


def test_parseNumber_single_digit():
    dict = {
        "I made workout for 5 mins": 5,
        "57 minutes": 57,
        "I made workout for575mins": 575,
        "5678 minutes": False,
        "Sentense without digits": False,
        "1 hour 30 mins": False,
    }
    for k, v in dict.items():
        assert parseNumber(k) == v
