from rest_framework import serializers
from api.models import Connections

class ConnectionsSerializer(serializers.ModelSerializer):
    #friendreq_by = serializers.ReadOnlyField(source='friendreq_by.username')

    class Meta:
        model =  Connections
        fields = ('id', 'friendreq_by', 'friendreq_to')
        read_only_fields = ('date_created', 'date_modified')
