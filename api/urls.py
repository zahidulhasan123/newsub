from rest_framework.routers import DefaultRouter
from .views import InstituteViewSet

router = DefaultRouter()
router.register('institutes', InstituteViewSet, basename='institute')
urlpatterns = router.urls
