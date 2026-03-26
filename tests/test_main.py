from fastapi.testclient import TestClient

from main import app


client = TestClient(app)

def test_read_sheep():

    response = client.get("/sheep/1")

    assert response.status_code == 200

    assert response.json() == {

        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

def test_add_sheep():

    new_sheep = {
        "id": 7,
        "name": "Suffolk",
        "breed": "Merino",
        "sex": "ewe"
    }


    response = client.post("/sheep/", json=new_sheep)


    assert response.status_code == 201


    data = response.json()
    assert data["name"] == new_sheep["name"]
    assert data["breed"] == new_sheep["breed"]
    assert data["sex"] == new_sheep["sex"]


    sheep_id = data["id"]
    get_response = client.get(f"/sheep/{sheep_id}")

    assert get_response.status_code == 200
    assert get_response.json()["name"] == new_sheep["name"]
