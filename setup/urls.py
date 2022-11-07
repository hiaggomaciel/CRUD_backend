from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from images.views import ImagesViewSet, UserViewSet, ImagesUpload, ImageListUserViewSet, ImageListUserImagesViewSet, ImageDetailUser

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('images', ImagesViewSet, basename='images')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('users/<int:user_id>/images/', ImageListUserViewSet.as_view()),
    path('users/<int:user_id>/images/<int:image_id>/', ImageListUserImagesViewSet.as_view()),
    path('users/<int:user_id>/images/<int:image_id>/file/', ImageDetailUser),
    path('users/<int:user_id>/images/uploadfiles/', ImagesUpload.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
