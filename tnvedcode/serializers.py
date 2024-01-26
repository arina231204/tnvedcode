# customs_management/serializers.py
from rest_framework import serializers
from .models import Permission, TnvedCode, Organization

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['organization', 'import_status_legal', 'import_status_individual']

class TnvedCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TnvedCode
        fields = ['code']

class OrganizationSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ['name', 'permissions']
