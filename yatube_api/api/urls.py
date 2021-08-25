from django.urls import path, include
from rest_framework.authtoken import views

from .views import (CommentDetailView, CommentsListView, GroupView,
                    PostDetailView, PostList)

urlpatterns = [
    path('v1/', include([
        path('api-token-auth/', views.obtain_auth_token),
        path('posts/', PostList.as_view()),
        path('posts/<int:post_id>/', PostDetailView.as_view()),
        path('posts/<int:post_id>/comments/', CommentsListView.as_view()),
        path('posts/<int:post_id>/comments/<int:comment_id>/',
             CommentDetailView.as_view()),
        path('groups/', GroupView.as_view({'get': 'list'})),
        path('groups/<int:group_id>/', GroupView.as_view({'get': 'retrieve'})),
    ]))
]
