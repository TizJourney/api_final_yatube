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


urlpatterns = [
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/', include(router.urls)),
    path('v1/group/', views.GroupViewSet.as_view()),
    path('v1/follow/', views.FollowViewSet.as_view()),
]
