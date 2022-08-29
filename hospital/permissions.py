from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

class IsOwner(permissions.BasePermission): 
    def has_object_permission(self, request, view, obj): 
        return obj.paciente.user == request.user


class IsAuxiliar(permissions.BasePermission):
    def has_permission(self, request, view):
        group_name ='auxiliares'
        if request.method in permissions.SAFE_METHODS:
            return request.user.groups.filter(name__exact=group_name).exists()
        return request.user.groups.filter(name__exact=group_name).exists()

class IsPersonalSalud(permissions.BasePermission):
    def has_permission(self, request, view):
        group_name ='personal_salud'
        if request.method in permissions.SAFE_METHODS:
            print(request.user.groups.filter(name__exact=group_name))
            return request.user.groups.filter(name__exact=group_name).exists()
        return request.user.groups.filter(name__exact=group_name).exists()

class IsPaciente(permissions.BasePermission):
    def has_permission(self, request, view):
        group_name ='pacientes'
        if request.method in permissions.SAFE_METHODS:
            return request.user.groups.filter(name__exact=group_name).exists()
        return request.user.groups.filter(name__exact=group_name).exists()

class IsHistoriaPaciente(permissions.BasePermission):
    def has_permission(self, request, view):
        group_name ='pacientes'
        if request.method in permissions.SAFE_METHODS:
            return request.user.groups.filter(name__exact=group_name).exists()
        return False

class VeSignosVitales(permissions.BasePermission):
    def has_permission(self, request, view):
        group_name ='pacientes'
        group_name2 ='personal_salud'
        if request.method in permissions.SAFE_METHODS:
            return (request.user.groups.filter(name__exact=group_name).exists() or request.user.groups.filter(name__exact=group_name2).exists())
        return request.user.groups.filter(name__exact=group_name2).exists()

