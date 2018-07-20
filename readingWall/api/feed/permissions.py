from rest_framework.permissions import BasePermission
from api.models import Feed

class IsOwner(BasePermission):
    """Custom permission class to allow only wallpost owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the wallpost owner."""
        if isinstance(obj, Feed):
            return obj.owner == request.user
        return obj.owner == request.user
