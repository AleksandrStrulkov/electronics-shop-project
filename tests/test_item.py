"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item():
	return Item('смартфон', 20000, 10)


def test_item_initialized(item):
	assert item.name == "смартфон"
	assert item.price == 20000
	assert item.quantity == 10


def test_calculate_total_price(item):
	assert item.calculate_total_price() == 200000


def test_apply_discount(item) -> None:
	Item.pay_rate = 0.8
	item.apply_discount()
	assert item.price == 16000


def test_name(item):
	item.name = 'Суперсмартфон'
	assert item.name == 'Суперсмарт'


def test_string_to_number(item):
	assert Item.string_to_number('7') == 7
	assert Item.string_to_number('7.5') == 7


