import os
from uuid import uuid4

import pytest
import requests


BASE_URL = os.getenv(
    "YOUGILE_API_URL", "https://yougile.com/api-v2"
).rstrip("/")


@pytest.fixture(scope="session")
def api():
    token = os.getenv("YOUGILE_API_TOKEN")
    if not token:
        pytest.skip("Set YOUGILE_API_TOKEN to run YouGile API tests")
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    })
    yield session
    session.close()


@pytest.fixture
def project(api):
    title = f"Skypro API test {uuid4().hex[:12]}"
    payload = {"title": title}
    user_id = os.getenv("YOUGILE_USER_ID")
    if user_id:
        payload["users"] = {user_id: "admin"}
    response = api.post(f"{BASE_URL}/projects", json=payload, timeout=20)
    assert response.status_code == 201, (
        f"Unable to prepare project: {response.status_code} "
        f"{response.text[:300]}"
    )
    project_id = response.json()["id"]
    try:
        yield project_id, title, response
    finally:
        # YouGile project API uses soft deletion via PUT.
        cleanup = api.put(
            f"{BASE_URL}/projects/{project_id}",
            json={"deleted": True},
            timeout=20,
        )
        if cleanup.status_code not in (200, 201):
            pytest.fail(
                f"Could not clean test project {project_id}: "
                f"{cleanup.status_code}: {cleanup.text[:300]}"
            )
