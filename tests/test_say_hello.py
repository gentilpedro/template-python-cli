import pytest

from app.domain.greeting import Greeting
from app.use_cases.say_hello import say_hello


def test_say_hello_returns_greeting_message():
    assert say_hello("Gentil") == "Hello, Gentil!"


def test_greeting_rejects_empty_recipient():
    with pytest.raises(ValueError):
        Greeting(recipient="  ")
