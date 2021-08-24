from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from posts.models import Comment, Group, Post

from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = 'post_id'


class CommentsListView(ListCreateAPIView):
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'post_id'

    def get_queryset(self):
        post_id = self.kwargs['post_id']

        posts = Post.objects.filter(pk=post_id).exists()
        if not posts:
            raise PermissionDenied(f'Нет постов с id: {post_id}')

        comments = Comment.objects.filter(post=post_id)
        if not comments.exists():
            raise PermissionDenied(f'Нет комментариев к посту с id: {post_id}')

        return comments

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(author=self.request.user, post_id=post_id)


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_id'


class GroupView(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_url_kwarg = 'group_id'
