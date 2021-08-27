from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api import views as api_views

router = DefaultRouter()
router.register(r'posts', api_views.PostView)
router.register(r'^posts/(?P<post_id>\d+)/comments', api_views.CommentsView,
                basename='comments')
router.register(r'groups', api_views.GroupView)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/api-auth/', include('rest_framework.urls',
                                 namespace='rest_framework')),
]
