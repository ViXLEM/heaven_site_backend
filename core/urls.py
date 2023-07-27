from django.urls import path, include
from rest_framework import routers

from core import views

router = routers.SimpleRouter()
router.register(r'table_data', views.TableDataSet)
router.register(r'table_view', views.TableView)


urlpatterns = [
    path('', include(router.urls)),
]