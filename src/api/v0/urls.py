from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, PersonViewSet

people_list = PersonViewSet.as_view({
    'get': 'list'
})



router = DefaultRouter()
router.register(r'users', RoomViewSet, base_name='users')
router.register(r'rooms', RoomViewSet, base_name='rooms')
router.register(r'people', PersonViewSet, base_name='people')


urlpatterns = router.urls