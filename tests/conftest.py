import pytest
from app import create_app


@pytest.fixture
def factory(monkeypatch):
    def make(place=None):
        if place is None:
            monkeypatch.delenv('APP_PLACE', raising=False)
        else:
            monkeypatch.setenv('APP_PLACE', place)
        app = create_app()
        app.config['TESTING'] = True
        return app
    return make
