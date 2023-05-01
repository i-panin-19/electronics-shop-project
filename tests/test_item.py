"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

obj1 = Item('Шоколад', 89.95, 20)

def test_calculate_total_price():
    assert obj1.calculate_total_price() == 1799.0

def test_apply_discount():
    obj1.apply_discount()
    assert obj1.price * Item.pay_rate == obj1.price
    assert obj1.price == 89.95

