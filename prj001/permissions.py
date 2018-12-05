from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        print(obj.owner, "IsOwnerOrReadOnly-----")
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the GeneralInfo.
        return obj.owner == request.user


class CheckOperationPerm(permissions.BasePermission):# for details
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        print(request.user, obj.owner)

        # 当前用户和资料匹配，即可以查看也可以修改；不匹配，只可以查看。
        if request.method in permissions.SAFE_METHODS:
            if request.user.has_perm('prj001.prj001_operation'):
                return True
            else:
                return False

        else:
            if request.user.has_perm('prj001.prj001_operation'):
                # Write permissions are only allowed to the owner of the GeneralInfo.
                return obj.owner == request.user


