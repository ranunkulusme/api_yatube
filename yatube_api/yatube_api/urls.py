from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as rest_views

from api import views

router = DefaultRouter()
router.register(r'posts', views.PostView)
router.register(r'^posts/(?P<post_id>\d+)/comments', views.CommentsView,
                basename='comments')
router.register(r'groups', views.GroupView)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/api-token-auth/', rest_views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
