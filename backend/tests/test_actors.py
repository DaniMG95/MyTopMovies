from tests import client


def test_get_actors():
    response = client.get("/actors/")
    assert response.status_code == 200


def test_post_actors():
    response = client.post("/actors/", json={"name": "test11", "age": 14, "gender": "male"})
    assert response.status_code == 200
    assert response.json() == {"name": "test11", "age": 14, "gender": "male"}


def test_post_malformed_actors():
    response = client.post("/actors/", json={"name": "test11", "agsaddsae": 14, "gesdaasdnder": "male"})
    assert response.status_code == 422


def test_post_exists_actors():
    response = client.post("/actors/", json={"name": "test11", "age": 14, "gender": "male"})
    assert response.status_code == 400


def test_post_error_gender_actors():
    response = client.post("/actors/", json={"name": "test", "age": 14, "gender": "dssda"})
    assert response.status_code == 400