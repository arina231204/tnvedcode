
from django.urls import path
from .views import PermissionSearchView

urlpatterns = [
    path('search/<str:code>/', PermissionSearchView.as_view(), name='permission-search'),

]
