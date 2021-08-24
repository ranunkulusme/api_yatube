from django.urls import path
from rest_framework.authtoken import views

from .views import (CommentDetailView, CommentsListView, GroupView,
                    PostDetailView, PostList)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/posts/', PostList.as_view()),
    path('api/v1/posts/<int:post_id>/', PostDetailView.as_view()),
    path('api/v1/posts/<int:post_id>/comments/', CommentsListView.as_view()),
    path('api/v1/posts/<int:post_id>/comments/<int:comment_id>/',
         CommentDetailView.as_view()),
    path('api/v1/groups/', GroupView.as_view({'get': 'list'})),
    path('api/v1/groups/<int:group_id>/', GroupView.as_view(
        {'get': 'retrieve'})),
]
