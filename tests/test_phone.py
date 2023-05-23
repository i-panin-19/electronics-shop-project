from src.phone import Phone

obj2 = Phone("iPhone 14", 120_000, 5, 2)

def test___repr__():
    assert repr(obj2) == "Phone('iPhone 14', 120000, 5, 2)"

def test___str__():
    assert str(obj2) == 'iPhone 14'

def test_calculate_total_price():
    assert obj2.calculate_total_price() == 600_000.0

def test_apply_discount():
    obj2.apply_discount()
    assert obj2.price * Phone.pay_rate == obj2.price
    assert obj2.price == 120_000.0

def test_name():
    obj2.name = 'Apple iPhone 14'
    assert obj2.name == 'iPhone 14'
    obj2.name = 'iPhone14p'
    assert obj2.name == 'iPhone14p'

def test_number_of_sim():
    obj2.number_of_sim = 1
    assert obj2.number_of_sim == 1
    obj2.number_of_sim = -1
    assert obj2.number_of_sim == 1

