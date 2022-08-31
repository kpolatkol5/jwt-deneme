from rest_framework import permissions


class PersonPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user

        #kullanııc get isteklerine direkt cevap verecektir (SAFE_METHODS)
        # eğer Post delete gibi istekler varsa giriş yapan kullanıcının ilgili objenin sahibi mi kontrol edecektir
        #ancak jwt ile login olma işlemini yapamadığım için bunu ekleyemiyorum