import pytest
from rest_framework.test import APIClient

from tasks.models import Task, Tag


@pytest.fixture
def api_client(db, django_user_model):
    user = django_user_model.objects.create_user("tester", "t@test.com", "pass")
    client = APIClient()
    client.force_authenticate(user)
    return client


@pytest.mark.django_db
def test_task_list(api_client):
    Task.objects.create(title="T1", status="pending")
    resp = api_client.get("/api/tasks/")
    assert resp.status_code == 200
    assert resp.data["count"] == 1


@pytest.mark.django_db
def test_task_filter_by_status(api_client):
    Task.objects.create(title="a", status="pending")
    Task.objects.create(title="b", status="done")
    resp = api_client.get("/api/tasks/?status=done")
    assert resp.status_code == 200
    assert resp.data["count"] == 1
    assert resp.data["results"][0]["status"] == "done"


@pytest.mark.django_db
def test_task_filter_by_tag(api_client):
    work = Tag.objects.create(name="work")
    t1 = Task.objects.create(title="x", status="pending")
    t1.tags.add(work)
    Task.objects.create(title="y", status="pending")
    resp = api_client.get("/api/tasks/?tags__name=work")
    assert resp.data["count"] == 1
