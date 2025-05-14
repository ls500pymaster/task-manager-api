import pytest
from tasks.models import Tag, Task
from tasks.serializers import TagSerializer, TaskSerializer


@pytest.mark.django_db
def test_tag_unique_validation():
    Tag.objects.create(name="Work")
    ser = TagSerializer(data={"name": "work"})
    assert not ser.is_valid()
    assert "Tag with this name already exists." in str(ser.errors)


@pytest.mark.django_db
def test_create_task_with_new_tags():
    data = {
        "title": "Write docs",
        "description": "",
        "status": "pending",
        "tags": [{"name": "docs"}, {"name": "urgent"}],
    }
    ser = TaskSerializer(data=data)
    assert ser.is_valid(), ser.errors
    task = ser.save()

    assert task.tags.count() == 2
    assert Tag.objects.filter(name="docs").exists()
    assert Tag.objects.filter(name="urgent").exists()


@pytest.mark.django_db
def test_update_task_replace_tags():
    tag_old = Tag.objects.create(name="old")
    task = Task.objects.create(title="A", status="pending")
    task.tags.add(tag_old)

    data = {"title": "A", "status": "pending", "tags": [{"name": "new"}]}
    ser = TaskSerializer(task, data=data)
    assert ser.is_valid(), ser.errors
    ser.save()

    assert task.tags.count() == 1
    assert task.tags.first().name == "new"
