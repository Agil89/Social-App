from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import MyUser
from rest_framework.pagination import LimitOffsetPagination
from .serializers import RegisterSerializer
from django.http import Http404


class RegisterView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Created!': serializer.data}, status=status.HTTP_201_CREATED) 
        return Response({'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)