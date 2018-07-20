from rest_framework import serializers
from api.models import Feed


class FeedSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Feed
        fields = ('id', 'owner', 'blog_url', 'context', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
