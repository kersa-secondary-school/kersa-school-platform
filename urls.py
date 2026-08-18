from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from core.views import *

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('applications', StudentApplicationViewSet)
router.register('announcements', AnnouncementViewSet)
router.register('resources', ResourceViewSet)
router.register('gallery', GalleryImageViewSet)
router.register('stories', StoryViewSet)
router.register('achievements', AchievementViewSet)
router.register('meetings', MeetingViewSet)
router.register('reviews', ReviewViewSet)
router.register('messages', MessageViewSet, basename='message')
router.register('activity-logs', ActivityLogViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]
