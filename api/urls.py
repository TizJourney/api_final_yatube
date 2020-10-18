import rest_framework.authtoken.views as authtoken_views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(
    r'posts/(?P<post_id>[0-9]+)/comments',
    views.CommentViewSet, basename='CommentViewSet'
)
router.register(r'posts', views.PostsViewSet)


urlpatterns = [
    path('v1/api-token-auth/', authtoken_views.obtain_auth_token),
    path('v1/', include(router.urls)),
]
