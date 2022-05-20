def test_new_item(new_item):
    assert new_item.name == "3DS"
    assert new_item.description == "XL"
    assert new_item.price == 350
    assert new_item.count == 5
    assert not new_item.in_trash
