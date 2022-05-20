def test_index_page(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Items" in response.data
    assert b"Trash" in response.data

def test_create_item(test_client):
    response = test_client.get("/create")
    assert response.status_code == 200
    assert b"Save" in response.data

def test_create_item_post_with_valid_data(test_client, init_db):
    response = test_client.post(
        "/create",
        data = dict(
            name = "JoyCons",
            description = "Red/Blue",
            price = 80,
            count = 100
        ),
        follow_redirects = True
    )
    assert response.status_code == 200
    assert b"JoyCons" in response.data

def test_create_item_post_with_invalid_data(test_client, init_db):
    response = test_client.post(
        "/create",
        data = dict(
            name = "JoyCons"
        ),
        follow_redirects = True
    )
    assert response.status_code == 200
    assert b"Save" in response.data
