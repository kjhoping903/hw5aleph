"""T01-T10: freeze before hello v2 implementation; never alter expectations."""
from flask import Flask


def test_T01_service_start(factory):
    assert isinstance(factory(), Flask)


def test_T02_health_status(factory):
    assert factory().test_client().get('/api/health').status_code == 200


def test_T03_health_json(factory):
    body = factory().test_client().get('/api/health').get_json()
    assert body == {'status': 'ok', 'service': 't05-stateless-handover'}
    assert all(type(value) is str for value in body.values())


def test_T04_hello_status(factory):
    assert factory().test_client().get('/api/hello').status_code == 200


def test_T05_hello_version(factory):
    body = factory().test_client().get('/api/hello').get_json()
    assert type(body['version']) is str
    assert body['version'] == 'v2'


def test_T06_default_place(factory):
    body = factory().test_client().get('/api/hello').get_json()
    assert type(body['place']) is str
    assert body['place'] == 'UNKNOWN'


def test_T07_daejeon(factory):
    body = factory('DAEJEON').test_client().get('/api/hello').get_json()
    assert type(body['place']) is str
    assert body['place'] == 'DAEJEON'


def test_T08_seoul(factory):
    body = factory('SEOUL').test_client().get('/api/hello').get_json()
    assert type(body['place']) is str
    assert body['place'] == 'SEOUL'


def test_T09_info_contract(factory):
    response = factory().test_client().get('/api/info')
    assert response.status_code == 200
    body = response.get_json()
    assert body == {'project': 'T05 Stateless Handover Lab', 'runtime': 'Flask', 'handover': True}
    assert type(body['project']) is str and type(body['runtime']) is str
    assert type(body['handover']) is bool


def test_T10_not_found(factory):
    response = factory().test_client().get('/api/not-found')
    assert response.status_code == 404
    assert response.is_json
    assert response.get_json() == {'error': 'not_found'}
