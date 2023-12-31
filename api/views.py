from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Action,UserAction
from .serializers import UserActionSerializer, ActionSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# Create your views here.


class CreateUserAction(ModelViewSet):
    queryset = UserAction.objects.all()
    serializer_class = UserActionSerializer


class CreateAction(ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


