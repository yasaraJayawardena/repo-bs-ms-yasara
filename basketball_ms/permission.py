from rest_framework.permissions import BasePermission
from basketball_ms.models import UserGroup


class IsAdminCoach(BasePermission):
    """
    Allows access only to authenticated users - Admin, coach.
    """

    def has_permission(self, request, view):
        if bool(request.user and request.user.is_authenticated):
            user_group = UserGroup.objects.filter(user=request.user).first()
            return user_group.group.group_category == "ad" or user_group.group.\
                group_category == "c"

        return False


class IsAdminPlayer(BasePermission):
    """
    Allows access only to authenticated users - Admin, Player.
    """

    def has_permission(self, request, view):
        if bool(request.user and request.user.is_authenticated):
            user_group = UserGroup.objects.filter(user=request.user).first()
            return user_group.group.group_category == "ad" or user_group.group.\
                group_category == "p"

        return False


class IsAuth(BasePermission):
    """
    Allows access only to authenticated users - Admin, Coach, Player.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
