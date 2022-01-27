from tests import client


def test_common_actors():
    response = client.get("/common_actors/?movies=strings,string")
    assert response.status_code == 200


def test_common_actors_not_exist_movie():
    response = client.get("/common_actors/?movies=strings,sdasadas")
    assert response.status_code == 400


def test_common_actors_not_exist_query():
    response = client.get("/common_actors/")
    assert response.status_code == 422
