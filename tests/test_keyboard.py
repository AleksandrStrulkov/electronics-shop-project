"""Здесь надо написать тесты с использованием pytest для модуля keyboard"""
import pytest
from src.item import Item
from src.keyboard import MixinChange, Keyboard


@pytest.fixture
def keyboard():
	return Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard(keyboard):
	assert str(keyboard) == "Dark Project KD87A"
	assert str(keyboard.language) == "EN"
	keyboard.change_lang()
	assert str(keyboard.language) == "RU"
	keyboard.change_lang()
	assert str(keyboard.language) == "EN"

