from rest_framework import serializers
from .models import Task, Tag
from rest_framework.validators import UniqueValidator


class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=30,
        validators=[
            UniqueValidator(
                queryset=Tag.objects.all(),
                lookup="iexact",
                message="Tag with this name already exists.",
            )
        ],
        help_text="The name of the tag",
    )

    class Meta:
        model = Tag
        fields = ["id", "name"]


class TaskSerializer(serializers.ModelSerializer):
    """
    Nested‐write serializer:
    - Accepts list of tags as [{"name": "work"}, …] on create/update.
    - Returns full tag objects in responses.
    """

    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = ["id", "title", "description", "status", "created_at", "tags"]
        read_only_fields = ["id", "created_at"]

    def _get_or_create_tags(self, tags_data):
        names = [t["name"] for t in tags_data]
        existing = Tag.objects.filter(name__in=names).in_bulk(field_name="name")
        new_names = [n for n in names if n not in existing]
        # Use bulk_create for single query
        Tag.objects.bulk_create([Tag(name=n) for n in new_names])
        return Tag.objects.filter(name__in=names)

    def create(self, validated_data):
        tags_data = validated_data.pop("tags", [])
        task = Task.objects.create(**validated_data)
        task.tags.set(self._get_or_create_tags(tags_data))
        return task

    def update(self, instance, validated_data):
        tags_data = validated_data.pop("tags", None)
        instance = super().update(instance, validated_data)

        if tags_data is not None:
            instance.tags.set(self._get_or_create_tags(tags_data))
        return instance
