from django.shortcuts import render

from rest_framework import viewsets
from .serializers import PasswordSerializer
from .models import Passwords

class PasswordViewSet(viewsets.ModelViewSet):
    queryset=Passwords.objects.all().order_by('username')
    serializer_class = PasswordSerializer
# Create your views here.
