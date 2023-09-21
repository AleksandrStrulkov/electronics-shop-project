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


@pytest.fixture
def phone():
	return Phone("iPhone 14", 120_000, 5, 2)


def test_phone(phone):
	assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"
	assert str(phone) == 'iPhone 14'
	assert phone.name == "iPhone 14"
	assert phone.price == 120000
	assert phone.quantity == 5
	assert phone.calculate_total_price() == 600000
	Phone.pay_rate = 0.8
	phone.apply_discount()
	assert phone.price == 96000.0
	phone.name = 'iPhone 14'
	assert phone.name == 'iPhone 14'
	assert Phone.string_to_number('7') == 7
	assert Phone.string_to_number('7.5') == 7


def test_add_phone():
	phone1 = Phone("iPhone 14", 120_000, 5, 2)
	item1 = Item("Смартфон", 10000, 20)
	assert item1 + phone1 == 25
	assert phone1 + phone1 == 10


