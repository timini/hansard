from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin

from users import views as users_views
from chat import views as chat_views


admin.autodiscover()

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', users_views.UserViewSet)
router.register(r'comments', chat_views.CommentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^users/current', users_views.current_user),
]
