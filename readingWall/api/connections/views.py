from rest_framework import permissions, status
from api.connections.serializers import ConnectionsSerializer
from api.models import Connections
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response

class Friends(APIView):
    """ This class adds connections"""
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        connections = Connections.objects.all()
        serializer = ConnectionsSerializer(connections, many=True)
        permission_classes = (permissions.IsAuthenticated,)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ConnectionsSerializer(data=request.data)
        #check if its 
        permission_classes = (permissions.IsAuthenticated,)
        if serializer.is_valid():
            serializer.save(friendreq_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
