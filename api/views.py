from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from . import serializers
from .models import Profile, Post, Comment

# Create your views here.
