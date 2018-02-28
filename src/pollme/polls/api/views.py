from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#get models
from ..models import Question, Choice

#get serializers
from .serializers import (
    QuestionListSerializer
)

class QuestionListAPIView(APIView):

    def get(self, request, format=None):
        """
        This should list all questions and their choices
        Feel free to use DRF generic class based views
        Otherwise it subclasses APIView
        """
        qs = Question.objects.all()
        serializer = QuestionListSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """nothing required for lab 5"""
        pass

    def put(self, request, format=None):
        """nothing required for lab 5"""
        pass

    def delete(self, request, format=None):
        """nothing required for lab 5"""
        pass
