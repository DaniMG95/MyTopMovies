from tests import client


def test_perfomances():
    response = client.get("/performances/?actors=strings,string")
    assert response.status_code == 200


def test_performances_not_exist_actor():
    response = client.get("/performances/?actors=strings,sdasadas")
    assert response.status_code == 400


def test_performances_not_exist_query():
    response = client.get("/performances/")
    assert response.status_code == 422
