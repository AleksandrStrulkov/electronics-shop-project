"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def item():
	return Item('смартфон', 20000, 10)


def test_item(item):
	assert repr(item) == "Item('смартфон', 20000, 10)"
	assert str(item) == 'смартфон'
	assert item.name == "смартфон"
	assert item.price == 20000
	assert item.quantity == 10
	assert item.calculate_total_price() == 200000
	Item.pay_rate = 0.8
	item.apply_discount()
	assert item.price == 16000
	item.name = 'Суперсмартфон'
	assert item.name == 'Суперсмарт'
	assert Item.string_to_number('7') == 7
	assert Item.string_to_number('7.5') == 7



