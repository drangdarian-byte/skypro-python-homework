from uuid import uuid4

from conftest import BASE_URL


def assert_api_error(response, expected_statuses):
    assert response.status_code in expected_statuses, (
        f"Unexpected status {response.status_code}: {response.text}"
    )
    data = response.json()
    assert isinstance(data.get("error"), (str, dict, list))
    assert data["error"]


def test_post_project_positive(project, api):
    project_id, title, created = project
    assert created.status_code == 201
    assert created.json()["id"] == project_id
    response = api.get(f"{BASE_URL}/projects/{project_id}", timeout=20)
    assert response.status_code == 200
    assert response.json()["title"] == title


def test_post_project_negative_missing_title(api):
    response = api.post(f"{BASE_URL}/projects", json={}, timeout=20)
    assert_api_error(response, {400, 422})


def test_put_project_positive(project, api):
    project_id, _, _ = project
    new_title = f"Updated test {uuid4().hex[:12]}"
    response = api.put(
        f"{BASE_URL}/projects/{project_id}",
        json={"title": new_title},
        timeout=20,
    )
    assert response.status_code == 200
    read_back = api.get(f"{BASE_URL}/projects/{project_id}", timeout=20)
    assert read_back.status_code == 200
    assert read_back.json()["title"] == new_title


def test_put_project_negative_unknown_id(api):
    unknown_id = str(uuid4())
    response = api.put(
        f"{BASE_URL}/projects/{unknown_id}",
        json={"title": "No such project"},
        timeout=20,
    )
    assert_api_error(response, {400, 404})


def test_get_project_positive(project, api):
    project_id, title, _ = project
    response = api.get(f"{BASE_URL}/projects/{project_id}", timeout=20)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id
    assert data["title"] == title


def test_get_project_negative_unknown_id(api):
    response = api.get(
        f"{BASE_URL}/projects/{uuid4()}", timeout=20
    )
    assert_api_error(response, {400, 404})
