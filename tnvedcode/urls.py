from django.urls import path
from . import views

urlpatterns = [
    path('search/<str:code>/', views.PermissionSearchView.as_view(), name='permission-search'),
    path('create_tnved_code/', views.create_tnved_code, name='create_tnved_code'),
    path('create_organization/', views.create_organization, name='create_organization'),
    path('create_permission/', views.create_permission, name='create_permission'),
    path('delete_code/<int:code>/', views.delete_tnved_code, name='delete_code'),
    path('delete_organization/<str:name>/', views.delete_organization, name='delete_organization'),
    path('delete_permission/<int:code>/<str:organization_name>/', views.delete_permission, name='delete_permission'),
    path('success/', views.success_view, name='success'),
    path('notsuccess/', views.notsuccess_view, name='notsuccess'),
    path('code/<int:code>/update/', views.update_code, name='update_code'),
    path('organization/<str:name>/update/', views.update_organization, name='update_organization'),
    path('update_permission/<int:code>/<str:organization_name>/', views.update_permission, name='update_permission'),
    path('codes/', views.all_codes, name='all_codes'),
    path('organizations/', views.all_оrganizations, name='all_оrganizations'),
    path('permissions/', views.all_permissions, name='all_permissions'),


]
