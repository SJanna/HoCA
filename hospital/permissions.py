from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

class IsMedicoOwner(permissions.BasePermission):
    message = 'Only the Owner has access.'
    """
    las empresas solo podran ver a la información vinculada a su usuario
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.usuario == request.user
            # Check permissions for write requesty
        return obj.usuario == request.user

class IsAuxiliar(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method not in permissions.SAFE_METHODS:
            return False

        group_name ='auxiliares'
        if request.user.groups.filter(name__exact=group_name).exists():
            return True

        return False


#Corregir permisos 
class IsPersonalSalud(permissions.BasePermission):
    def has_permission(self, request, view):
        group_name ='personal_salud'
        if request.user.groups.filter(name__exact=group_name).exists() and request.method in permissions.SAFE_METHODS:
            return True
        return True
