from rest_framework.routers import DefaultRouter
from .views import RoomViewSet


router = DefaultRouter()
router.register(r'rooms', RoomViewSet, base_name='rooms')

urlpatterns = router.urls