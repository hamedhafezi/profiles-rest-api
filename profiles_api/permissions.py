from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    '''Allow user to edit their own profile'''

    def has_object_permission(self, requset, view, obj):
        print("=============>", obj)
        '''Check user is trying to edit their own profile'''
        if requset.method in permissions.SAFE_METHODS:
            return True
        return obj.id == requset.user.id
