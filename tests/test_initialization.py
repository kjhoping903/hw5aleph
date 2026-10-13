from app import create_app


def test_place_is_snapshot_at_app_creation(monkeypatch):
    monkeypatch.setenv('APP_PLACE', 'DAEJEON')
    first = create_app()
    monkeypatch.setenv('APP_PLACE', 'SEOUL')
    assert first.test_client().get('/api/hello').get_json() == {
        'message': 'Hello', 'version': 'v2', 'place': 'DAEJEON'}
    assert create_app().test_client().get('/api/hello').get_json()['place'] == 'SEOUL'
