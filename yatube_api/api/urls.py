from django.urls import include, path
from rest_framework.authtoken import views

from .views import (CommentDetailView, CommentsListView, GroupView,
                    PostDetailView, PostListView)

post_list_view = PostListView.as_view({'get': 'list', 'post': 'create'})
post_detail_view = PostDetailView.as_view(
    {'get': 'retrieve',
     'patch': 'partial_update',
     'delete': 'destroy'})
comments_list_view = CommentsListView.as_view(
    {'get': 'list',
     'post': 'create'})
comments_detail_view = CommentDetailView.as_view(
    {'get': 'retrieve',
     'patch': 'partial_update',
     'delete': 'destroy'})

urlpatterns = [
    path('v1/', include([
        path('api-token-auth/', views.obtain_auth_token),
        path('posts/', post_list_view),
        path('posts/<int:post_id>/', post_detail_view),
        path('posts/<int:post_id>/comments/', comments_list_view),
        path('posts/<int:post_id>/comments/<int:comment_id>/',
             comments_detail_view),
        path('groups/', GroupView.as_view({'get': 'list'})),
        path('groups/<int:group_id>/', GroupView.as_view({'get': 'retrieve'})),
    ])),
    path('api-auth/', include('rest_framework.urls')),
]
