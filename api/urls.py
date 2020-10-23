from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

router = DefaultRouter()
router.register(
    r'posts/(?P<post_id>[0-9]+)/comments',
    views.CommentViewSet, basename='CommentViewSet'
)
router.register(r'posts', views.PostsViewSet)

v1_url_patterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('follow/', views.FollowView.as_view()),
    path('group/', views.GroupView.as_view()),
]

urlpatterns = [
    path('v1/', include(v1_url_patterns)),
    path('v1/', include(router.urls)),
]
