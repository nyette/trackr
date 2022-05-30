from trackr.models import Item

def test_index_page(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Items" in response.data
    assert b"Trash" in response.data

def test_create_item(test_client):
    response = test_client.get("/create")
    assert response.status_code == 200
    assert b"Save" in response.data

def test_create_item_post_valid(test_client, init_db):
    response = test_client.post(
        "/create",
        data = dict(
            name = "Test Item 2",
            description = "For testing purposes only.",
            price = 0,
            count = 1
        ),
        follow_redirects = True
    )
    assert response.status_code == 200
    assert b"Test Item" in response.data

def test_create_item_post_invalid(test_client, init_db):
    response = test_client.post(
        "/create",
        data = dict(
            name = "Test Item"
        ),
        follow_redirects = True
    )
    assert response.status_code == 200
    assert b"Save" in response.data

def test_get_item_valid(test_client, init_db):
    item = Item.query.filter_by(name = "Test Item").first()
    response = test_client.get(f"/{item.id}")
    assert response.status_code == 200
    assert b"Test Item" in response.data

def test_get_item_invalid(test_client, init_db):
    item = Item.query.filter_by(name = "Test Item").first()
    response = test_client.get(f"/{item.id + 1}")
    assert response.status_code == 404
    assert b"Test Item" not in response.data

def test_update_item(test_client, init_db):
    item = Item.query.filter_by(name = "Test Item").first()
    response = test_client.get(f"/{item.id}/update")
    assert response.status_code == 200
    assert b"Save" in response.data

def test_update_item_post_valid(test_client, init_db):
    item = Item.query.filter_by(name = "Test Item").first()
    response = test_client.post(
        f"/{item.id}/update",
        data = dict(
            name = "Test Item",
            description = "For testing purposes only.",
            price = 0,
            count = 5
        ),
        follow_redirects = True
    )
    assert response.status_code == 200
    assert b"Test Item" in response.data

def test_update_item_post_invalid(test_client, init_db):
    item = Item.query.filter_by(name = "Test Item").first()
    response = test_client.post(
        f"/{item.id}/update",
        data = dict(
            name = ""
        ),
        follow_redirects = True
    )
    assert response.status_code == 200
    assert b"Save" in response.data

def test_delete_item(test_client, init_db):
    item = Item.query.filter_by(name = "Test Item").first()
    response = test_client.get(f"/{item.id}/delete")
    assert response.status_code == 200
    assert b"Delete" in response.data

def test_delete_item_post(test_client, init_db):
    item = Item.query.filter_by(name = "Test Item").first()
    response = test_client.post(
        f"/{item.id}/delete",
        data = dict(
            deletion_comment = "Not Needed"
        ),
        follow_redirects = True
    )
    assert response.status_code == 200
    assert b"The trash bin is empty" not in response.data

def test_restore_item(test_client, init_db):
    item = Item.query.filter_by(name = "Test Item").first()
    response = test_client.post(
        f"/{item.id}/delete",
        data = dict(
            deletion_comment = "Not Needed"
        ),
        follow_redirects = True
    )
    response = test_client.get(
        f"/{item.id}/restore",
        follow_redirects = True
    )
    assert response.status_code == 200
    assert b"The trash bin is empty" in response.data

def test_purge_item(test_client, init_db):
    item = Item.query.filter_by(name = "Test Item").first()
    response = test_client.post(
        f"/{item.id}/delete",
        data = dict(
            deletion_comment = "Not Needed"
        ),
        follow_redirects = True
    )
    response = test_client.get(
        f"/{item.id}/purge",
        follow_redirects = True
    )
    assert response.status_code == 200
    assert b"The trash bin is empty" in response.data
