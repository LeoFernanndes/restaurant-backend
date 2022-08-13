from rest_framework import routers
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from people.viewsets import UserViewset
from people.views import CustomTokenObtainPairView


router = routers.SimpleRouter()
router.register("users", UserViewset, basename="users")

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token-refresh-view')
]
urlpatterns += router.urls