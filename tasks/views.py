from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import Task, Tag
from .serializers import TaskSerializer, TagSerializer
from rest_framework.decorators import action


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.prefetch_related("tags").all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {"status": ["exact"], "tags__name": ["exact"]}
    search_fields = ["title", "description"]

    @action(methods=["POST"], detail=True)
    def tasks(self, request, pk=None):
        task = self.get_object()
        tags = task.tags.all()
        serializer = TaskSerializer(tags, many=True, context={"request": request})
        return Response(serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
