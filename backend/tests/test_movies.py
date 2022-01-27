from tests import client


def test_get_movies():
    response = client.get("/movies/")
    assert response.status_code == 200


def test_create_movie():
    response = client.post("/movies/", json={"title": "testttt", "category": "miedo", "cast": ["test11", "string",
                                                                                               "strings"]})
    assert response.status_code == 200
    data = response.json()
    data["cast"] = data["cast"].sort()
    assert data == {"title": "testttt", "category": "miedo", "cast": ["test11", "string", "strings"].sort()}


def test_exist_create_movie():
    response = client.post("/movies/", json={"title": "testttt", "category": "miedo", "cast": ["test11", "string",
                                                                                               "strings"]})
    assert response.status_code == 400


def test_create_movie_not_exist_actor():
    response = client.post("/movies/", json={"title": "testttt", "category": "miedo", "cast": ["test12231", "string",
                                                                                               "strings"]})
    assert response.status_code == 400


def test_malformed_create_movie():
    response = client.post("/movies/", json={"title": "testttt", "dsds": "miedo", "cast": ["test11", "string",
                                                                                           "strings"]})
    assert response.status_code == 422