"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone():
	return Phone("iPhone 14", 120_000, 5, 2)


def test_phone(phone):
	assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"
	assert str(phone) == 'iPhone 14'
	assert phone.number_of_sim == 2


def test_number_of_sim(phone):
	phone1 = Phone("iPhone 14", 120_000, 10, 3)
	assert phone1.number_of_sim == 3
	with pytest.raises(ValueError):
		phone1.number_of_sim = 0


def test_add_phone(phone):
	phone1 = Phone("iPhone 14", 120_000, 5, 2)
	item1 = Item("Смартфон", 10000, 20)
	assert item1 + phone1 == 25
	assert phone1 + phone1 == 10
	with pytest.raises(ValueError):
		phone1 + 10 == 30