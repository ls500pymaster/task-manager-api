from rest_framework import serializers
from .models import Task, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ["id", "name"]

    # Extra validation to avoid case-insensitive duplicates
    def validate_name(self, value: str) -> str:
        if Tag.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("Tag with this name already exists.")
        return value


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

        def _get_or_create_tags(self, tag_data_list):
            tag_objs = []
            for tag_data in tag_data_list:
                tag_objs.append(Tag.objects.get_or_create(name=tag_data["name"])[0])
            return tag_objs

        def create(self, validated_data):
            tags_data = validated_data.pop("tags", [])
            task = Task.objects.create(**validated_data)
            task.tags.set(self._get_or_create_tags(tags_data))
            return task

        def update(self, instance, validated_data):
            tags_data = validated_data.pop("tags", None)
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()

            if tags_data is not None:
                instance.tags.set(self._get_or_create_tags(tags_data))
            return instance