"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone
import pytest

obj1 = Item('Шоколад', 89.95, 20)

def test___repr__():
    assert repr(obj1) == "Item('Шоколад', 89.95, 20)"

def test___str__():
    assert str(obj1) == 'Шоколад'

def test___add__():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

def test_calculate_total_price():
    assert obj1.calculate_total_price() == 1799.0

def test_apply_discount():
    obj1.apply_discount()
    assert obj1.price * Item.pay_rate == obj1.price
    assert obj1.price == 89.95

def test_name():
    with pytest.raises(Exception):
        obj1.name = 'СуперпуперШоколад'

    obj1.name = 'Шоколадко'
    assert obj1.name == 'Шоколадко'

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
