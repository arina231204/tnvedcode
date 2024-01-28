from rest_framework import generics
from django.shortcuts import render, redirect
from .forms import TnvedCodeForm, OrganizationsForm, PermissionForm
from .models import Permission,TnvedCode, Organization

from .serializers import PermissionSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


class PermissionSearchView(generics.ListAPIView):
    serializer_class = PermissionSerializer

    def get_queryset(self):
        code = self.kwargs.get('code', None)
        if code is not None:
            try:
                tnved_code = TnvedCode.objects.get(code=code)
                permissions = Permission.objects.filter(code=tnved_code)
                return permissions
            except TnvedCode.DoesNotExist:
                return Permission.objects.none()
        else:
            return Permission.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        context = {'permissions': queryset}
        return render(request, 'tnvedcode/permission_search.html', context)




def create_tnved_code(request):
    if request.method == 'POST':
        form = TnvedCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TnvedCodeForm()
    return render(request, 'tnvedcode/create_code.html', {'form': form})


def create_organization(request):
    if request.method == 'POST':
        form = OrganizationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = OrganizationsForm()
    return render(request, 'tnvedcode/create_organization.html', {'form': form})

def create_permission(request):
    if request.method == 'POST':
        form = PermissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PermissionForm()
    return render(request, 'tnvedcode/create_permission.html', {'form': form})


def delete_tnved_code(request, code):
    try:
        tnved_code = TnvedCode.objects.get(code=code)
    except TnvedCode.DoesNotExist:
        return redirect('notsuccess')

    if request.method == 'POST':

        tnved_code.delete()
        return redirect('success')

    return render(request, 'tnvedcode/delete_code.html', {'tnved_code': tnved_code})


def delete_organization(request, name):
    try:
        organization = Organization.objects.get(name=name)
    except Organization.DoesNotExist:
        return redirect('notsuccess')

    if request.method == 'POST':
        organization.delete()
        return redirect('success')

    return render(request, 'tnvedcode/delete_organization.html', {'organization': organization})


def delete_permission(request, code, organization_name):
    try:
        permission = Permission.objects.get(code__code=code, organization__name=organization_name)
    except Permission.DoesNotExist:
        return redirect('notsuccess')

    if request.method == 'POST':
        permission.delete()
        return redirect('success')

    return render(request, 'tnvedcode/delete_permission.html', {'permission': permission})



def update_code(request, code):
    try:
        tnved_code = TnvedCode.objects.get(code=code)
    except TnvedCode.DoesNotExist:
        return redirect('notsuccess')

    if request.method == 'POST':
        form = TnvedCodeForm(request.POST, instance=tnved_code)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TnvedCodeForm(instance=tnved_code)

    return render(request, 'tnvedcode/update_code.html', {'form': form, 'code': code})


def update_organization(request, name):
    try:
        organization = Organization.objects.get(name=name)
    except Organization.DoesNotExist:
        return redirect('notsuccess')

    if request.method == 'POST':
        form = OrganizationsForm(request.POST, instance=organization)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = OrganizationsForm(instance=organization)

    return render(request, 'tnvedcode/update_organizations.html', {'form': form})

def update_permission(request, code, organization_name):
    try:
        permission = Permission.objects.get(code__code=code, organization__name=organization_name)
    except Permission.DoesNotExist:
        return redirect('notfound')

    if request.method == 'POST':
        form = PermissionForm(request.POST, instance=permission)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PermissionForm(instance=permission)

    return render(request, 'tnvedcode/update_permission.html', {'form': form, 'permission': permission})

def all_codes(request):
    tnved_codes = TnvedCode.objects.all()
    return render(request, 'tnvedcode/all_codes.html', {'tnved_codes': tnved_codes})

def all_оrganizations(request):
    organizations = Organization.objects.all()
    return render(request, 'tnvedcode/all_organizations.html', {'organizations': organizations})

def all_permissions(request):
    permissions = Permission.objects.all()
    return render(request, 'tnvedcode/all_permissions.html', {'permissions': permissions})







def success_view(request):
    return render(request, 'tnvedcode/success.html')

def notsuccess_view(request):
    return render(request, 'tnvedcode/notsuccess.html')