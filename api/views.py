from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post, Group, Follow
from .serializers import (
    CommentSerializer,
    PostSerializer,
    FollowSerializer,
    GroupSerializer,
)

from .permissions import IsAuthorOrReadOnly

from django.contrib.auth import get_user_model
User = get_user_model()

class PostsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('group',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(generics.ListCreateAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class FollowViewSet(generics.ListCreateAPIView):
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__username','=following__username']    

    def perform_create(self, serializer):
        following_user = get_object_or_404(User, username=self.request.data['following'])
        follower_user = self.request.user
        serializer.save(user=follower_user, following_id=following_user.id)

