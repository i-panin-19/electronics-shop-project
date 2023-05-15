"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

obj1 = Item('Шоколад', 89.95, 20)

def test___repr__():
    assert repr(obj1) == "Item('Шоколад', 89.95, 20)"

def test___str__():
    assert str(obj1) == 'Шоколад'

def test_calculate_total_price():
    assert obj1.calculate_total_price() == 1799.0

def test_apply_discount():
    obj1.apply_discount()
    assert obj1.price * Item.pay_rate == obj1.price
    assert obj1.price == 89.95

def test_name():
    obj1.name = 'СуперпуперШоколад'
    assert obj1.name == 'Шоколад'
    obj1.name = 'Шоколадко'
    assert obj1.name == 'Шоколадко'

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
