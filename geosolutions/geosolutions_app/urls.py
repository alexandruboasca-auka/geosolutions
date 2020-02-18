from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api, views

router = DefaultRouter()
router.register(r'points', api.PointViewSet)
router.register(r'searches', api.SearchViewSet)

urlpatterns = [
	path('api/', include(router.urls)),
	path('', views.IndexView.as_view(), name='index')
]