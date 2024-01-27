from django import forms
from .models import TnvedCode, Organization, Permission

class TnvedCodeForm(forms.ModelForm):
    class Meta:
        model = TnvedCode
        fields = '__all__'

class OrganizationsForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

class OrganizationsForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'


class PermissionForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = '__all__'
