from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import fields

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        models = CustomUser
        fields = "__all__"