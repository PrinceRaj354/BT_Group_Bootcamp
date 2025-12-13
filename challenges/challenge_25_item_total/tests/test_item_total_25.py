import pytest
from challenges.challenge_25_item_total.item_total import calculate_item_total

def test_valid_item_total():
    result = calculate_item_total("A101", "Pen", 10, 5)
    assert result["total"] == 50

def test_single_quantity():
    result = calculate_item_total("B202", "Notebook", 1, 40)
    assert result["total"] == 40

def test_invalid_quantity():
    with pytest.raises(ValueError):
        calculate_item_total("C303", "Book", 0, 100)

def test_invalid_price():
    with pytest.raises(ValueError):
        calculate_item_total("D404", "Bag", 2, -500)

def test_empty_item_code():
    with pytest.raises(ValueError):
        calculate_item_total("", "Marker", 3, 20)
