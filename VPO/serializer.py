from rest_framework import serializers

from .models import User
from .models import User_member
from .models import User_organizer
from .models import Organizer_project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("__all__")


class User_register_member(serializers.ModelSerializer):
    class Meta:
        model = User_member
        fields = ("__all__")


class User_register_organizer(serializers.ModelSerializer):
    class Meta:
        model = User_organizer
        fields = ("__all__")


class User_Organizer_project(serializers.ModelSerializer):
    class Meta:
        model = Organizer_project
        fields = ("__all__")

