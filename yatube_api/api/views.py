from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from posts.models import Comment, Group, Post

from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostListView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(ModelViewSet):
    serializer_class = PostSerializer
    lookup_url_kwarg = 'post_id'

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        new_queryset = Post.objects.filter(pk=post_id)
        return new_queryset


class CommentsListView(ModelViewSet):
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'post_id'

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        comments = Comment.objects.filter(post=post_id)
        return comments

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(author=self.request.user, post_id=post_id)


class CommentDetailView(ModelViewSet):
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_id'

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        comments = Comment.objects.filter(post=post_id)
        return comments

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied(
                'Изменение чужого контента запрещено!'
            )
        super(CommentDetailView, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied(
                'Изменение чужого контента запрещено!'
            )
        super(CommentDetailView, self).perform_destroy(instance)


class GroupView(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_url_kwarg = 'group_id'
