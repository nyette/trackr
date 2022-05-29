def test_new_item(new_item):
    assert new_item.name == "Test Item"
    assert new_item.description == "For testing purposes only."
    assert new_item.price == 0
    assert new_item.count == 1
    assert not new_item.in_trash
