import logging
import random
import time

import pytest
import requests

ENDPOINT = "https://reqres.in"


@pytest.mark.API
def test_get_list_users():
    response = requests.get(ENDPOINT + "/api/users?page=2")
    assert response.status_code == 200
    logging.info("\nStatus code response: {}".format(response.status_code))
    data = response.json()
    per_page = data["per_page"]
    assert len(data) == per_page
    logging.info("\nNumber of users listed per page: {}".format(per_page))


@pytest.mark.API
def test_get_single_user():
    user_id = random.randint(1, 12)
    response = requests.get(ENDPOINT + f"/api/users/{user_id}")
    assert response.status_code == 200
    logging.info("\nStatus code response: {}".format(response.status_code))
    data = response.json()
    assert data["data"]["id"] == user_id
    logging.info("\nUser_id returned: {}".format(data["data"]["id"]))
    logging.info("\nUser first name: {}".format(data["data"]["first_name"]))
    logging.info("\nUser last name: {}".format(data["data"]["last_name"]))
    logging.info("\nUser email: {}".format(data["data"]["email"]))


@pytest.mark.API
def test_single_user_not_found():
    user_id = 23
    response = requests.get(ENDPOINT + f"/api/users/{user_id}")
    assert response.status_code == 404
    logging.info("\nStatus code response: {}".format(response.status_code))


@pytest.mark.API
def test_list_resource():
    response = requests.get(ENDPOINT + "/api/unknown")
    # Concern about API url: /unknown ?
    assert response.status_code == 200
    logging.info("\nStatus code response: {}".format(response.status_code))
    data = response.json()
    per_page = data["per_page"]
    assert len(data) == per_page
    logging.info("\nNumber of resource returned: {}".format(per_page))


@pytest.mark.API
def test_single_resource():
    resource_id = random.randint(1, 6)
    response = requests.get(ENDPOINT + f"/api/unknown/{resource_id}")
    assert response.status_code == 200
    logging.info("\nStatus code response: {}".format(response.status_code))
    data = response.json()
    assert data["data"]["id"] == resource_id
    logging.info("\nResource id: {}".format(data["data"]["id"]))
    logging.info("\nResource name: {}".format(data["data"]["name"]))


@pytest.mark.API
def test_single_resource_not_found():
    resource_id = 23
    response = requests.get(ENDPOINT + f"/api/unknown/{resource_id}")
    assert response.status_code == 404
    logging.info("\nStatus code response: {}".format(response.status_code))


@pytest.mark.API
def test_create_user():
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    create_user_response = requests.post(ENDPOINT + "/api/users", json=payload)
    assert create_user_response.status_code == 201
    logging.info("\nStatus code response: {}".format(create_user_response.status_code))

    data = create_user_response.json()
    assert str(payload["name"]) == data["name"]
    logging.info("\nUser name: {}".format(data["name"]))
    assert str(payload["job"]) == data["job"]
    logging.info("\nUser job: {}".format(data["job"]))


# TBD: we have to get single user base on use_id after creating to make sure creation successfully


@pytest.mark.API
def test_update_user_using_put():
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    user_id = 2
    update_user_response = requests.put(ENDPOINT + f"/api/users/{user_id}", json=payload)
    assert update_user_response.status_code == 200
    logging.info("\nStatus code response: {}".format(update_user_response.status_code))

    data = update_user_response.json()
    assert str(payload["name"]) == data["name"]
    logging.info("\nUser name: {}".format(data["name"]))
    assert str(payload["job"]) == data["job"]
    logging.info("\nUser job: {}".format(data["job"]))

# TBD: We have to get single user again to make sure we can update successfully


@pytest.mark.API
def test_update_user_using_patch():
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    user_id = 2
    update_user_response = requests.patch(ENDPOINT + f"/api/users/{user_id}", json=payload)
    assert update_user_response.status_code == 200
    logging.info("\nStatus code response: {}".format(update_user_response.status_code))

    data = update_user_response.json()
    assert str(payload["name"]) == data["name"]
    logging.info("\nUser name: {}".format(data["name"]))
    assert str(payload["job"]) == data["job"]
    logging.info("\nUser job: {}".format(data["job"]))

# TBD: We have to get single user again to make sure we can update successfully


@pytest.mark.API
def test_delete_user():
    user_id = 2
    response = requests.delete(ENDPOINT + f"/api/users/{user_id}")
    assert response.status_code == 204
    logging.info("\nStatus code response: {}".format(response.status_code))


# TBD: We have to get single user again base on user_id after deleting


@pytest.mark.API
def test_register_successful():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(ENDPOINT + "/api/register", json=payload)
    assert response.status_code == 200
    logging.info("\nStatus code response: {}".format(response.status_code))


@pytest.mark.API
def test_register_unsuccessful():
    payload = {
        "email": "sydney@fife"
    }
    response = requests.post(ENDPOINT + "/api/register", json=payload)
    assert response.status_code == 400
    logging.info("\nStatus code response: {}".format(response.status_code))

    data = response.json()
    assert data["error"] == "Missing password"
    logging.info("\nError response: {}".format(data["error"]))


@pytest.mark.API
def test_login_successful():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(ENDPOINT + "/api/login", json=payload)
    assert response.status_code == 200
    logging.info("\nStatus code response: {}".format(response.status_code))


@pytest.mark.API
def test_login_unsuccessful():
    payload = {
        "email": "peter@klaven"
    }
    response = requests.post(ENDPOINT + "/api/login", json=payload)
    assert response.status_code == 400
    logging.info("\nStatus code response: {}".format(response.status_code))
    data = response.json()
    assert data["error"] == "Missing password"
    logging.info("\n Error response: {}".format(data["error"]))


@pytest.mark.API
def test_delayed_response():
    response = requests.get(ENDPOINT + "/api/users?delay=3")
    time.sleep(3)
    assert response.status_code == 200
    logging.info("\nStatus code response: {}".format(response.status_code))

    data = response.json()
    assert data["per_page"] == len(data)
    logging.info("\nNumber of user response per page: {}".format(len(data)))

