"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def test_item():
	return Item(['смартфон', 20000, 10])


def test_calculate_total_price(test_item):
	assert test_item.calculate_total_price() == 12500*10


def test_apply_discount(test_item):
	assert test_item.apply_discout() == 8000
