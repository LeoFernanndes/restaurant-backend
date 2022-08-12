from rest_framework import routers

from people.viewsets import CustomerViewset


router = routers.SimpleRouter()
router.register("customers", CustomerViewset, basename="customers")

urlpatterns = []
urlpatterns += router.urls