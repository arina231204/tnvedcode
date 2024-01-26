# customs_management/views.py
from django.shortcuts import render
from rest_framework import generics
from .models import Permission, TnvedCode, Organization
from .serializers import TnvedCodeSerializer, PermissionSerializer

class PermissionSearchView(generics.ListAPIView):
    serializer_class = PermissionSerializer

    def get_queryset(self):
        code = self.kwargs.get('code', None)
        if code is not None:
            tnved_code = TnvedCode.objects.get(code=code)
            permissions = Permission.objects.filter(code=tnved_code)
            return permissions
        else:
            return Permission.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        context = {'permissions': queryset}
        return render(request, 'tnvedcode/permission_search.html', context)
