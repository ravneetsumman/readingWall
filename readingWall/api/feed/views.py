from rest_framework import permissions, status
from api.feed.serializers import FeedSerializer
from api.models import Feed
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from api.feed.permissions import IsOwner

class FeedCreate(APIView):
    """ This class creates feed"""
    def get(self, request, format=None):
        feed = Feed.objects.all()
        serializer = FeedSerializer(feed, many=True)
        permission_classes = (permissions.IsAuthenticated,)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FeedSerializer(data=request.data)
        permission_classes = (permissions.IsAuthenticated,)
        #return Response(req_sent_count)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        """Save the post data when creating a new wallpost."""
        serializer.save(owner=self.request.user)
