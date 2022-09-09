import pytest
from trackr import create_app
from config import Config
from trackr.db import db
from trackr.models import Item


@pytest.fixture(scope="module")
def new_item():
    item = Item(
        name="Test Item", description="For testing purposes only.", price=0, count=1
    )
    return item


@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    app.config.from_object(Config)
    url = app.config["SQLALCHEMY_DATABASE_URI"]
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)
    app.config.update(
        {
            "SQLALCHEMY_DATABASE_URI": url,
        }
    )
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client


@pytest.fixture(scope="module")
def init_db(test_client, new_item):
    db.session.add(new_item)
    db.session.commit()
    yield db
    db.session.close()
    db.drop_all()
    db.create_all()
