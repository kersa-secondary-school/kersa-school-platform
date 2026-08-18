from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == 'admin'

class StudentApplicationViewSet(viewsets.ModelViewSet):
    queryset = StudentApplication.objects.all()
    serializer_class = StudentApplicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        app = self.get_object()
        app.status = 'approved'
        app.save()
        return Response({'status': 'approved'})

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAdminOrReadOnly]

class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        img = self.get_object()
        img.likes += 1
        img.save()
        return Response({'likes': img.likes})

    @action(detail=True, methods=['post'])
    def save(self, request, pk=None):
        img = self.get_object()
        Save.objects.create(user=request.user, content_object=img)
        return Response({'saved': True})

# ... other ViewSets