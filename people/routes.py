from rest_framework import routers
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_nested import routers as nested_routers

from people.viewsets import UserViewset
from people.views import CustomTokenObtainPairView, UpdateUserRoleApiView
from common.viewsets import PersonAddressViewset


router = routers.SimpleRouter()
router.register("users", UserViewset, basename="users")

addresses_router = nested_routers.NestedSimpleRouter(router, 'users', lookup='user')
addresses_router.register('addresses', PersonAddressViewset, basename='addresses')


urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token-refresh-view'),
    path('users/<int:pk>/set_role', UpdateUserRoleApiView.as_view(), name='user-update-role')
]

urlpatterns += router.urls
urlpatterns += addresses_router.urls