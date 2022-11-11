from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,)
from rest_framework import routers
from .views import ImagesViewSet, UserViewSet, ImagesUpload, ImageListUserViewSet, ImageListUserImagesViewSet, ImageDetailUser

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('images', ImagesViewSet, basename='images')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('users/<int:user_id>/images/', ImageListUserViewSet.as_view()),
    path('users/<int:user_id>/images/<int:image_id>/',
         ImageListUserImagesViewSet.as_view()),
    path('users/<int:user_id>/images/<int:image_id>/file/', ImageDetailUser),
    path('users/<int:user_id>/images/uploadfiles/', ImagesUpload.as_view()),
]
