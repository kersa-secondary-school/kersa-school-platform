from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'full_name', 'email', 'phone', 'role']

class StudentApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentApplication
        fields = '__all__'

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class GalleryImageSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    is_saved = serializers.SerializerMethodField()
    class Meta:
        model = GalleryImage
        fields = ['id', 'title', 'category', 'image', 'created_at', 'likes', 'comments', 'is_saved']
    def get_comments(self, obj):
        return CommentSerializer(obj.comments.all(), many=True).data
    def get_is_saved(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.saves.filter(user=request.user).exists()
        return False

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at']

# ... similarly for other models