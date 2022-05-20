import pytest
from trackr import create_app
from trackr.db import db
from trackr.models import Item

@pytest.fixture(scope = "module")
def new_item():
    item = Item(
        name = "3DS",
        description = "XL",
        price = 350,
        count = 5
    )
    return item

@pytest.fixture(scope = "module")
def test_client():
    app = create_app()
    app.config.update({
        "TESTING": True
    })
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client

@pytest.fixture(scope = "module")
def init_db(test_client, new_item):
    db.create_all()
    db.session.add(new_item)
    db.session.commit()
    yield
    db.drop_all()
