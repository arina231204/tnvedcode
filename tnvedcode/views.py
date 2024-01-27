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
    return render(request, 'tnvedcode/create_code.html', {'form': form})

def create_permission(request):
    if request.method == 'POST':
        form = PermissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PermissionForm()
    return render(request, 'tnvedcode/create_code.html', {'form': form})


def delete_tnved_code(request, code):
    try:
        tnved_code = TnvedCode.objects.get(code=code)
    except TnvedCode.DoesNotExist:
        return HttpResponse("Такого объекта не существует", status=404)

    if request.method == 'POST':
        tnved_code.delete()
        return redirect('success')

    return render(request, 'tnvedcode/delete_code.html', {'tnved_code': tnved_code})


def delete_organization(request, name):
    try:
        organization = Organization.objects.get(name=name)
    except Organization.DoesNotExist:
        return HttpResponse("Такого объекта не существует", status=404)

    if request.method == 'POST':
        organization.delete()
        return redirect('success')  # Замените 'your_redirect_url' на необходимый URL

    return render(request, 'tnvedcode/delete_organization.html', {'organization': organization})


def delete_permission(request, code, organization_name):
    try:
        permission = Permission.objects.get(code__code=code, organization__name=organization_name)
    except Permission.DoesNotExist:
        return HttpResponse("Такого объекта не существует", status=404)

    if request.method == 'POST':
        permission.delete()
        return redirect('success')

    return render(request, 'tnvedcode/delete_permission.html', {'permission': permission})

def success_view(request):
    return render(request, 'tnvedcode/success.html')